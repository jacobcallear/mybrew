from setuptools import setup, find_packages

setup(
    name='mybrew',
    version='0.1.0',
    url='https://github.com/jacobcallear/mybrew',
    author='Jacob Callear',
    author_email='jacob18@callear.net',
    description='Intuitive command-line interface for a cafe database.',
    packages=find_packages(),
    install_requires=['prompt-toolkit>=3.0.8', 'PyMySQL>=0.10.1']
)
