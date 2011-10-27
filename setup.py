import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyad",
    version = "0.4.9",
    author = "Zakir Durumeric",
    author_email = "zakird@gmail.com",
    maintainer = "Zakir Durumeric",
    maintainer_email = "zakird@gmail.com",
    url = "https://github.com/zakird/pyad",
    description = "A pure Python Object-Oriented Active Directory management framework built on ADSI through pywin32.",
    license = "GNUv3",
    keywords = "python microsoft windows active directory AD adsi",
    packages=[
        'pyad'
    ],
    long_description = read('README'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Operating System :: Microsoft :: Windows",
        "Topic :: System :: Systems Administration :: Authentication/Directory :: LDAP"
    ],
    install_requires=[
        'setuptools',
        'pywin32'
    ]
)