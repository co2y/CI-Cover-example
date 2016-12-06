# coding=utf-8
import os
from setuptools import setup, find_packages
from mmm import __version__, __author__, __email__

with open('requirements.txt', 'r') as f:
    requirements = f.read().splitlines()


ROOT = os.path.abspath(os.path.dirname(__file__))


setup(
    name='mmm',
    version=__version__,
    author=__author__,
    author_email=__email__,
    keywords='mmm',
    description='just for test',
    url='https://github.com/co2y/mmm',
    download_url='https://github.com/co2y/mmm/tarball/master',
    packages=find_packages(),
    package_data={'': ['LICENSES']},
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'mmm = mmm.main:run'
        ]
    },
    license='MIT License',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Other Audience',
        'Natural Language :: Chinese (Traditional)',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
)
