#This is a simple bmi calculator. 
#It takes user inputs such as height in meters and weight in kilograms
print("This is a BMI Calculator")
print("Please enter your height in meters!")
height = input() # stored as str 
print("Please enter weight in kg!")
weight = input() # stored as str
int_weight = int(weight) 
float_height = float(height) #you have to use the float to be able to maths 
bmi = int_weight / (float_height **2) # ** rasies the ^2
finalbmi = round(bmi)  # round function gives the nearest whole number 
print(f"Your bmi is {finalbmi}") #use of the fstring to display BMI in sentence!
