#Creating an empty list called my_list
my_list = []

#Appending values to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#Inserting value to second position
my_list.insert(1, 15)

#extending my_list to another list
list2 = [50,60,70]
my_list.extend(list2)

#removing the last element from my list
my_list.pop()

#sorting the list in ascending order
my_list.sort()

#Find and print the index of the value 30 in my_list
print(my_list.index(30))

#printing the list finally
print(my_list)