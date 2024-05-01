"""
This is an example of Google style.

Args:

Returns:


"""
from ._version import __version__


def test_print_in_src():
    """
    This is an example of Google style.

    Args:

    Returns:


    """

    try:
        print("version", __version__)
    except ValueError as ve:
        print("here except", ve)

    print("debug_basic_sanity.setup_class")
