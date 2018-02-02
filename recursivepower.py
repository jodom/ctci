import unittest

def recursivePower(a, b):
	''' compute pow(a,b) recursively '''
	while b > 0:
		return a*recursivePower(a, b-1)
	return 1

class TestRecPow(unittest.TestCase):
	def test_recurse(self):
		self.assertEqual(recursivePower(1,1), 1)
		self.assertEqual(recursivePower(1,100), 1)
		self.assertEqual(recursivePower(2,1), 2)
		self.assertEqual(recursivePower(2,2), 4)
		self.assertEqual(recursivePower(2,3), 8)

if __name__ == '__main__':
	unittest.main()