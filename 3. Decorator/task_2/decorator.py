
def show_name(func):

	def wrapper(*args):
	
		print(f"->{func.__name__} was called")
		return func(args)

	return wrapper




