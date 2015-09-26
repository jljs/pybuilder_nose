#!/usr/bin/env python
import sys
sys.path.insert(0, 'src/main/python')

from pybuilder_nose.tasks import run_unit_tests, clean_coverage
from pybuilder.core import Author, init, use_plugin


use_plugin('python.core')
use_plugin('python.distutils')
use_plugin('python.install_dependencies')

name = 'pybuilder_nose'
version = '0.0.1'

authors = [Author('Alex Dowgailenko','adow@psikon.com')]
url = 'https://github.com/alex-dow/pybuilder_nose'
description = 'Pybuilder plugin to work with Nose'
license = 'Apache License, Version 2.0'
summary = 'PyBuilder Nose Plugin'

default_task = ['clean', 'install_dependencies', 'publish']
#default_task = ['clean', 'install_dependencies', 'analyze', 'publish']

@init
def set_properties(project):
  project.set_property('flake8_verbose_output', True)

  project.get_property('distutils_commands').append('bdist_wheel')
  project.set_property('distutils_classifiers', [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7'
  ])

  project.build_depends_on_requirements('dev-requirements.txt')

  
