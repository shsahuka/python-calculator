def calculator(operation, num1, num2):
	"""Perform arithmetic on two numbers."""
	if operation == "add":
		return num1 + num2
	if operation == "subtract":
		return num1 - num2
	if operation == "multiply":
		return num1 * num2
	if operation == "divide":
		if num2 == 0:
			raise ValueError("Cannot divide by zero")
		return num1 / num2
	raise ValueError(f"Unsupported operation: {operation}")
