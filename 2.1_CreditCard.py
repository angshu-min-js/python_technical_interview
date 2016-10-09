class CreditCard:
	 ”””A consumer credit card.”””

	 def init (self, customer, bank, acnt, limit):
	 ”””Create a new credit card instance.

	 The initial balance is zero.

	 customer the name of the customer (e.g., John Bowman )
	 bank the name of the bank (e.g., California Savings )
	 acnt the acount identifier (e.g., 5391 0375 9387 5309 )
	 limit credit limit (measured in dollars)
	 ”””
	 self. customer = customer
	 self. bank = bank
	 self. account = acnt
	 self. limit = limit
	 self. balance = 0

	 def get customer(self):
	 ”””Return name of the customer.”””
	 return self. customer

	 def get bank(self):
	 ”””Return the bank s name.”””
	 return self. bank

	 def get account(self):
	 ”””Return the card identifying number (typically stored as a string).”””
	 return self. account

	 def get limit(self):
	 ”””Return current credit limit.”””
	 return self. limit

	 def get balance(self):
	 ”””Return current balance.”””
	 return self. balance
	 def charge(self, price):
	 ”””Charge given price to the card, assuming sufficient credit limit.

	 Return True if charge was processed; False if charge was denied.
	 ”””
	 if price + self. balance > self. limit: # if charge would exceed limit,
	 return False # cannot accept charge
	 else:
	 self. balance += price
	 return True

	 def make payment(self, amount):
	 ”””Process customer payment that reduces balance.”””
	 self. balance -= amount