# Empty list
x=[]
print(type(x))
#list of numbers
x=[1,2,5,8,4,90,201]
print(x)
#to get size of list
print(len(x))
#list is mutable
#Adding items at end of list
x.append(6)
x.append(45)
print(x)

#Deleting itmems from list
#delete last item using pop or delete at any index
x.pop()
print("list after after pop() ",x)
x.pop(2)
print(x)
#using del to delete at position or remove to remove first occurance of that item
x.remove(6)
print("After removing 6",x)
del x[0]
print("After deletion at 0th index", x)

#clear a lsit
x.clear()
print(x)

#delete list variable
del x
#this print statement gives an error
#print(x)
