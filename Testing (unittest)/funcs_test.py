import unittest
import hellofuncs

class TestFuncs(unittest.TestCase):
	# Test (1)
	def test_hello1(self):
		self.assertEqual(hellofuncs.hello_func1(), 'Hello Function.')

	# Test (2)
	def test_hello2(self):
		self.assertEqual(hellofuncs.hello_func2('Hallo'), 'Hallo Function.')

	# Test (3)
	def test_hello3(self):
		self.assertRaises(ValueError, hellofuncs.hello_func2, '123456789012345678901')

	# Test (4)
	def test_hello4(self):
		with self.assertRaises(ValueError):
			hellofuncs.hello_func2('123456789012345678901')


if __name__ == '__main__':
	unittest.main()

