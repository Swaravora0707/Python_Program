#3.Write a program to enter marks of 4 subjects and display result (resultshall include total, percentage and grade

Sub1 =int(input("Enter Your C.net Subject Marks :"))
Sub2 =int(input("Enter Your Python Subject Marks:"))
Sub3=int(input("Enter Your Mobile Programming Subject Marks:"))
Sub4=int(input("Enter Your DAV Subject Marks:"))

total = Sub1 + Sub2 + Sub3 + Sub4
percentage = (total / 400) * 100   


if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"


print("\n--- Result ---")
print("Total Marks:", total)
print("Percentage:", percentage, "%")
print("Grade:", grade)
