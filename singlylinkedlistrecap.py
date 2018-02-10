import unittest

class SinglyLinkedList:
	class _Node:
		""" Node helper class containing element e """
		def __init__(self, e=None):
			self.element = e
			self.next = None

	def __init__(self, e=None):
		""" initialize a linked list """
		if e and any(isinstance(e, tp) for tp in [int, float]):
			self.head = self._Node(e)
			self.tail = self.head
			self.length = 1
		elif e and any(isinstance(e, tp) for tp in [str, list, tuple]):
			self.head = self._Node(e[0])
			self.tail = self.head
			self.length = 1
			for i in range(1,len(e)):
				self.prependElement(e[i])
		else:
			raise Exception("Initialize list with an element or a sequence")


	def __len__(self):
		if self.head:
			return self.length
		return '0: Empty linked list'

	def appendElement(self, e):
		""" add a new element to the back of the list """
		if self.tail:
			new = self._Node(e)
			self.tail.next = new
			self.tail = new
			self.lenth += 1
		else:
			raise Exception('Empty linked list')

	def prependElement(self, e):
		""" add a new element to the  front of the list """
		if self.head:
			new = self._Node(e)
			new.next = self.head
			self.head = new
			self.length += 1
		else:
			raise Exception('Empty linked list')

	def removeHead(self):
		""" remove and return an element at the front of the list """
		if self.head:
			node = self.head
			self.head = node.next
			self.length -= 1
			if self.length == 0:
				self.tail = None
			return node.element
		else:
			raise Exception('Empty linked list')

	def removeTail(self):
		""" remove and return an element at the back of the list """
		if self.head:
			walk = self.head
			# traverse to one element before the tail
			while walk.next.next:
				walk = walk.next
			node = walk.next
			walk.next = None
			self.tail = walk
			self.length -= 1
			if self.length == 0:
				self.head = None
			return node.element
		else:
			raise Exception('Empty linked list')

	def __str__(self):
		""" generate a string representation of a sll """
		if self.head:
			walk = self.head
			rep = []
			while walk.next:
				rep.extend(str(walk.element), '>')
				walk = walk.next
			return ''.join(rep)
		raise Exception('Empty linked list')

class TestSLL(unittest.TestCase):
	def test_create_sll(self):
		with self.assertRaisesRegex(Exception, "Initialize list with an element or a sequence"):
			SinglyLinkedList()

	def test_initialize_with_digit(self):
		lst = SinglyLinkedList(10)
		self.assertTrue(lst)
		self.assertEqual(len(lst), 1)
		self.assertEqual(lst.head.element, 10)
		self.assertEqual(lst.tail.element, 10)

		lst = SinglyLinkedList(10.0)
		self.assertTrue(lst)
		self.assertEqual(len(lst), 1)
		self.assertEqual(lst.head.element, 10.0)
		self.assertEqual(lst.tail.element, 10.0)

	def test_initialize_with_sequence(self):
		lst = SinglyLinkedList('jodom')
		self.assertEqual(len(lst), 5)
		self.assertEqual(lst.head.element, 'm')
		self.assertEqual(lst.tail.element, 'j')

		lst2 = SinglyLinkedList([1,2,3,4,5])
		self.assertEqual(len(lst2), 5)
		self.assertEqual(lst2.head.element, 5)
		self.assertEqual(lst2.tail.element, 1)

		lst3 = SinglyLinkedList(('1','2','3','4','5'))
		self.assertEqual(len(lst3), 5)
		self.assertEqual(lst3.head.element, '5')
		self.assertEqual(lst3.tail.element, '1')

	def test_string_representation(self):
		pass


if __name__ == '__main__':
	unittest.main()
