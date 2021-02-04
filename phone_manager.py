# Manage a list of phones
# And a list of employees

# Each employee gets 0 or 1 phones

class Phone():

	def __init__(self, id, make, model):
		self.id = id
		self.make = make
		self.model = model
		self.employee_id = None


	def assign(self, employee_id):
		self.employee_id = employee_id


	def is_assigned(self):
		return self.employee_id is not None


	def __str__(self):
		return 'ID: {} Make: {} Model: {} Assigned to Employee ID: {}'.format(self.id, self.make, self.model, self.employee_id)



class Employee():

	def __init__(self, id, name):
		self.id = id
		self.name = name


	def __str__(self):
		return 'ID: {} Name {}'.format(self.id, self.name)



class PhoneAssignments():

	def __init__(self):
		self.phones = []
		self.employees = []


	def add_employee(self, employee):
		if id_does_not_exist(employee, self.employees):
			self.employees.append(employee)
		else:
			raise PhoneError


	def add_phone(self, phone):
		if id_does_not_exist(phone, self.phones):
			self.phones.append(phone)
		else:
			raise PhoneError


	def assign(self, phone_id, employee):
		can_assign_phone, phone = can_assign(self.phones, phone_id, employee)
		if can_assign_phone:
			phone.assign(employee.id)


	def un_assign(self, phone_id):
		# Find phone in list, set employee_id to None
		for phone in self.phones:
			if phone.id == phone_id:
				phone.assign(None)   # Assign to None


	def phone_info(self, employee):
		# find phone for employee in phones list

		# TODO  should return None if the employee does not have a phone
		# TODO  the method should raise an exception if the employee does not exist

		for phone in self.phones:
			if phone.employee_id == employee.id:
				return phone


		return None


def id_does_not_exist(phone, phones):
	no_id = True
	for p in phones:
		if phone.id == p.id:
			no_id = False

	return no_id


def can_assign(phones, phone_id, employee):
	phone = find_phone(phones, phone_id)
	available = phone_available(phone, employee)
	has_no_phone = employee_has_phone(phones, employee)

	return available and has_no_phone, phone


def find_phone(phones, phone_id):
	for phone in phones:
		if phone.id == phone_id:
			return phone


def phone_available(phone, employee):
	available = True
	if phone.employee_id == employee.id:
		available = False
	elif phone.is_assigned():
		available = False
		raise PhoneError

	return available


def employee_has_phone(phones, employee):
	has_no_phone = True
	for phone in phones:
		if phone.employee_id == employee.id:
			has_no_phone = False
			raise PhoneError

	return has_no_phone


class PhoneError(Exception):
	pass
