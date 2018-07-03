from setuptools import setup, find_packages, Extension

setup(
  name = 'memPostgres',
  version = '0.0.1',
  author = 'Matheus E. Muller',
  author_email = 'hello@memuller.com',
  license = 'UNLICENSE',
  packages = ['memPostgres', 'memPostgres.models']
)