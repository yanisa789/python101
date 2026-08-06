global_variable = "I'm outside the function"

def my_function():
    print(global_variable)
    
my_function()  #output: I'm outside the function
print(global_variable)  #output: I'm outside the function