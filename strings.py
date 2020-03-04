#In most fo the programmming languages a b c d declared as char and write declare as string
#but in python all  a b c d write declared as string

x = "c"
print(type(x))

x = "write"
print(type(x))


#python understand string that is the data between quotes "" or ''
x= 2
print(type(x))

x = "2"
print(type(x))


#use the method to convert text from lower to upper case
#method are function related to a class like upper related to string
x = "water"
print(x.upper())

# to get all method related to datatype write dir("datatype")
dir("string")
print(dir("string"))

#to get the first char capital
print(x.title())

#to convert text from capiy]talized to lower
x= "WATER"
print(x.lower())

#remove space from string
y = "  value"
print(y)
print(y.split())


#indexing and slicing
#string contain char each one has it's own index and it starts with 0

#to get the value of char in specific index in string  we can use [index]
x='water'
print(x[2])

#if you want to replace any char use the method string_name.replace('','')
print(x.replace('t','x'))

#slicing , means splitting the sting to smaller  parts
# we can use slicing by x=[1:3] the first included and the second excluded
x= 'hello world!'
print(x[0:5])

#to get the value from the end we can use -value like x[-2]
print(x[-2])

#get part of the string from the end by using the  -ve index
print(x[-6:-1])

#to start spliting from the first char we can leave it empty like x[:5]
#to split till the end we can leave the second index empty like x[-6:]
print(x[:5])
print(x[-6:])


#string formatting -> arrange strings in order
x="My"
y="name"
z="is"
b= "amira"
a= x + " " + y +" " + z +" " + b
print(a)

#in python we can use more efficient way to format strings
#first method work in python 2 and 3 using format methon
a = "My name is {}".format(b)
print(a)
c=29

#if we have two variables we can add more than {}
a = "My name is {} and My age is {}".format(b,c)
print(a)

#we can also use the index of the argument for the function format to indicate the variable if you don't want to write the arguments in the same order
a = "My name is {0} and My age is {1}".format(b,c)
print(a)

#second method work in python 3 only using format methon f" text to display {variable name}"
a= f"My name is {b}"
print(a)
a= f"My name is {b} and My age is {c}"
print(a)

#we can also use simple list to format string and the index of the list item used in ordering the list items in the string
x=["amira" , "reading" , 29]
a=f"My name is {x[0]} , my favourite hoppy is {x[1]} and My age is {x[2]}"
print(a)
