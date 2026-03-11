# Task 1 - Print Formatting

# First line
print("Hello", "World", "Welcome", "Python", sep=" ", end="\n")

# Second line
print("Laptop", "Mouse", "Keyboard", sep=" | ")


# Task 2 - Variables
name = "Ravi"
age = 22
city = "Chennai"
print(name, age, city, sep="-")


# Task 3 - Multiple assignment
name, age, student = "Meena", 20, True
print(name, age, student)



# Task 4
word = "Python"
print("First letter:", word[0])
print("Third letter:", word[2])
print("Last letter:", word[-1])



# Task 5 - Arithmetic operations
print("25 + 10 =", 25 + 10)
print("50 - 20 =", 50 - 20)
print("8 * 5 =", 8 * 5)
print("100 / 10 =", 100 / 10)
print("10 % 3 =", 10 % 3)
print("2 ** 4 =", 2 ** 4)
print("20 // 3 =", 20 // 3)



# Task 6 - BODMAS
print(3 + 2 * 5 ** 2)


# Task 7 - Assignment Operator
#first problem
num = 50
num += 25
print(num)

# second problem
num = 100
num /= 10
print(num)


# Task 8 - Comparison Operator
print(10 > 5)
print(20 < 15)
print(5 == 5)
print(10 != 8)
print(7 >= 7)
print(6 <= 2)


# Task 9 - String Comparison
a = "apple"
b = "Apple"

print(a == b)


# Task 10 – Logical Operators
print(10 > 5 and 5 == 5)
print(5 > 10 or 10 == 10)
print(not(5 > 2))


# Task 11 – Membership Operator
numbers = [10, 20, 30, 40, 50]
print(20 in numbers)
print(60 in numbers)
print(30 not in numbers)


# Task 12 – Swap Variables
a = 10
b = 20
a, b = b, a
print("a =", a)
print("b =", b)


# Task 13 – Bitwise XOR
a = 6
b = 3

print(a ^ b)