marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    mark = float(input("Enter marks: "))
    marks.append(mark)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

count = 0
for mark in marks:
    if mark > 80:
        count += 1

print("\n--- Marks Analysis ---")
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Highest Mark:", highest)
print("Lowest Mark:", lowest)
print("Subjects scoring more than 80:", count)
