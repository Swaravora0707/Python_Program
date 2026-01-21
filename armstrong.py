#4. Write a program to enter 10 numbers and display all armstrong numbers from those numbers.

a =int(input("Enter 10 numbers:"))

for i in range(10):
    num = int(input())
    n = num
    power = len(str(num))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** power
        n //= 10

    if total == num:
        print(num, "is an Armstrong Number")



