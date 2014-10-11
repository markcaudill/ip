import sys
import os
_basedir = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, _basedir)
sys.path.insert(1, '%s/venv/lib64/python2.7/site-packages' % _basedir)
from app import app as application