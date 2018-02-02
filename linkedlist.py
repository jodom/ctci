import unittest

class LinkedList:
	class _ListNode:
		""" helper node class """
		def __init__(self, x):
			self.value = x
			self.next = None

	def __init__(self, value=None):
		self.head = self._ListNode(value)
		self.tail = self.head

	def append(self, x):
		if not self.head:
			self.head.value = x
		else:
			self.tail.next = self._ListNode(x)


class TestMakeshiftList(unittest.TestCase):
	def test_create_a_list(self):
		lst = LinkedList()
		self.assertTrue(lst)
		self.assertEqual(lst.head.value, None)

		lst2 = LinkedList(1)
		self.assertEqual(lst2.head.value, 1)

if __name__ == '__main__':
	unittest.main()
