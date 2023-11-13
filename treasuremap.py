line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]

map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to hide the treasure?\n") 

letter = position[0].lower() #lower cases the user input
abc = ["a","b","c"] 
letterdex = abc.index(letter) #sorts the indexs with letters
numberdex = int(position[1]) -1 #need to minus one, starts counting from 0 
map[numberdex][letterdex] = "X" #number index has to g first, due to the index being in a nested loop

print(f"{line1}\n{line2}\n{line3}")