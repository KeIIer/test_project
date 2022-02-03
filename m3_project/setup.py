from setuptools import setup

with open('requirements.txt') as f:
   requirements = f.readlines()

setup(
   name='m3_project',
   version='1.0',
   description='m3 testing project',
   packages=['m3_project, app'],
   install_requires=requirements,
)
