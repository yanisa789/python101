def print_all(*args):
    for index, args in enumerate(args):
        print(f"Argument {index + 1}: {args}")
#example usage
print_all("python", 3.8, True, [1, 2, 3], {"key": "value"})
#output:
#argument 1: python
#argument 2: 3.8
#argument 3: True
#argument 4: [1,2,3]
#argument 5: {'key': 'value'}