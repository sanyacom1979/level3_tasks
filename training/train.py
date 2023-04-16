def a():
	v1 = 2
	v2 = 1
	def b():
		return v1 + v2
	return b

f = a()

print(f())