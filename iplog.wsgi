#!/usr/bin/python

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))

# use virtualenv "venv"
activate_this = os.path.join(_HERE, 'venv/bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

# make "iplog" available on PYTHONPATH
sys.path.insert(0, _HERE)

from iplog import app as application
