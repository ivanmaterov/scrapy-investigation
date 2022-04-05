#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="Ivan Materov",
    author_email='ivan.materov@saritasa.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A small project for scrapy-investigation",
    entry_points={
        'console_scripts': [
            'scrapy_investigation=scrapy_investigation.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='scrapy_investigation',
    name='scrapy_investigation',
    packages=find_packages(include=['scrapy_investigation', 'scrapy_investigation.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ivanmaterov/scrapy_investigation',
    version='0.1.0',
    zip_safe=False,
)
