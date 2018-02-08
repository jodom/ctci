import unittest


# check soln @https://github.com/coder-pft/Algorithms-in-Java/commit/479a42fdbbf4303d89beef8df9e270a29580110d

class Solution:

	def area(self, height, i, j):
		return min(height[i],height[j])*(j-i)

	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""
		n = len(height)
		if not isinstance(height, list) or n < 2:
			raise Exception('Invalid input')
		elif n == 2:
			return self.area(height, 0, 1)
		else:
			i, j = 0, n-1
			maxpair = [i, j]
			_max = 0
			while i < j:
				current = self.area(height, i, j)
				_max = current if current > _max else _max
				
				if height[i] < height[j]:
					i += 1
				else:
					j -= 1
			return _max


class TestMaxWater(unittest.TestCase):
	soln = Solution()
	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.maxArea([1])
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.maxArea('abcde')

	def test_single_pair(self):
		self.assertEqual(self.soln.maxArea([3,4]), 3)

	def test_consecutive_pairs(self):
		self.assertEqual(self.soln.maxArea([6,3,5,8,2,1,22,50,2,5]), 22)

if __name__ == '__main__':
	unittest.main()
