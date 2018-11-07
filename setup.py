# -*- coding: utf-8 -*-

from distutils.core import setup
from setuptools import find_packages

setup(
      name='pyalog',
      version='0',
      description="Give a desktop interface to your interactive scripts",
      long_description=open('README.md').read(),
      keywords='desktop dialog',
      author='David PG',
      author_email='davidpg@protonmail.com',
      url='https://github.com/devopsysadmin/pyalog',
      license='GPL v3',
      packages=find_packages(exclude=['test']),
      entry_points={
          'console_scripts': [
             'pyalog = cmdline:main',
          ],
      },
      include_package_data=True,
      zip_safe=False,
      install_requires=[line for line in open('requirements.txt')],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities'
      ]
)