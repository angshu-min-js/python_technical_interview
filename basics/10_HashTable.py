"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""

class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hash = self.calculate_hash_value(string)
        if hash != -1:
            if self.table[hash] != None:
                self.table[hash].append(string)
            else:
                self.table[hash] = [string]

    def lookup(self, string):
        hash = self.calculate_hash_value(string)
        if hash != -1:
            if self.table[hash] != None:
                    if string in self.table[hash]:
                        return hash
        return -1

    def calculate_hash_value(self, string):
        value = ord(string[0])*100 + ord(string[1])
        return value

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
