# Read numbers from a file
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

# Compute statistics
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Write results to a new file
with open("results.txt", "w") as file:
    file.write(f"Sum: {total}\nAverage: {average}\nMax: {maximum}\nMin: {minimum}\n")

# Reverse a string
def reverse_string(s):
    return s[::-1]

# Test reverse_string
print(reverse_string("Python"))
