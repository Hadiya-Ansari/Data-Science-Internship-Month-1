# Internship Task 1: Python Data Handling
# Part 1: List Operations
# -------------------------------

numbers = [
    12, 45, 23, 67, 89, 34, 22, 10, 5, 99,
    76, 54, 31, 18, 27, 40, 60, 71, 83, 90,
    14, 36, 48, 52, 66, 74, 81, 95, 3, 58
]

# Calculate Mean
mean = sum(numbers) / len(numbers)

# Calculate Median
numbers.sort()
length = len(numbers)

if length % 2 == 0:
    median = (numbers[length // 2 - 1] + numbers[length // 2]) / 2
else:
    median = numbers[length // 2]

# Min and Max
minimum = min(numbers)
maximum = max(numbers)

print("List Statistics")
print("Mean:", mean)
print("Median:", median)
print("Minimum:", minimum)
print("Maximum:", maximum)


# -------------------------------
# Part 2: Dictionary Operations
# -------------------------------

students = {
    "Amit": 85,
    "Riya": 92,
    "Neha": 78,
    "Rahul": 88,
    "Pooja": 91,
    "Karan": 74,
    "Sneha": 95,
    "Vikas": 80,
    "Anjali": 89,
    "Rohit": 76
}

# Convert dictionary to list and sort
sorted_students = sorted(students.items(), reverse=True, key=lambda x: x[1])

print("\nTop 3 Scorers")
print(sorted_students[0][0], ":", sorted_students[0][1])
print(sorted_students[1][0], ":", sorted_students[1][1])
print(sorted_students[2][0], ":", sorted_students[2][1])


# -------------------------------
# Part 3: File Handling
# -------------------------------

file_sum = 0

with open("numbers.txt", "r") as file:
    for line in file:
        file_sum += int(line)

print("\nSum of numbers from file:", file_sum)
