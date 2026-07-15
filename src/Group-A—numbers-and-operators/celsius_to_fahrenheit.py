'''This is a simple program that converts Celsius to Fahrenheit.'''

'''Definiing the variables.'''
c = 0
f = 0
while_flag = True


'''Function to request user input.'''
def request_input():
	global c
	c = input("Enter the temperature in celsius: ")
	return c

while while_flag:
	try:
		request_input()
		c = float(c)
		'''Calculation for the conversion.'''
		f = (c * 1.8) + 32
		'''Conditional statements to determine if it is hot or cold outside.'''
		if c > 15:
			print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit. It is hot outside.")
		elif c < 15:
			print(f"{c} degrees Celsius is equal to {f} degrees Fahrenheit. It is cold outside.")
		while_flag = False
	except:
		print(f"You have entered {c} which is not an integer or float")
		request_input()




