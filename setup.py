# coding: utf-8
import sys
from setuptools import setup, find_packages


# Backward-compatibility dependencies for Python 2
_python2_requires = [
    'backports.os',
] if sys.version_info < (3,) else []


setup(
    name='backports.test.support',
    description="Backport of Python 3's test.support package",
    url='https://github.com/pjdelport/backports.test.support',

    author=u'Piët Delport',
    author_email='pjdelport@gmail.com',

    package_dir={'': 'src'},
    packages=find_packages('src'),

    setup_requires=['setuptools_scm'],
    use_scm_version=True,

    install_requires=_python2_requires,

    license='Python Software Foundation License',
    classifiers=[
        'Development Status :: 6 - Mature',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Python Software Foundation License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
)
