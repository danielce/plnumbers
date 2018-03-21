#!/usr/bin/env python
# -*- coding: utf-8 -*-
import importlib
import re
from .countries import data, reverse_data


class PhoneNumber(object):
    """ Class that represents polish phone number """
    _NUMBERTYPES = None

    # Minimum length of valid phone number
    _MIN_LENGTH = 3

    # Maximum length of valid phone number
    _MAX_LENGTH = 17

    # Default length of phone number which also indicates
    # that given number has not leading plus or zeroes
    _DEFAULT_LEN = 9

    # Only polish numbers are supported at the moment
    _DEFAULT_COUNTRY = 'PL'

    # True if parsed number starts with + sign
    _LEADING_PLUS = False

    # True if parsed numbers starts with zeroes
    _LEADING_ZERO = False

    def __init__(self, number, leading_zero=False, prefix=None,
                 leading_plus=False, country=None, raw=None):
        if not raw:
            return PhoneNumber.parse(number)
        self.number = number
        self.leading_zero = leading_zero
        self.leading_plus = leading_plus
        self.prefix = prefix
        self.country = country
        self.raw = raw
        self.get_carrier()

    def get_carrier(self):
        """ Returns name of carrier to which parsed number belongs """
        number = self.number
        if not self.prefix or not self.country:
            self.carrier = None
            return
        try:
            mod = importlib.import_module(
                'plnumbers.{}'.format(self.country)
            )
        except ImportError:
            self.carrier = None
            return

        self._NUMBERTYPES = mod.LANE_TYPE
        match = None
        for pattern, value in mod.LOOKUPS:
            if re.search(pattern, number):
                match = mod.CARRIERS[value]
                break

        if match:
            self.numbertype = self._NUMBERTYPES.get(match[1])
            self.carrier = match[0]
        else:
            self.numbertype = self._NUMBERTYPES.get('u')
            self.carrier = None

    @classmethod
    def check_length(self, number):
        """
        Validator that examines if parsed number is valid
        according to minimum and maximum length.
        """
        if PhoneNumber._MIN_LENGTH > len(number):
            raise ValueError('PhoneNumber too short')

        if PhoneNumber._MAX_LENGTH < len(number):
            raise ValueError('PhoneNumber too long')

    @classmethod
    def parse(cls, number):
        raw = number
        leading_plus = cls._LEADING_PLUS
        leading_zero = cls._LEADING_ZERO
        number = "".join(str(number).split())

        cls.check_length(number)

        if len(number) == cls._DEFAULT_LEN:
            return cls.create_default(number)

        if number[0] == '+':
            number = number[1:]
            leading_plus = True
        elif number[0:1] == '00':
            leading_zero = True
            number = number[2:]

        country_prefix, number = number[0:2], number[2:]
        country_code = reverse_data().get(
            country_prefix, None
        )

        return cls(
            number=number,
            leading_zero=leading_zero,
            leading_plus=leading_plus,
            prefix=country_prefix,
            country=country_code,
            raw=raw,
        )

    @classmethod
    def create_default(cls, number):
        """
        Creates PhoneNumber object if it
        """
        country_prefix = data.get(cls._DEFAULT_COUNTRY)

        return cls(
            number=number,
            leading_zero=cls._LEADING_ZERO,
            leading_plus=cls._LEADING_PLUS,
            prefix=country_prefix,
            country=cls._DEFAULT_COUNTRY,
            raw=number,
        )

    def is_fixed(self):
        """ checks if parsed number is fixed/landline """
        return self.numbertype == self._NUMBERTYPES['l']

    def is_mobile(self):
        """ chekcs if parsed number is valid gsm number"""
        return self.numbertype == self._NUMBERTYPES['m']

    def is_human(self):
        """ returns True if number is identified as fixed or
        gsm excluding ivr, special numbers and so on"""
        ntype = self.numbertype
        return ((ntype == self._NUMBERTYPES['l']) or
                (ntype == self._NUMBERTYPES['m']))

    def __unicode__(self):
        return "<{} ({}): {}>".format(
            self.country,
            self.carrier, self.number)

    def __repr__(self):
        return "<{} ({}): {}>".format(
            self.country,
            self.carrier, self.number)

    def __str__(self):
        return self.number
