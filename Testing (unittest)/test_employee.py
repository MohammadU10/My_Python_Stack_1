import unittest
from employee_class import Employee
import datetime


class TestEmployee(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		print('setupClass')

	@classmethod
	def tearDownClass(cls):
		print('teardownClass')
		print("Raise Amount:", Employee.raise_amt)

	def setUp(self):
		self.emp_1 = Employee('Corey', 'Schafer', 40000)
		self.emp_2 = Employee('Tom', 'Smith', 70000)

	def tearDown(self):
		pass

	# Test (1) - email property
	def test_email(self):
		self.assertEqual(self.emp_1.email, 'Corey.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Tom.Smith@email.com')

		self.emp_1.first = "John"
		self.emp_2.first = "Bob"

		self.assertEqual(self.emp_1.email, 'John.Schafer@email.com')
		self.assertEqual(self.emp_2.email, 'Bob.Smith@email.com')

	# Test (2) - fullname property
	def test_fullname(self):
		self.assertEqual(self.emp_1.fullname, 'Corey Schafer')
		self.assertEqual(self.emp_2.fullname, 'Tom Smith')

		self.emp_1.first = "John"
		self.emp_2.first = "Bob"

		self.assertEqual(self.emp_1.fullname, 'John Schafer')
		self.assertEqual(self.emp_2.fullname, 'Bob Smith')

	# Test (3) - apply_raise method
	def test_apply_raise(self):
		self.emp_1.apply_raise()
		self.emp_2.apply_raise()

		self.assertEqual(self.emp_1.pay, 42000)
		self.assertEqual(self.emp_2.pay, 73500)

	# Test (4) - set raise amount Class method
	def test_set_raise_amt(self):
		self.assertEqual(Employee.raise_amt, 1.05)

		Employee.set_raise_amt(1.10)

		self.assertEqual(Employee.raise_amt, 1.10)

	# Test (5) - from_string (string splitter) Class method
	def test_from_string(self):
		self.emp_1 = Employee.from_string("John-Doe-50000")
		self.assertEqual(self.emp_1.first, "John")
		self.assertEqual(self.emp_1.last, "Doe")
		self.assertEqual(self.emp_1.pay, "50000")

	# Test (6) - is_workday (is the given date workday? checker) Static method
	def test_is_workday(self):
		self.my_date1 = datetime.date(2016, 7, 10)
		self.my_date2 = datetime.date(2016, 7, 11)

		self.assertEqual(Employee.is_workday(self.my_date1), False)
		self.assertEqual(Employee.is_workday(self.my_date2), True)


if __name__ == '__main__':
	unittest.main()
