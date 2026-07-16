a = [1,2,3]
b = a
c =[1,2,3]
d =[1,2,3]

print(a is b) #true, since a and b refer to the same oblect
print(a is c) #false, since a and c refer to different objects
print(c is d) #false, since c and d refer to different objects
print(a == c) #true, since the contents of a and c are equal
print(c == d) #true, since the contents of c and d are equal