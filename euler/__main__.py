import problem001
import problem002
import problem088
import unittest

only_fast_tests = False

class EulerTest(unittest.TestCase):

    def test_problem001(self):
        self.assertEqual(problem001.solve(), 233168)

    def test_problem002(self):
        self.assertEqual(problem002.solve(), 4613732)

    def test_problem088(self):
        self.assertEqual(problem088.solve_max_size(6), 30)
        self.assertEqual(problem088.solve_max_size(12), 61)
        if not only_fast_tests:
            self.assertEqual(problem088.solve(), 7587457)

unittest.main()

