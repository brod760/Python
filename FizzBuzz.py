limit = 100
for nums in range( 1,limit +1):
    if nums % 3 == 0 and nums % 5 == 0:
        print("FizzBuzz")
    elif nums % 3 == 0:
        print("Fizz")
    elif nums % 5 == 0:
        print("Buzz")
    else:   
        print(nums)