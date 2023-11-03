#height checker and admission charges based by age and height 

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18: 
        print("Please pay $7.") #you can add as man elif's in between the if statemtns.
    else:
        print("Please pay $12.")
else: 
    print("Sorry, you have to grow taller before you can ride.")
