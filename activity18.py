tri = eval(input("Please enter number of triangle/s-->:  "))
for a in range (1,5):
    for b in range (1, tri + 1):
        for c in range (1, a + 1):
            print("*", end= " ")
        for d in range (5, a, -1):
            print(" ", end= " ")
        print(end= " ")
    print()
