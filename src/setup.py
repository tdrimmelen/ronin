from setuptools import setup

setup(
   name='ronincontroller',
   version='1.0',
   description='A useful module',
   author='Man Foo',
   author_email='foomail@foo.example',
   packages=['ronincontroller'],  #same as name
   install_requires=['serial'], #external packages as dependencies
)