'''
data = "((())))(()"

counter = 0

for elem in data:
	if elem == "(":
		counter += 1
	elif elem == ")":
		counter -= 1
	if counter < 0:
		break

if counter:
	print("Incorrect")
else:
	print("Ok")
'''