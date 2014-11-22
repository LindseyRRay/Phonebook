#Test hash table
from hash import HashTable
import unittest

class test_hash(unittest.TestCase):

	def setUp(self):
		self.hash = HashTable(11)

	def test_put(self):
		self.hash.put("Lindsey Raymond", "9786217554")
		self.assertEqual(self.hash.keys[3], "Lindsey Raymond")
		self.assertEqual(self.hash.data[3], "9786217554")

	def test_get(self):
		self.assertEqual(self.hash.get("Lindsey Raymond"), "9786217554")

	def test_size(self):
		self.assertEqual(self.hash.length, 11)

	def test_get(self):
		self.hash["James Hayward"] = "123456789"
		self.hash.put("Lindsey Raymond", "9786217554")
		self.assertEqual(self.hash["Lindsey Raymond"], self.hash.get("Lindsey Raymond"))
		self.assertEqual(self.hash["James Hayward"], "123456789")

if __name__ == '__main__':
	unittest.main()
