from setuptools import setup, find_packages
import sys, os


setup(name='elspecSetup',
      version='2.0.0',
      description="Setup for Elspec Automation",
      long_description="""\
Libraries needed for automation""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='elspec',
      author='Elspec Automation',
      author_email='nissimd@elspec-ltd.com',
      url='https://github.com/ElspecAuto/elspecsetup',
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
