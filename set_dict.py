color_set= set() 
color_set.add("ajay")
fruits = ["apple", "banana", "cherry"]
mixed = (1, "hello", 3.14, True)
color_set.update(fruits)
color_set.update(mixed)
## after update and adding all list var items 

print(color_set) 


# find index of value in tuple 
print(mixed.index(3.14))
print(fruits.index("banana"))
# fruits.remove("banana")
if "banana" in fruits:
    fruits.pop(fruits.index("banana"))
print(fruits)
print(sorted(color_set))
