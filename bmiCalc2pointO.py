#This is a simple bmi calculator. 
#displays bmi and weight range from underwight - obese 
#It takes user inputs such as height in meters and weight in kilograms
print("This is a BMI Calculator")

weight = int(input())
print("Please enter weight in kg!") 
height = float(input())
print("Please enter your height in meters!") #you have to use the float to be able to maths 
bmi = weight / (height **2) # ** rasies the ^2
#finalbmi = round(bmi)  # round function gives the nearest whole number
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif 18.5 < bmi and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
else:
  bmi <= 35
  print(f"Your BMI is {bmi}, you are obese.")
