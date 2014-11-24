#Creates hash table for storing phone book information
#names are keys and phone numbers are values
import pdb
#python -m cProfile -sort cumtime programname.py

class HashTable(object):

	def __init__(self, table_size, linear_probing = 3):
		self.table_size = table_size
		#linear probing value
		self.linear_probing = linear_probing
		self.hashkeys = [None]*self.table_size
		self.data = [None]*self.table_size

	def hashfunction(self, key):
		#implements the midsquare method with the ordinal values for chars
		hash_val = sum([ord(char) for char in key])**2
		return hash_val%self.table_size

	def rehash(self, hashvalue):
		return (hashvalue+self.linear_probing)%self.table_size

	def put(self, key, data):
		#Add an item to the hash table
		hashvalue = self.hashfunction(key)

		#check if slot empty
		if self.hashkeys[hashvalue] == None:
			self.hashkeys[hashvalue] = key
			self.data[hashvalue] = data

		else:
		#if key already exits, then replace with new data
			if self.hashkeys[hashvalue] == key:
				self.data[hashvalue] = data
		#if slot already taken by different key, then use a 				
			else:
				nextslot = self.rehash(hashvalue)
				while self.hashkeys[nextslot] != None and self.hashkeys[nextslot] != key:
					nextslot = self.rehash(nextslot)

				self.hashkeys[nextslot] = key
				self.data[nextslot] = data

	def get(self, key):
		hashvalue = self.hashfunction(key)
		#check if key actually exists in data
		if self.hashkeys[hashvalue] == None:
			raise KeyError("Value does not exist")
		while self.hashkeys[hashvalue] != key:
			hashvalue = self.rehash(hashvalue)
			#make sure that searching doesn't occur infinitely 
			#this part shouldn't happen, but might 
			if hashvalue == self.hashfunction(key):
				raise KeyError("Value does not exist")
		return self.data[hashvalue]

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, data):
		return self.put(key, data)

	@property
	def keys(self):
	    return self.hashkeys

	@property 
	def values(self):
		return self.data

	@property 
	def length(self):
		return self.table_size 

	
if __name__ == '__main__':
	test = HashTable(11)





