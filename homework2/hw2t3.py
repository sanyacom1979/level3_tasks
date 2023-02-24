import hashlib

def register_user(d, login, pwd):
	if not login in d:
		d[login] = hashlib.md5(pwd.encode("utf-8")).hexdigest()
	else:
		print(f"Пользователь с логином {login} уже существует.")


def login_user(d, login, pwd):
	if login in d:
		if hashlib.md5(pwd.encode("utf-8")).hexdigest() == d[login]:
			return "ok"
		else:
			return "failed"
	else:
		return "failed"


if __name__ == "__main__":
	
	d = {}

	print(f"Пользователей нет {d}")
	
	print("Регистрация пользователей")

	while True:
		login_pwd = input("Логин ' ' пароль: ").split(" ")
		if login_pwd[0] == "0":			
			break
		login, pwd = login_pwd
		register_user(d, login, pwd)

	print(f"После заполнения пользователей {d}")

	print("Попытки залогиниться")
    
	if d:
		while True:
			login_pwd = input("Логин ' ' пароль: ").split(" ")
			if login_pwd[0] == "0":
				break
			login, pwd = login_pwd
			print(login_user(d, login, pwd))
	