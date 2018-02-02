import unittest

class Solution:
	def convert(self, s, r):
		"""
		Convert a string s to its zigzag form
		:type s: str
		:type r: int
		:rtype: str
		"""
		if not isinstance (s, str) or not isinstance(r, int):
			raise Exception('Invalid input')
		elif r <= 1 or r >= len(s):
			return s
		else:
			zig = [''] * r

			index, step = 0, 1

			for c in s:
				zig[index] += c
				if index == 0:
					step = 1
				elif index == r - 1:
					step = -1
				index += step

			return ''.join(zig)

class TestZig(unittest.TestCase):
	soln = Solution()
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.convert(12345, 3)
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.convert(['12345'], 3)
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.convert('12345', '3')

	def test_trivial_zigs(self):
		self.assertEqual(self.soln.convert('J', 1), 'J')
		self.assertEqual(self.soln.convert('J', 5), 'J')
		self.assertEqual(self.soln.convert('JK', 1), 'JK')
		self.assertEqual(self.soln.convert('JK', 2), 'JK')

	def test_odd_rows_of_zig(self):
		self.assertEqual(self.soln.convert('JODOMK', 3), 'JMOOKD')
		self.assertEqual(self.soln.convert('JODOMK', 5), 'JODOKM')

	def test_even_rows_of_zig(self):
		self.assertEqual(self.soln.convert('JODOMK', 2), 'JDMOOK')
		self.assertEqual(self.soln.convert('JODOMK', 4), 'JOKDMO')

	def test_spaced_zig(self):
		self.assertEqual(self.soln.convert('JODOM KONUKO', 3), 'JMNOO OUODKK')

if __name__ == '__main__':
	unittest.main()
