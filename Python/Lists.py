my_list = [1, 2, "up" , "down" , "left"] 
print(my_list)
print(my_list[0])
print(my_list[-1])
del my_list[0] # Deletes the object in the element position
print(my_list)
my_list.remove(2) # Removes all matching objects in the list
print(my_list)
my_list.append(input("What is missing from this list: "))
print(my_list)