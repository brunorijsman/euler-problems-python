import problem001
import problem002
import unittest

class EulerTest(unittest.TestCase):

    def test_problem001(self):
        self.assertEqual(problem001.solve(), 233168)

    def test_problem002(self):
        self.assertEqual(problem002.solve(), 4613732)

unittest.main()

