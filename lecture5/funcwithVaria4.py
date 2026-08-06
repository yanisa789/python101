def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_info(name="Alice", age=35, city="New york")
#output:
#name: Alice
#age: 35
#city: New york