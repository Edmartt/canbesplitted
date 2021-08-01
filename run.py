import unittest
from code.backend_algorithm import Splitter

tests = unittest.TestLoader().discover('tests')
unittest.TextTestRunner(verbosity=2).run(tests)
