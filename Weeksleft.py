#This simple program calculates and displays the weeks you have left. Assuming that you live to 90
print("Welcome to the weeks Calculator!")
age = input("what is your age?")
years = 90 - int(age)
#Need to convert years to weeks. Mult by 52
WeeksLeft = int(years) * 52
#f string to show result
print(f"You have {WeeksLeft} weeks left.")
