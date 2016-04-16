import unittest
import hello as sut


@unittest.skip("Don't forget to test!")
class HelloTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.hello_example()
        self.assertEqual("Happy Hacking", result)
