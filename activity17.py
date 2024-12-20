column = eval(input("Please enter number of columns-->:  "))
for a in range (1,11):
    for b in range (1, column + 1):
        print(f"{a} x {b} = {a * b}", end= "\t")
    print()