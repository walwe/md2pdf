from setuptools import setup, find_packages
from md2pdf import version

__version__ = version

setup(name='md2pdf',
      version=__version__,
      description='Markdown to PDF converter',
      url='',
      packages=find_packages(),
      include_package_data=True,
      author='walwe',
      license='MIT License'
      )
