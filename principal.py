print("Write a program to input p, r, n and find out interest using simple input output statement.")

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
n = float(input("Enter time: "))

si = (p * r * n) / 100

print("Simple Interest =", si)
