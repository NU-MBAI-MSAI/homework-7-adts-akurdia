import unittest
from tests import test_bst, test_bst_2

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTests(loader.loadTestsFromModule(test_bst))
suite.addTests(loader.loadTestsFromModule(test_bst_2))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)