def calculate_stats(numbers):
    total =sum(numbers)
    average = total / len(numbers)
    maximum =max(numbers)
    minimum =min(numbers)
    return total, average, maximum, minimum
#Example usege
numbers = [5, 10, 15, 20, 25]
total, avg, max_num, min_num = calculate_stats(numbers)
print(f"Total Sum: {total}")
print(f"Average: {avg}")
print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")