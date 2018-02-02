import unittest

class 
def withinRange(num):
	""" check a numbe ris within the 32-bit signed integer range """
	return -2147483648 <= num <= 2147483647

def reverseInt(num):
	""" reverse a 32-bit signed integer, returning a zero in case of overflow """
	if not isinstance(num, int):
		raise Exception('Invalid input')
	elif -10 < num < 10:
		return num
	else:
		cp = abs(num)

		reverse = 0
		while cp > 0:
			reverse *= 10
			reverse += cp%10
			cp //= 10

		if num < 0:
			reverse *= -1

		if withinRange(reverse):
			return reverse
		return 0

class TestModule(unittest.TestCase):

	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			reverseInt('abcd')
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			reverseInt(-1235.9903)

	def test_single_digit_input(self):
		self.assertEqual(reverseInt(5), 5)
		self.assertEqual(reverseInt(-5), -5)

	def test_already_palindrome_ints(self):
		self.assertEqual(reverseInt(33), 33)
		self.assertEqual(reverseInt(-33), -33)

	def test_overflow_cases(self):
		self.assertEqual(reverseInt(2147483647), 0)
		self.assertEqual(reverseInt(-2147483648), 0)

if __name__ == '__main__':
	unittest.main()
