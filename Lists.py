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

#creating new variable and using range function
x=[]
for i in range(10):
    x.append(i)
print(x)

#using list slicing
print("list slicing and striding")
print(x[:]) #print whole list
print(x[::2])# print list wuth interval 2
print(x[2:5]) #print list starting at index 2 and ending at 4
print(x[2:])  #print list from 3rd element to last
print(x[:8:3])  #print list from start index=0, end index=5 and step=3
print(x[:-2]) # using negative indexes, print upto 2nd last number(exclusive)
print(x[-1]) #print last number

#entend() to add another list's items completely
y=[21,55,66,88,33,22,99]
x.extend(y)
print(x)
x.reverse()
#reversing list in place
print(x)
#sorting list in place
x.sort()
print(x)
x.sort(reverse=True)
print(x)

print("Sorted list",sorted(x,reverse=False))
print("List in descending order",sorted(x,reverse=True)) #temporary
print(x)

#list can contain any type even another list as an element
list1=[1,2,4.8,9.0,'a','b',"hello"]
print(list1)
list1.append(x)
print(list1)
list1.append((2,3)) #appending tuple in the list
print(list1)

del list1[-2]
print(list1)
