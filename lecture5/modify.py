counter = 0
def increment():
    global counter
    counter += 1
#calling the function
increment()
increment()
print(counter)   #output: 2