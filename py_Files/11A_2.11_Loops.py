# while and for loops
# while loops

x=0
while (x<5):
    print(x)
    x=x+1

# practice
# x=0
# while (x<10):
#     print(x)
#     x=x+1
    
for y in range (2,10):
     print(y)

# for x in range (2,10):
#       print(x) 

# practice
# for x in range (2,10):
#     print(x)


# array
days= ["mond", "tue", "wed", "thur", "fri", "sat", "sund"]

for i in days:
    print (i)

    
# practice
days=["M","T","W","Th","F","Sa","Su"]
for d in days:
    #if (d=="F"): break
    if (d=="F"): continue
    print(d)