import codecs
import os

from setuptools import find_packages, setup


here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(os.path.join(here, 'requirements.txt')) as f:
    requirements = [line.strip() for line in f.readlines()]

setup(name='pyelf',
      version='0.1',
      description='pyelf is an ELF files reader',
      long_description=long_description,
      url='https://github.com/guilload/pyelf',
      author='Adrien Guillo',
      author_email='adrien@guilload.com',
      license='MIT',
      classifiers=[
                   'Development Status :: 3 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Programming Language :: Python :: 2.6',
                   'Programming Language :: Python :: 2.7',
                   ],
      keywords='ELF',
      platforms=['Cross-platform'],
      install_requires=requirements,
      packages=find_packages(exclude=['tests']),
      scripts=['bin/pyelf'],
      )
