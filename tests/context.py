"""
This is an example of Google style.

Args:
    param1: This is the first param.
    param2: This is a second param.

Returns:
    This is a description of what is returned.

Raises:
    KeyError: Raises an exception.
"""


import os
import sys
from src.debug_basic_sanity import setup_class

curr_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(curr_dir, "..")))


setup = setup_class
setup.test_print_in_src()
