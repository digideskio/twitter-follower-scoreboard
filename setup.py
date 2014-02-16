from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='twitter-follower-scoreboard',
      version=version,
      description="Generates a scoreboard in JSON format for a designated set of Twitter handles, ranked by follower count",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Sanders Kleinfeld',
      url='',
      license='MIT',
      test_suite='nose.collector',
      packages=find_packages(exclude=["*.test", "*.test.*", "test.*", "test"]),
      scripts=[ 'generate_twitter_scoreboard.py'
              ],
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'pyyaml',
          'twitter',
      ]
      )

