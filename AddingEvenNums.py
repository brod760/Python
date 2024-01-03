#This program takes the sum of all even numbers from 0 to 1000. 
target = int(input("Enter a number between 0 and 1000! ")) # Enter a number between 0 and 1000
total = 0 
for numbers in range(2,target + 1, 2):
  if numbers % 2 == 0:
    total += numbers 
print(total)
  