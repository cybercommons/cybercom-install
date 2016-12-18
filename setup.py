#!/usr/bin/env python

from distutils.core import setup

setup(name='cybercomInstall',
      version='1.0',
      description='Cybercommons Installation Utility',
      author='Mark STacy',
      author_email='markstacy@ou.edu',
      url='http://cybercommons.org',
      #packages=['cybercomInstall',],
      entry_points = {
        "console_scripts": ['cybercomInstall = cybercominstall']
        }
     )
