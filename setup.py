from plnumbers import __version__
from setuptools import setup

setup(name='plnumbers',
      version=__version__,
      description='Polish Phone Numbers',
      url='http://github.com/danielce/plnumbers',
      author='Daniel Cichowski',
      author_email='d.cichowski@gmail.com',
      license='MIT',
      packages=['plnumbers'],
      test_suite='plnumbers.tests',
      zip_safe=False)
