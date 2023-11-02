#simple tip calculator, will split the bil and also calculate tip based on fixed rated 
# update will include user to select their own tip amount. 

print("Welcome to the Tip Calculator")
bill = float(input("What was the total of the bill? ")) #input is saved as str
Numberof_ppl = int(input("How many people will split the bill?" )) #input is saved as str
Percent_ofTip = float(input("How much of tip do you want to give? 10, 12, or 15?" )) # input is saved as str
tip_as_percent = Percent_ofTip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
x = round(total_bill, 2)
print(f"Each persone will pay ${x}")


