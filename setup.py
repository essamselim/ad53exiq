from distutils.core import setup
from setuptools import find_packages

setup(name='ad53exiq',
      version='0.1',
      author='DSSS',
      author_email='essameldin.selim@gmail.com',
      packages=find_packages(),
      install_requires=['numpy', 'Pillow', 'ipywidgets'])
