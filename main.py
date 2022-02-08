mylist = []

# Asks for the user to input 4 numbers, then appends them to the list
for i in range(1,5):  
  input_number = input("Enter number #" + str(i))
  input_number = int(input_number)
  mylist.append(input_number)
  
# Prints out the list on separate lines
for i in range(len(mylist)):
  print(mylist[i])

# Swaps the first and last lines of the list and prints the whole list on one line
mylist[0], mylist[len(mylist)-1] = mylist[len(mylist)-1], mylist[0]
print(mylist)

# I think this should be fine, you guys can look over the code to see if it's ok to commit