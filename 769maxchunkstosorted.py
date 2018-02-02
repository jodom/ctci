import unittest

class Solution:
	# helper functions
	def sortedUp(self, arr):
		""" check if an array is sorted in an incresing order """
		i, j = 0, 1
		n = len(arr)
		while j < n:
			if arr[j] < arr[i]:
				return False
			else:
				i, j = j, j+1
		return True

	def sortedDown(self, arr):
		""" check if an array is sorted in a  decreasing order """
		i, j = 0, 1
		n = len(arr)
		while j < n:
			if arr[j] > arr[i]:
				return False
			else:
				i, j = j, j+1
		return True

	def join(self, arr1, arr2):
		""" merge two arrays into a sorted array """
		joined = []
		m, n = len(arr1), len(arr2)
		i, j = 0, 0
		while i+j < m+n:
			if i < m and (arr1[i] < arr2[j] or j >= n):
				joined.append(arr1[i])
				i += 1
			else:
				joined.append(arr2[j])
				j += 1
		return joined

	def split(self, arr):
		""" chunk an unsorted arraay """
		n = len(arr)
		i, j = 0, 1
		chunks = []
		while j < n:
			if arr[j] < arr[j-1]:
				chunks.append(arr[i:j+1])
				i, j = j+1, j+2
			else:
				j += 1
		chunks.append(arr[i: j])
		return chunks


	def maxChunksToSorted(self, arr):
		"""
		:type arr: List[int]
		:rtype: int
		"""
		pass

class TestSolution(unittest.TestCase):`
	soln = Solution()
	arr1 = [0,1,2,3,4]
	arr2 = [9,8,7,6,5]

	def test_sorted_up_helper(self):
		self.assertTrue(self.soln.sortedUp(self.arr1))
		self.assertFalse(self.soln.sortedUp(self.arr2))


	def test_sorted_down_helper(self):
		self.assertTrue(self.soln.sortedDown(self.arr2))
		self.assertFalse(self.soln.sortedDown(self.arr1))

	def test_join_helper(self):
		expected = [0,1,2,3,4,9,8,7,6,5]
		self.assertEqual(self.soln.join(self.arr1, self.arr2), expected)

	def test_split(self):
		expected = [[0,1,2,3,4,9, 8],[7,6],[5]]
		self.assertEqual(self.soln.split([0,1,2,3,4,9,8,7,6,5]), expected)

if __name__ == '__main__':
	unittest.main()
