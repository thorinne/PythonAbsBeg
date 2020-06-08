# CH 2 Challenges
# Problem 2

food1 = input("What is one of your favorite foods? ")
food2 = input("Enter another one of your favorite foods? ")
print("Here is a new food to try! How about: ", food1+food2)

print("\n\n")

# Problem 3
bill = float(input("Please enter the food bill: "))
fifteen = float((bill*.15) + bill)
print("At 15%, your bill would be {:.2f}, from a bill of {:.2f}.".format(fifteen, bill))
twenty = float((bill * .20) + bill)
print("At 20%, your bill would be {:.2f}, from a bill of {:.2f}.".format(twenty, bill))

print("\n\n")

# Problem 4

car_tax = float(.075)
car_license = float(.125)
dealer_prep = int(1300)
destination_charge = int(500)
car_price = float(input("what is the price of the car: "))
total = car_price + dealer_prep + destination_charge + (car_tax * car_price) + (car_license * car_price)
print("The total comes out ot be: ",total)
