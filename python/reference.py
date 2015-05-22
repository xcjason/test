funcs = []
for i in range(10):
	funcs.append(lambda: i)

for func in funcs:
	print func()