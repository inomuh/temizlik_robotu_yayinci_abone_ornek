#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

d = generate_distutils_setup(
   packages=['temizlik_robotu_yayinci_ornek'],
   package_dir={'': 'src'}
)

setup(**d)
