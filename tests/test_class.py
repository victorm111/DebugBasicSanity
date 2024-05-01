# content of test_class.py
# call with pytest -q test_class.py
# when grouping tests inside classes is that each test has a unique
# instance of the class.
# Having each test share the same class instance would be very
# detrimental to
# test isolation and would promote poor test practices.

# Test classes must be named “Test*”


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

# import contexts
# To give the individual tests in the tests folder debug_basic_sanity
# package import context

from .context import setup_class

# Access package code
setup_class.test_print_in_src()


class TestClass:
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

    def test_one(self):
        """
        test for one

        :param str self: instance of the class
        :return: the assertion result
        :rtype: bool
        :raises ValueError: if the assertion fails
        """
        x = "this"
        assert "h" in x

    def test_two(self):
        """
        test for two

        :param str self: instance of the class
        :return: the assertion result
        :rtype: bool
        :raises ValueError: if the assertion fails
        """
        x = "hello"
        assert "h" in x
