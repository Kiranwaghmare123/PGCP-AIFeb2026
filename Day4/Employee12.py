class Order:

def calculateBill(self, price)
	tax = price * 0.18
	total = price + tax
	
	print("Price= ", price)
	print("Tax= ", tax)
	print("Total Amount= ", total)
	
o1 = Order()
o1.calculateBill(1000)