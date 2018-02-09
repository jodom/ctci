import unittest

class Solution:
	""" 
		Optimised solution, only reverse half the number :
		checkout : https://leetcode.com/articles/palindrome-number/

		O(log10n) time complexity
		O(1) space complexity
	"""

	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		if not isinstance(x, int):
			raise Exception('Invalid input')
		elif x < 0 or (x%10 ==0 and x != 0):
			return False
		else:
			reverse = 0
			while x > reverse:
				reverse = reverse*10 + x%10
				x //= 10
			return x == reverse or x == reverse//10


class TestPalindrome(unittest.TestCase):
	soln = Solution()
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.isPalindrome("string")

	def test_single_digit_int(self):
		self.assertTrue(self.soln.isPalindrome(9))
		self.assertFalse(self.soln.isPalindrome(-5))

	def test_palindrome_digit(self):
		self.assertTrue(self.soln.isPalindrome(33))
		self.assertFalse(self.soln.isPalindrome(-33))
		self.assertFalse(self.soln.isPalindrome(331))
		self.assertFalse(self.soln.isPalindrome(-331))

if __name__ == '__main__':
	unittest.main()
