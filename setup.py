#!/usr/bin/python3
# coding: utf-8

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ProtonMail',
    version='0.1',
    description='ProtonMail client',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords="protonmail proton mail encryption",
    license="GPLv3",
    author='ShellCode',
    author_email='shellcode33@protonmail.ch',
    url='https://github.com/ShellCode33/ProtonMail',
    packages=find_packages(),
    python_requires='>=3.6',

    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
    ],

    install_requires=[],

    entry_points={
        "console_scripts": [
            "protonmail = protonmail.cli:main",
        ]
    }
)
