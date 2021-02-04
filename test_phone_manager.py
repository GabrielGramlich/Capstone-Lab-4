import unittest
from phone_manager import Phone, Employee, PhoneAssignments, PhoneError

class TestPhoneManager(unittest.TestCase):

	def test_create_and_add_new_phone(self):

		testPhone1 = Phone(1, 'Apple', 'iPhone 6')
		testPhone2 = Phone(2, 'Apple', 'iPhone 5')

		testPhones = [ testPhone1, testPhone2 ]

		testAssignmentMgr = PhoneAssignments()
		testAssignmentMgr.add_phone(testPhone1)
		testAssignmentMgr.add_phone(testPhone2)

		# assertCountEqual checks if two lists have the same items, in any order.
		# (Despite what the name implies)
		self.assertCountEqual(testPhones, testAssignmentMgr.phones)


	def test_create_and_add_phone_with_duplicate_id(self):
		testPhone1 = Phone(1, 'Apple', 'iPhone 6')
		testPhone2 = Phone(1, 'Apple', 'iPhone 5')

		testAssignmentMgr = PhoneAssignments()
		testAssignmentMgr.add_phone(testPhone1)

		with self.assertRaises(PhoneError):
			testAssignmentMgr.add_phone(testPhone2)


	def test_create_and_add_new_employee(self):
		test_employee1 = Employee(1,'Human')
		test_employee2 = Employee(2,'Very Real Human')
		test_employee3 = Employee(3,'Zagnork, Conqueror of Worlds')

		test_assignment_manager = PhoneAssignments()

		test_assignment_manager.add_employee(test_employee1)
		test_assignment_manager.add_employee(test_employee2)
		test_assignment_manager.add_employee(test_employee3)

		self.assertIn(test_employee1, test_assignment_manager.employees)
		self.assertIn(test_employee2, test_assignment_manager.employees)
		self.assertIn(test_employee3, test_assignment_manager.employees)


	def test_create_and_add_employee_with_duplicate_id(self):
		test_employee1 = Employee(1,'Colin Jost')
		test_employee2 = Employee(1,'Michael Che')

		test_assignment_manager = PhoneAssignments()
		test_assignment_manager.add_employee(test_employee1)

		with self.assertRaises(PhoneError):
			test_assignment_manager.add_employee(test_employee2)


	def test_assign_phone_to_employee(self):
		test_phone = Phone(1, 'Apple', 'iPhone 420')
		test_employee = Employee(1,'Snoop Dogg')

		test_assignment_manager = PhoneAssignments()
		test_assignment_manager.add_phone(test_phone)
		test_assignment_manager.add_employee(test_employee)

		test_assignment_manager.assign(1,test_employee)

		self.assertEqual(test_employee.id,test_phone.employee_id)


	def test_assign_phone_that_has_already_been_assigned_to_employee(self):
		test_phone = Phone(1, 'Apple', 'iPhone 420')
		test_employee1 = Employee(1,'Snoop Dogg')
		test_employee2 = Employee(2,'Wiz Khalifa')

		test_assignment_manager = PhoneAssignments()
		test_assignment_manager.add_phone(test_phone)
		test_assignment_manager.add_employee(test_employee1)
		test_assignment_manager.add_employee(test_employee2)

		test_assignment_manager.assign(1,test_employee1)

		with self.assertRaises(PhoneError):
			test_assignment_manager.assign(1,test_employee2)


	def test_assign_phone_to_employee_who_already_has_a_phone(self):
		test_phone1 = Phone(1, 'Apple', 'iPhone 420')
		test_phone2 = Phone(2, 'Samsung', 'Galaxy 420')
		test_employee = Employee(1,'Snoop Dogg')

		test_assignment_manager = PhoneAssignments()
		test_assignment_manager.add_phone(test_phone1)
		test_assignment_manager.add_phone(test_phone2)
		test_assignment_manager.add_employee(test_employee)

		test_assignment_manager.assign(1,test_employee)

		with self.assertRaises(PhoneError):
			test_assignment_manager.assign(2,test_employee)


	def test_assign_phone_to_the_employee_who_already_has_this_phone(self):
		test_phone = Phone(1, 'Apple', 'iPhone 420')
		test_employee = Employee(1,'Snoop Dogg')

		test_assignment_manager = PhoneAssignments()
		test_assignment_manager.add_phone(test_phone)
		test_assignment_manager.add_employee(test_employee)

		test_assignment_manager.assign(1,test_employee)
		self.assertEqual(test_employee.id,test_phone.employee_id)
		test_assignment_manager.assign(1,test_employee)
		self.assertEqual(test_employee.id,test_phone.employee_id)


	def test_un_assign_phone(self):
		test_phone = Phone(1, 'Apple', 'iPhone 420')
		test_employee = Employee(1,'Snoop Dogg')

		test_assignment_manager = PhoneAssignments()
		test_assignment_manager.add_phone(test_phone)
		test_assignment_manager.add_employee(test_employee)

		test_assignment_manager.assign(1,test_employee)
		member_assigned = test_phone.employee_id

		self.assertIsNotNone(member_assigned)

		test_assignment_manager.un_assign(1)
		member_assigned = test_phone.employee_id

		self.assertIsNone(member_assigned)


	def test_get_phone_info_for_employee(self):
		# TODO write this test and remove the self.fail() statement
		# Create some phones, and employees, assign a phone,
		# call phone_info and verify correct phone info is returned

		# TODO check that the method returns None if the employee does not have a phone
		# TODO check that the method raises an PhoneError if the employee does not exist

		self.fail()
