import problem001
import problem002
import problem074
import problem088
import problem092
import unittest

only_fast_tests = True

class EulerTest(unittest.TestCase):

    def test_problem001(self):
        self.assertEqual(problem001.solve(), 233168)

    def test_problem002(self):
        self.assertEqual(problem002.solve(), 4613732)

    def test_problem074(self):
        self.assertEqual(problem074.solve_max(5000), 18)
        if not only_fast_tests:
            self.assertEqual(problem074.solve_max(1000000), 402)

    def test_problem088(self):
        self.assertEqual(problem088.solve_max_size(6), 30)
        self.assertEqual(problem088.solve_max_size(12), 61)
        if not only_fast_tests:
            self.assertEqual(problem088.solve(), 7587457)

    def test_problem092(self):
        self.assertEqual(problem092.solve_max(1000), 857)
        if not only_fast_tests:
            self.assertEqual(problem092.solve(), 8581146)

unittest.main()
