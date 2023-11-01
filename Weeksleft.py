#This simple program calculates and displays the weeks you have left. Assuming that you live to 90
age = input()
years = 90 - int(age)
#Need to convert years to weeks. Mult by 52
WeeksLeft = int(years) * 52
#f string to show result
print(f"You have {WeeksLeft} weeks left.")