plnumbers Python Library
===========================

plnumbers Python Library
===========================

Phone number parsing library dedicated for identifying polish national numbers.
It can recognize both line type and carrier name.

Example Usage
-------------

PhoneNumber is object that represents valid phone number. Just provide phone number as string and pass to parse method.

```pycon
>>> from plnumbers import PhoneNumber
>>> number = PhoneNumber.parse('+48601000000')
>>> number
<PL (Polkomtel): 601000000>
>>> number.is_mobile()
True
>>> number.is_fixed()
False
```

