#dictionary like list but instead of index we use partical names and called it keys
#dictionary represented by {} , x ={"key-name": key-value}
x={"number":1,"name":"amira", "age":29,"job":"developer"}

#access the value of the elements by the key name dictinary-name[key-name]
print(x["name"])

#if you want to change any element you can use dictionary-name[key-name] = new-value
x["name"] = "amirah"
print(x["name"])

#we can find the length of the dictinary by using the method len
print(len(x))

#you can add element to the dictionary by just assign value to anew keys dictinary-name[new-key-name] value
x["lastN"] ="HM"

print(len(x))

#if you want to remove element you can use pop method but you should pass the key name of the value you want to remove
x.pop("lastN")
print(len(x))

#if you want to pop the last item of the dictionary , you can use popitem method without identify the key-name
x.popitem()
print(len(x))
