student = {1: "Ashok", 2: "Raj", 3: "Govind"}

roll_no = int(input("Enter a number: "))

name = student.get(roll_no, "Student")
print(f"Congratulation {name}")
