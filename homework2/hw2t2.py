def reverse_dict(d):
	d1 = {v : k for k, v in d.items()}
	d.clear()
	d.update(d1)

if __name__ in "__main__":
	d = {"a" : 10, "b" : 8, "e" : 11, "g" : 6, "x" : 3}
	print(f"До {d}")
	reverse_dict(d)
	print(f"После {d}")