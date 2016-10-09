class Vector:
	 ”””Represent a vector in a multidimensional space.”””

	 def init (self, d):
	 ”””Create d-dimensional vector of zeros.”””
	 self. coords = [0] d

	 def len (self):
	 ”””Return the dimension of the vector.”””
	 return len(self. coords)

	 def getitem (self, j):
	 ”””Return jth coordinate of vector.”””
	 return self. coords[j]

	 def setitem (self, j, val):
	 ”””Set jth coordinate of vector to given value.”””
	 self. coords[j] = val

	 def add (self, other):
	 ”””Return sum of two vectors.”””
	 if len(self) != len(other): # relies on len method
	 raise ValueError( dimensions must agree )
	 result = Vector(len(self)) # start with vector of zeros
	 for j in range(len(self)):
	 result[j] = self[j] + other[j]
	 return result

	 def eq (self, other):
	 ”””Return True if vector has same coordinates as other.”””
	 return self. coords == other. coords

	 def ne (self, other):
	 ”””Return True if vector differs from other.”””
	 return not self == other # rely on existing eq definition

	 def str (self):
	 ”””Produce string representation of vector.”””
	 return < + str(self. coords)[1:-1] + > # adapt list representation