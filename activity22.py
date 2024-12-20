def greetings():
    print("Hello Sir Mesiera")

def activity2():
    num1 = eval(input("Please enter a number-->:  "))
    num2 = eval(input("Please enter another number-->:  "))
    print(num1 , "floor divided to" , num2 "=" , num1 // num2)

def activity4():
    num1 = eval(input("Enter a number--> "))
    num2 = eval(input("Enter another number--> "))

    answer1= num1 + num2
    answer2= num1 - num2
    answer3= num1 * num2
    answer4= num1 / num2
    answer5= num1 ** num2
    answer6= num1 % num2
    answer7= num1 // num2

    print("The sum of " , num1 , " and " , num2 , " is " , answer1 )
    print("The difference of " , num1 , " and " , num2 , " is " , answer2 )
    print("The product of " , num1 , " and " , num2 , " is " , answer3 )
    print("The quotient of " , num1 , " and " , num2 , " is " , answer4 )
    print("The exponent of " , num1 , " and " , num2 , " is " , answer5 )
    print("The remainder of " , num1 , " and " , num2 , " is " ,answer6 )
    print("The floor division of " , num1 , " and " , num2 , " is " , answer7 )

def activity6():
    x = 5
    print(x)
    x = x + 10
    print(x)
    x = x + 15
    print(x)
    x += 10
    print(x)

def activity8():
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
    
def activity 9():
    age = eval(input("Good Day! Please type your age-->:   "))

    if age == 1:
	    print("Toddler")
    elif age <8:
	    print("Toddler")
    elif age == 8:
	    print("Pre-teen")
    elif age < 14:
	    print("Pre-teen")

def activity10():
    name = input("Good Day Student! Please type your name here -->: ")
    is_student = input("Are you currently an enrolled student of Dalubhasaan ng Lungsod ng Lucena? (YES/NO) : ").strip().lower()

    if is_student == "yes":
        while True:
            try:
                year_level = int(input("What year are you currently enrolled?: \n 1 - Freshmen or 1st Year \n 2 - Sophomore or 2nd Year \n 3 - Junior or 3rd Year \n 4 - Senior or 4th Year \nYour choice: "))
                if year_level in [1, 2, 3, 4]:
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 4.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        year_messages = {
            1: f"Hi {name}, Freshman, Welcome to DLL!",
            2: f"Hi {name}, Sophomore, Welcome to DLL!",
            3: f"Hi {name}, Junior, Welcome to DLL!",
            4: f"Hi {name}, Senior, Welcome to DLL!"
        }

        print(year_messages[year_level])
    else:
        print("Thank you for using the system, Goodbye!")

    activity10()

def activity11():
    for x in range (1 , 201):
        print(x, "Happy Founding Anniversary, Dalubhasaan ng Lungsod ng Lucena")

def activity12():
    for n in range (11, 0, -1): 
        print(n)

def activity13():
    num = eval(input(f"Please enter a number here-->:   "))
    factorial = 1
    for n in range (11, num * 1, -1): 
        print("n")

def activity14():
    for x in range (0, 11):
    print(x, end = " ")
    for y in range (0, 11):
        print("*", end = " ")
    print()

def activity15():
    for x in range (0, 11):
        print(x, end = " ")
    for y in range (0, x):
        print("*", end = " ")
    print()

def activity 16():
    for x in range (6, 0, -1):
        print(" ", end= " ")
    for y in range (6, x, -1):
        print(" ", end= " ")
    for z in range (1, x+1):
        print(" ", end= " ")
    for a in range (1, x + 1):
        print("*", end=" ")
    print()

    
