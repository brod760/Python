print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size would you like? S, M, L? ") # What size pizza do you want? S, M, or L
add_pepperoni = input("Pepperoni, Y, N? ") # Do you want pepperoni? Y or N
extra_cheese = input("Extra Cheese, Y, N? ") # Do you want extra cheese? Y or N
#Need to find out what kind of pizza the customer wants
bill = 0 
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25 #since S&M are used you dont have to speicify the L size
  
if add_pepperoni == "Y":
  if size == "S": #charging for pep is diff for small
    bill +=2 
  else:
    bill +=3 #dollar more for M or L pizzas 

if extra_cheese == "Y":
  bill += 1
else: 
 bill += 0 # can omit this
print(f"Your final bill is: ${bill}.")
