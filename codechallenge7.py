Grocery = input("Good Day, Customer! Did you buy a grocery? (YES?NO) -->:   ")
if Grocery.lower() == "yes":
    print("Thank you for buying to our store, my dear customer!")
item = input("What item did you buy? -->:   ")
cost = float(input("How much is the cost of the item you bought? -->:    "))
gvAmount = int(input("Given Amount -->:   "))
age = int(input("How old are you? (Senior Citizen discount of 20% will be applied if you are qualified for the discount.)"))

tax = cost * 0.123
total = cost + tax

print = (f"A 12.3% tax of PHP{tax} was added to the cost of the item.")

if age >=60:
        discount = total * 0.052
        discounted = total - discount
        print(" You have received a 5.2% of discount because you are qualified for the Senior Citizen Discount.")
        


