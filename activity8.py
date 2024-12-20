name = input("Please Enter your Name-->:")
password = input("Good Day! Please input your password--> :")

if password.lower() == "secret":
	print("Access Granted for", name)
	print("Enjoy using the system")
elif password.lower() == "shimenet":
	print("Hello Sara Duterte")
	print("Shimenet like my system")
else:
	print("Access Denied")
print("System Exit")
