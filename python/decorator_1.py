def compose_greet_function(name):
	def get_message():
		return 'Hello there ' + name + '!'

	return get_message

greet = compose_greet_function('John')
print greet()

def p_decorate(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@p_decorate
def get_text(name):
   return "lorem ipsum, {0} dolor sit amet".format(name)

print get_text('John')

# my_get_text = p_decorate(get_text)
# print my_get_text("John")