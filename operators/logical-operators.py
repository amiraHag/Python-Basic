#Logical operators: three types and, or , not
#logical operators used when we complix condition
x = 4
y=8
z = 10

#And logical operator and : check if the variable value satisfy all the conditions
print((y>x) and (y<z) )
print((x>y) and (y<z) )
print((x>y) and (y>z) )

#Or logical operator or : check if the variable value satisfy any of the conditions
print((y>x) or (y<z) )
print((x>y) or (y<z) )
print((x>y) or (y>z) )

#Not logical operator not : get the inverse of the condition
print(not(y>x) )
print(not(x>y))
