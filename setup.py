from __future__ import print_function

from setuptools import setup
import codecs
import os
import re

here = os.path.abspath(os.path.dirname(__file__))


def read(file_paths, default=""):
    # intentionally *not* adding an encoding option to open
    try:
        return codecs.open(os.path.join(here, *file_paths), 'r').read()
    except:
        return default


def find_version(file_paths):
    version_file = read(file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


description = 'Python client library for Zoom.us REST API'
long_description = read('README.md', default=description)

setup(
    name='zoomus',
    version=find_version(['zoomus', '__init__.py']),
    url='http://github.com/actmd/zoomus/',
    license='Apache Software License',
    author='Patrick R. Schmid',
    install_requires=['requests'],
    author_email='prschmid@act.md',
    description=description,
    long_description=long_description,
    packages=['zoomus', 'zoomus.components'],
    include_package_data=True,
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Internet',
        'Topic :: Office/Business',
        'Topic :: Software Development :: Libraries'
    ]
)