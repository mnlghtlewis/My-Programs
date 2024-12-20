name = input("Please enter your name-->:   ")
prelim = eval(input("Please enter your Prelim grade-->:  "))
midterm = eval(input("Please enter your Midterm grade-->:  "))
semi_final = eval(input("Please enter your Semi-Final grade-->:  "))
final = eval(input("Please enter your Final grade-->:  "))
quiz = eval(input("Please enter your Quiz grade-->:  "))
project = eval(input("Please enter your Project grade-->:  "))

final_grade = (prelim*0.15) + (midterm*0.15) + (semi_final*0.15) + (final * 0.15) + (quiz*0.15) + (project*0.15)

if final_grade >= 75:
	print("Congratulations," , name , " you have passed the course!")
else:
	print("Sorry," , name , "you failed.")
	if 0 <= grade <= 100:
		return grade
	else:
		print("Invalid Grade. Please enter a grade between 0-100")