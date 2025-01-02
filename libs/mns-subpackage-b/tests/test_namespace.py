import unittest
import mynamespace.subpackage_b as sub_b

class TestNamespace(unittest.TestCase):
    def test_namespace(self):
        # test that the namespace module is properly defined
        # self.assertIsNotNone(sub_b)
        self.assertEqual(sub_b.name, "b")