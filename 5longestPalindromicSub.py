import unittest


def longestPalindromicSub(string):
	""" return the longest palindromic substring in a string """
	n = len(string)
	if not isinstance(string, str) or n < 1:
		raise Exception('Invalid input')
	else:
		s = string.lower()
		sr = ''.join(reversed(s))
		if s == sr:
			return string
		else:
			i, j = 1, n-1
			subs = []
			while i < n:
				a = n
				for a in range(n, i, -1):
					if s[i:a] in sr:
						subs.append(s[i:a])
						break
				i += 1		
			print(subs)
			while j > 1:
				b = 0
				for b in range(0, j):
					if s[b:j] in sr:
						subs.append(s[b:j])
						break
				j -= 1
			print(subs)
			return max(subs)
			# while 
			# 	elif s[i:j] in sr and i < j:
			# 		return s[i:j]
			# 	else:
			# 		i, j = i+1, j-1
			# return string[0]


class TestLongestPalSub(unittest.TestCase):
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			longestPalindromicSub('')
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			longestPalindromicSub([])

	def test_with_entire_palindrome(self):
		self.assertEqual(longestPalindromicSub('e'), 'e')
		self.assertEqual(longestPalindromicSub('raceCar'), 'raceCar')

	def test_random_case(self):
		self.assertEqual(longestPalindromicSub('babad'), 'aba')
		self.assertEqual(longestPalindromicSub('autogenerated'), 'ene')

	def test_no_palindrome_in_string(self):
		self.assertEqual(longestPalindromicSub('randomword'), 'r')

if __name__ == '__main__':
	unittest.main()