import unittest

class Solution:

	def _reverse(self, x):
		reverse = 0
		cp = abs(x)
		while cp > 0:
			reverse = reverse*10 + cp%10
			cp //= 10
		reverse = -1*reverse if x < 0 else reverse
		if -2147483648 <= reverse <= 2147483647:
			return reverse
		return False
			

	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if not isinstance(x, int):
			raise Exception('Invalid input')
		elif -10 < x < 10:
			return True
		else:
			return self._reverse(x) == x


class TestPalindrome(unittest.TestCase):
	soln = Solution()
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.isPalindrome("string")

	def test_single_digit_int(self):
		self.assertTrue(self.soln.isPalindrome(9))
		self.assertTrue(self.soln.isPalindrome(-5))

	def test_palindrome_digit(self):
		self.assertTrue(self.soln.isPalindrome(33))
		self.assertTrue(self.soln.isPalindrome(-33))
		self.assertFalse(self.soln.isPalindrome(331))
		self.assertFalse(self.soln.isPalindrome(-331))

if __name__ == '__main__':
	unittest.main()
