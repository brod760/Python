year = int(input("Enter a year "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:  
      print("Leap year")#year has to meet all 3 conidtions to be considered a leap year.
    else:
        print("Not leap year")  
  else:
      print("Leap year") 
else:
      print("Not leap year")