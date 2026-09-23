n = int(input("Enter number of subjects: "))

total = 0

for i in range(n):
    marks = float(input("Enter marks: "))
    total = total + marks

average = total / n

print("Average Marks =", average)
