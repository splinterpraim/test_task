
#Text of Errors
Text_errors = {'TypeError' : 'TypeError: Decorator parameters are incorrect',
				'IndexError' : 'IndexError: Wrong number of decorator arguments'}


def show_name(*args1):

		
	def outer(func):

		def wrapper(*args2,**kwargs):
			try:
				if len(args1) == 0 or len(args1) > 1:
					raise IndexError
				elif not isinstance(args1[0],(float, int)):
					raise TypeError	
				new_args = args2[:-1] + (args2[-1]*args1[0],)

				print(f"->{func.__name__} was called")
				return func(*new_args,**kwargs)

			except TypeError:
				print(Text_errors['TypeError'])
				return None
			except IndexError:
				print(Text_errors['IndexError'])
				return None

		return wrapper


	return outer




