"""
This module defines the base framework defines the `BaseUnitTest` class,
a reusable test foundation built on top of Python's `unittest` framework.
It standardizes test structure, lifecycle management, and assertion behavior
across multiple test suites.
"""
import unittest

class CustomAssertionsMixin:
    """
    A mixin class that provides additional custom assertion methods to extend
    the capabilities of standard unit test cases.
    """
    pass

class BaseUnitTest(unittest.TestCase, CustomAssertionsMixin):
    """
    A reusable base class for writing unit tests, extending Python's
    buit-in unittest framework with custom assertion methods.

    This class provides a bunch of hooks that are automatically invoked
    before and after each test case or once per test suite.

    Notes
    -----
    These hooks can be overriden to customize setup and teardown logic.

    .. _docs:
        https://docs.python.org/3/library/unittest.html
    """
    @classmethod
    def setUp(cls):
        """
        Set up the environment before running each test method.
        """
        pass

    @classmethod
    def tearDown(cls):
        """
        Tear down the environment after running each test method.
        """
        pass

    @classmethod
    def setUpClass(cls):
        """
        Set up the environment before any tests in the class are executed.
        """
        pass

    @classmethod
    def tearDownClass(cls):
        """
        Tear down the environment after all tests in the class are executed.
        """
        pass
