try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    mit_license = f.read()

setup(
    name='dta_test',
    version='0.1',
    packages=find_packages(exclude=('tests', 'docs')),
    url='https://github.com/arturosolutions/dta_test',
    license=mit_license,
    author='Arturo Gonzalez',
    author_email='arturo@arturosolutions.com.au',
    description='Login system that provides authentication to businesses.',
    long_description=readme
)
