import unittest

def number_digits(n):
  if n == 0:
    return 1
  if n < 0:
    return number_digits(-n)
  digits = 0
  while n != 0:
    digits += 1
    n //= 10
  return digits

def triangle(n):
  return n * (n+1) // 2

def square(n):
  return n * n

def pentagonal(n):
  return n * (3*n-1) // 2

def hexagonal(n):
  return n * (2*n-1)

def heptagonal(n):
  return n * (5*n-3) // 2

def octagonal(n):
  return n * (3*n-2)

class NumberTest(unittest.TestCase):

  def test_number_digits(self):
    self.assertEqual(number_digits(1), 1)
    self.assertEqual(number_digits(9), 1)
    self.assertEqual(number_digits(10), 2)
    self.assertEqual(number_digits(15), 2)
    self.assertEqual(number_digits(19), 2)
    self.assertEqual(number_digits(1234567890123), 13)
    self.assertEqual(number_digits(-1), 1)
    self.assertEqual(number_digits(-9), 1)
    self.assertEqual(number_digits(-15), 2)
    self.assertEqual(number_digits(0), 1)

  def test_triangle(self):
    self.assertEqual(triangle(1), 1)
    self.assertEqual(triangle(2), 3)
    self.assertEqual(triangle(3), 6)
    self.assertEqual(triangle(4), 10)
    self.assertEqual(triangle(5), 15)
    
  def test_square(self):
    self.assertEqual(square(1), 1)
    self.assertEqual(square(2), 4)
    self.assertEqual(square(3), 9)
    self.assertEqual(square(4), 16)
    self.assertEqual(square(5), 25)

  def test_pentagonal(self):
    self.assertEqual(pentagonal(1), 1)
    self.assertEqual(pentagonal(2), 5)
    self.assertEqual(pentagonal(3), 12)
    self.assertEqual(pentagonal(4), 22)
    self.assertEqual(pentagonal(5), 35)

  def test_hexagonal(self):
    self.assertEqual(hexagonal(1), 1)
    self.assertEqual(hexagonal(2), 6)
    self.assertEqual(hexagonal(3), 15)
    self.assertEqual(hexagonal(4), 28)
    self.assertEqual(hexagonal(5), 45)

  def test_heptagonal(self):
    self.assertEqual(heptagonal(1), 1)
    self.assertEqual(heptagonal(2), 7)
    self.assertEqual(heptagonal(3), 18)
    self.assertEqual(heptagonal(4), 34)
    self.assertEqual(heptagonal(5), 55)

  def test_octagonal(self):
    self.assertEqual(octagonal(1), 1)
    self.assertEqual(octagonal(2), 8)
    self.assertEqual(octagonal(3), 21)
    self.assertEqual(octagonal(4), 40)
    self.assertEqual(octagonal(5), 65)

if __name__ == '__main__':
  unittest.main()
