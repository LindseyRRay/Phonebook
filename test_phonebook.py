#test phonebook class
import unittest
from phonebook import Phonebook

class TestPhonebook(unittest.TestCase):

	def setUp(self):
		self.new = Phonebook()

	def test_create(self):
		self.new.create()
		self.assertEqual(self.new.create_flag, True)

	def test_add(self):
		self.new.add("James Ray", "123456789")
		self.new.add("Laura Rose", "23456")
		self.new.add("Ambulance", "911")

		self.assertEqual(len(set(self.new.database.hashkeys)), 4)
		self.assertEqual(self.new.database["Laura Rose"], "23456")

	def test_remove(self):
		self.new.create()
		self.new.add("James Ray", "123456789")
		self.new.add("Laura Rose", "23456")
		self.new.add("Ambulance", "911")
		self.new.remove("James Ray")
		self.assertRaises(KeyError)

	def test_change(self):
		self.new.create()
		self.new.add("James Ray", "123456789")
		self.new.add("Laura Rose", "23456")
		self.new.add("Ambulance", "911")
		self.new.change("Laura Rose", "9999999")
		self.assertEqual(self.new.database["Laura Rose"], "9999999")

	def test_lookup(self):
		self.new.create()
		self.new.add("Laura Rose", "23456")
		self.assertEqual(self.new.lookup("Laura Rose"), "23456")

	def test_reverse_lookup(self):
		self.new.create()
		self.new.add("Laura Rose", "23456")
		self.assertEqual(self.new.reverse_lookup("23456"), "Laura Rose")

	def test_save(self):
		self.new.create()
		self.new.add("James Ray", "123456789")
		self.new.add("Laura Rose", "23456")
		self.new.add("Ambulance", "911")
		self.new.save()
		self.new2 = Phonebook()
		self.assertEqual(self.new.reverse_lookup("23456"), "Laura Rose")

if __name__ == '__main__':
	unittest.main()