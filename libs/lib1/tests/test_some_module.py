import unittest
from lib1.some_module import some_function

class TestSomeModule(unittest.TestCase):
    def test_some_function(self):
        result= some_function()
        # assertions to verify the function's behavior
        self.assertEqual(result, "Hello from lib1's some_function!")