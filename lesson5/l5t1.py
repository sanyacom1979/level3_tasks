'''
n = 4
m = 5
f_r = {"helloworld.exe" : ["R", "X"],
"pinglog" : ["W", "R"],
"nya" : ["R"],
"goodluck" : ["X", "W", "R"]
}
q = ["read nya", "write helloworld.exe", "execute nya",
"read pinglog", "write pinglog"]

for i in q:
	if i.split(" ")[0][0].upper() in f_r[i.split(" ")[1]]:
		print("OK")
	else:
		print("Access denied")
'''