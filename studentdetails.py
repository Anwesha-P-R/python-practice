name = input("Enter student name: ")
age = int(input("Enter age: "))
cgpa = float(input("Enter CGPA: "))
gender = input("Enter gender: ")
hosteller = input("Is the student a hosteller? (True/False): ") == "True"
roll_no = int(input("Enter roll number: "))

print("\n--- Student Details ---")
print("Name       :", name)
print("Age        :", age)
print("CGPA       :", cgpa)
print("Gender     :", gender)
print("Hosteller  :", hosteller)
print("Roll Number:", roll_no)
