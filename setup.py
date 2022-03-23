from setuptools import setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
  name = "encodeci",
  version = "0.0.1",
  description = "A Python (cipher) encoder and decoder module",
  long_description = long_description,
  long_description_content_type = "text/markdown",
  url = "https://github.com/kokonut27/encodeci",
  author = "kokonut27",
  author_email = "beol0127@gmail.com",
#To find more licenses or classifiers go to: https://pypi.org/classifiers/
  license = "MIT License",
  packages=['encodeci'],
  classifiers = [
  "Programming Language :: Python :: 3.6",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
],
  zip_safe=False,
  python_requires = ">=3.6",
)