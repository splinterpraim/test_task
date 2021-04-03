

#Text of Errors
Text_errors = {
				'TypeError' : 'TypeError: Function parameters are incorrect',
				'IndexError':'IndexError: You have not passed arguments to the function',
				'ZeroDivisionError': 'ZeroDivisionError: Division by zero occurred'}




def sum(*args):

	try:
		if len(args) == 0:
			raise IndexError

		result = 0
		for p in args:
			try:

				if not isinstance(p,(float, int)):
					raise TypeError

				result += p

			except TypeError:
				print(Text_errors['TypeError'])
				result = None
				break;

	except IndexError:
		print(Text_errors['IndexError'])
		result = None

	return result


def subtract(*args):

	try:
		if len(args) == 0:
			raise IndexError

		result = args[0]
		if not isinstance(result,(float, int)):
				raise TypeError

		for p in args[1:]:
			try:

				if not isinstance(p,(float, int)):
					raise TypeError

				result -= p

			except TypeError:
				print(Text_errors['TypeError'])
				result = None
				break;

	except IndexError:
		print(Text_errors['IndexError'])
		result = None

	except TypeError:
		print(Text_errors['TypeError'])
		result = None

	return result


def multiply(*args):

	try:
		if len(args) == 0:
			raise IndexError

		result = 1
		for p in args:
			try:

				if not isinstance(p,(float, int)):
					raise TypeError

				result *= p

			except TypeError:
				print(Text_errors['TypeError'])
				result = None
				break;

	except IndexError:
		print(Text_errors['IndexError'])
		result = None

	return result


def divide(*args):

	try:
		if len(args) == 0:
			raise IndexError

		result = args[0]
		if not isinstance(result,(float, int)):
			raise TypeError

		for p in args[1:]:
			try:
				
				if not isinstance(p,(float, int)):
					raise TypeError

				result /= p

			except TypeError:
				print(Text_errors['TypeError'])
				result = None
				break;

			except ZeroDivisionError:
				print(Text_errors['ZeroDivisionError'])
				result = None
				break;

	except IndexError:
		print(Text_errors['IndexError'])
		result = None

	except TypeError:
		print(Text_errors['TypeError'])
		result = None
		
	return result
