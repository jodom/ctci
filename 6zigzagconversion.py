import unittest

class Solution:
	def convert(self, s, r):
		""" convert a string s to its zigzag form """
		if not isinstance(s, str) or not isinstance(r, int):
			raise Exception('Invalid input')
		else:
			n = len(s)
			if n < 3 or r < 2:
				return s
			else:
				rows = []
				for i in range(r):
					rows.append([])

				mid = (r-1)//2 if r%2 == 0 else r//2
				i = 0

				while i < n:
					for row in rows:
						row.append(s[i])
						i += 1
						if i >= n:
							break
					if i < n:
						rows[mid].append(s[i])
						i += 1

				zig = []
				for row in rows:
					zig += row

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
		self.assertEqual(self.soln.convert('JODOMK', 5), 'JODKOM')

	def test_even_rows_of_zig(self):
		self.assertEqual(self.soln.convert('JODOMK', 2), 'JDOKOM')
		self.assertEqual(self.soln.convert('JODOMK', 4), 'JKOMDO')

	def test_spaced_zig(self):
		self.assertEqual(self.soln.convert('JODOM KONUKO', 3), 'JMNOO OUODKK')

if __name__ == '__main__':
	unittest.main()
