def compose_greet_function(name):
	def get_message():
		return 'Hello there ' + name + '!'

	return get_message

greet = compose_greet_function('John')
print greet()

def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

my_get_text = p_decorate(get_text)

print my_get_text("John")