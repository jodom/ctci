import unittest
from linkedlist import LinkedList

class Solution:
	def _sum(self, first, second):
		""" helper: add the sum of two nodes and store in a linked list """
		nodesum = first.value + second.value
		if nodesum > 9:
			result.append(nodesum % 10)
		else:
			result.append(nodesum)
		carry = nodesum // 10

	def addTwoNums(self, firstList, secondList):
		if any(not isinstance(inp, LinkedList) for inp in [firstList, secondList]):
			raise Exception('Invalid input')
		else:
			n1 = firstList.head
			n2 = secondList.head

			if not n1.value or not n2.value:
				raise Exception('Invalid input')
			else:
				result = LinkedList()
				carry = 0
				flag = True

				while flag:
					while n1 and n2:
						self._sum(n1, n2)
						n1, n2 = n1.next, n2.next

					while n1:
						self._sum(n1, carry)
						n1 = n1.next

					while n2:
						self._sum(n2, carry)
						n2 = n2.next

					if carry:
						result.append(carry)
						carry = 0

					flag = False

				return result


class TestAddTwoLL(unittest.TestCase):
	soln = Solution()

	def addToList(self, lst, linkedList):
		for x in lst:
			linkedList.append(x)
		return linkedList

	def test_invalid_input(self):
		with self.assertRaisesRegex(Exception, 'Invalid input'):
			self.soln.addTwoNums([1,2,3], '1234')

	def test_add_equal_lengths(self):
		first = second = expect = LinkedList()
		first = self.addToList([2,4,3], first)
		second = self.addToList([5,6,4], second)
		expect = self.addToList([7,0,8], expect)

		self.assertEqual(self.soln.addTwoNums(first, second), expect)

	def test_add_different_lengths(self):
		first = second = expect = LinkedList()
		first = self.addToList([2,4,3], first)
		second = self.addToList([5], second)
		expect = self.addToList([7,4,3], expect)

		self.assertEqual(self.soln.addTwoNums(first, second), expect)

	def test_lists_with_end_overflows(self):
		first = second = expect = LinkedList()
		first = self.addToList([2,4,3], first)
		second = self.addToList([5,3,7], second)
		expect = self.addToList([7,7,0,1], expect)

		self.assertEqual(self.soln.addTwoNums(first, second), expect)

if __name__ == '__main__':
	unittest.main()
