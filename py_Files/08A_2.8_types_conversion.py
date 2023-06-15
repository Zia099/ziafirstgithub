x=7                # int
y=10.2             # float
z="Hellow"         # str
print(type(x))
print(type(y))
print(type(z))

# # implicit type conversion
x=x+y
print(x, ", Type of x :", type(x))

#practice
x=3   # shift+alt+A
y=5.6
z=x+y
print(z , "\nType of z: \n", type(z))

# explicit type conversion
""" age=input("what is your age? ")
print(age, "\n", type(age))
age=int(age)
print(type(age)) """

# #Practice
age= input("what is your age? ")
print(age, type(age))

print(type(int(age)))

# # name
# # name=input("what is your name? ")
# # print(name, type(name))
# # print(type(str(name)))
