 class Range:
	 ”””A class that mimic s the built-in range class.”””

	 def init (self, start, stop=None, step=1):
	 ”””Initialize a Range instance.

	 Semantics is similar to built-in range class.
	 ”””
	 if step == 0:
	 raise ValueError( step cannot be 0 )

	 if stop is None: # special case of range(n)
	 start, stop = 0, start # should be treated as if range(0,n)

	 # calculate the effective length once
	 self. length = max(0, (stop - start + step - 1) // step)

	 # need knowledge of start and step (but not stop) to support getitem
	 self. start = start
	 self. step = step

	 def len (self):
	 ”””Return number of entries in the range.”””
	 return self. length

	 def getitem (self, k):
	 ”””Return entry at index k (using standard interpretation if negative).”””
	 if k < 0:
	 k += len(self) # attempt to convert negative index

	 if not 0 <= k < self. length:
	 raise IndexError( index out of range )

	 return self. start + k self. step