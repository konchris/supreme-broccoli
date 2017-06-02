#!/usr/bin/env python
# coding: utf-8

from cx_Freeze import setup, Executable

buildOptions = dict(packages=[], excludes=[])

base = 'Console'

executables = [
    Executable('supreme_broccoli/cli_test.py', base=base)
]


def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='Supreme Broccoli',
    version="0.1.0",
    description='Test creating cross-platform standalone executables in' +
                'Python 3.5',
    options=dict(build_exe=buildOptions),
    executables=executables,

    long_description=readme(),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
        'Topic :: Text Processing :: Linguistic',
    ],

    keywords='hello world test console command line',
    url='https://github.com/konchris/guitest/',
    author='Christopher Espy',
    author_email='github@konchris.de',
    license='GPLv3',
    packages=['supreme_broccoli'],
    ## install_requires=[
    ##     '',
    ##     ],

    ## test_suite='tests.test_cli_test',
    ## tests_require=['pytest', 'pytest-cov'],
    ## entry_points={
    ##     'console_scripts': ['cli-test=supreme_broccoli.cli_test:main'],
    ##     },
    ## include_package_data=True,
    ## zip_safe=False,
)
