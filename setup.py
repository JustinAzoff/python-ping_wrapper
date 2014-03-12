from setuptools import setup, find_packages
import sys, os

version = '0.5'

setup(name='ping_wrapper',
      version=version,
      description="Ping Wrapper",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='ping',
      author='Justin Azoff',
      author_email='justin@bouncybouncy.net',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
