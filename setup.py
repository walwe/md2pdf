#!/usr/bin/env python
from setuptools import setup, find_packages
from pkg_resources import get_distribution

with open("README.md", "r") as f:
    long_description = f.read()

setup(name='md2pdf',
      version='0.0.4',
      description='Markdown to PDF converter',
      url='https://github.com/walwe/md2pdf',
      packages=find_packages(),
      include_package_data=True,
      author='walwe',
      license='MIT License',
      entry_points='''
        [console_scripts]
        md2pdf=md2pdf.cli:cli
      ''',
      install_requires=[
            'markdown2',
            'click'
      ],
      python_requires='>=3.6',
      long_description_content_type="text/markdown",
      long_description=long_description,
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ]
      )
