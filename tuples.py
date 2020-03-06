#tuples represented by ()
#tuples similar two list wih only two diff,
# 1. use () instead of [] in lists
# 2. elements in tubles can not be changes , this mean tuples ar not mainubilated
x=("red", "green","blue", "black","yellow", 3 , 3.4)
#tuples use indexing to access specific element just like list
print(x[2])
#we can also use negative index to access element in tuples
print(x[-2])

#x.append("orange") will get an error because tuples not manipulated
#use dir(tuple) to know the methods that can be applied to the tuple
print(dir(tuple))

#use len(tuple_name) to get the length of tuple
print(len(x))
