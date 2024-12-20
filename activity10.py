def get_student_info():
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

get_student_info()