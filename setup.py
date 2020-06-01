# -*- coding: utf-8 -*-

import os
from os import path

from setuptools import setup, find_packages
from shutil import copy2

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup_args = {
    'name': 'ndx-hierarchical-behavioral-data',
    'version': '0.1.0',
    'description': 'NWB extensions for organizing hierarchical behavioral data',
    'author': 'Ben Dichter, Armin Najarpour Foroushani',
    'author_email': 'ben.dichter@catalystneuro.com',
    'url': 'https://github.com/Armin12/ndx-hierarchical-behavioral-data',
    'license': 'BSD 3-Clause',
    'long_description': long_description,
    'long_description_content_type': "text/markdown",
    'install_requires': [
        'pynwb>=1.1.2'
    ],
    'packages': find_packages('src/pynwb'),
    'package_dir': {'': 'src/pynwb'},
    'package_data': {'ndx-hierarchical-behavioral-data': [
        'spec/ndx-hierarchical-behavioral-data.namespace.yaml',
        'spec/ndx-hierarchical-behavioral-data.extensions.yaml',
    ]},
    'classifiers': [
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    'zip_safe': False
}


def _copy_spec_files(project_dir):
    ns_path = os.path.join(project_dir, 'spec', 'ndx-hierarchical-behavioral-data.namespace.yaml')
    ext_path = os.path.join(project_dir, 'spec', 'ndx-hierarchical-behavioral-data.extensions.yaml')

    dst_dir = os.path.join(project_dir, 'src', 'pynwb', 'ndx-hierarchical-behavioral-data', 'spec')
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)

    copy2(ns_path, dst_dir)
    copy2(ext_path, dst_dir)


if __name__ == '__main__':
    _copy_spec_files(os.path.dirname(__file__))
    setup(**setup_args)