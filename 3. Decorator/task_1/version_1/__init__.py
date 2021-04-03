

def sum(*args):

	result = 0
	for p in args:
		result += p

	return result


def subtract(*args):
	
	result = args[0]
	for p in args[1:]:
		result -= p

	return result


def multiply(*args):

	result = 1
	for p in args:
		result *= p

	return result


def divide(*args):

	result = args[0]
	for p in args[1:]:
		result /= p

	return result


