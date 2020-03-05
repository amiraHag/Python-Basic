#list is kind of collection datatype
#colletion datatype is collection of different type of data
#list represented by [] contains many values separated by ,
x= ["red" , "green", "blue","yellow","black"]
print(x)
#list can contain different datatype
y =["red", "green","blue", 3]
print(y)

#check the method that can be applied on list by using dir()
print(dir(list))

#to access specific element in the list, we use index of the element
#the index of the element start from 0
print(y[2])
#we can use -ve index to get the list element
print(y[-1])

#to get the number of elements in the list , you can use the method len()
print(len(y))

#to remove last item on the list , use pop() function
y.pop()
print(y)

#to add item in the last on the list , use append(the item ) function
y.append(3)
print(y)

#to remove specific item on the list , use remove() function
y.remove("blue")
print(y)

#to delete the list , use del() function
del(y)
#print(y) give error because no variable name y
