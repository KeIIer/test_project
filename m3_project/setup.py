from setuptools import setup, find_packages

with open('requirements.txt') as f:
   requirements = f.readlines()

setup(
   name='m3_project',
   version='1.0',
   description='m3 testing project',
   packages=find_packages(),
   install_requires=requirements,
)
