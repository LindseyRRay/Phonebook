from hash import HashTable
from csv import reader
import sys
import pdb



class Phonebook:

	def __init__(self):
		#connect to permanent storage
		self.create_flag = False
		self.delimiter = '|'
		self.storage = "permanent_data.txt"
		self.database = HashTable(5479)
		#call function to read existing data into hash table
		self._import_data()
	

	def _read_lines(self):
		with open(self.storage, 'r') as old_data:
			for row in old_data:
				if not row.startswith("#"):
					yield row

	def _import_data(self):
		for row in self._read_lines():
			if row.startswith("~"):
				self.create()
			else:
				name = row.split(self.delimiter)[0]
				number = row.split(self.delimiter)[-1]
				self.database[name] = number

	def add(self, name, number):
		#print(self.database.hashkeys)
		if name not in set(self.database.hashkeys):
			self.database[name] = number
		else:
			raise KeyError("Value already exists")


	def remove(self, name):
		self.database.put(name, None)
		self.database.hashkeys[self.database.hashkeys.index(name)] = None

	def change(self, name, number):
		if name in set(self.database.hashkeys):
			self.database[name] = number
		else:
			raise KeyError("Value does not exist")

	def lookup(self, name):
		try:
			return self.database[name]
		except:
			raise KeyError("Value does not exist")

	def reverse_lookup(self, number):
		#Note that this will be slow
		try:
			location = self.database.data.index(number)
			return self.database.hashkeys[location]
		except:
			raise LookupError("Value does not exist")

	def create(self):
		self.create_flag = True

	def save(self):
		with open(self.storage, 'w') as txt_file:
			txt_file.write("#permanent storage file\n")
			if self.create_flag:
				txt_file.write("~CREATED\n")
			for name in self.database.keys:
				if name != None:
					txt_file.write(name+"|"+self.database[name]+"\n")


	def check_input_errors(self, args):
		if len(args) == 1:
			raise RuntimeError("Need more input")


	def parse_arguments(self, args):
		self.check_input_errors(args)
		if self.create_flag:
			if args[1] == "add":
				self.add(*args[2:4])
			else:
				result = getattr(self, args[1])(args[2])
		else:
			if args[1] == 'create':
				self.create()
			else:
				raise RuntimeError("Phonebook does not exist")
		self.save()
		return result

if __name__ == '__main__':
	args = sys.argv[:]
	print(args)
	userPhone = Phonebook()
	res = userPhone.parse_arguments(args)
	print(res)
