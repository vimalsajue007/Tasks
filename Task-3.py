# Section 1: Loop Basics (1–10)
# Task 1 - Print numbers from 1 to 50 using for loop
for i in range(1, 51):
    print(i)


# Task 2 - Print even numbers from 1 to 100
for i in range(1, 101):
    if i%2==0:
        print(i)


# Task 3 - Print odd numbers from 1 to 100
for i in range(1, 101):
    if i%2!=0:
        print(i)


# Task 4 - Print multiplication table of 7
for i in range(1, 11):
    print(i, "* 7 =", i*7)
    

# Task 5 - Find sum of numbers from 1 to 100
total = 0
for i in range(1, 101):
    total += i
print("Sum =", total)


# Task 6 - Print numbers in reverse from 50 to 1
for i in range(50, 0, -1):
    print(i)


# Task 7 - Count how many numbers are divisible by 3 (1–100)
count = 0
for i in range(1, 101):
    if i % 3 == 0:
        count += 1
print("Count =", count)


# Task 8 - Print squares of numbers from 1 to 10
for i in range(1, 11):
    print(i*i)


# Task 9 - Print cube of first 10 numbers
for i in range(1, 11):
    print(i ** 3)


# Task 10 - Take input n, print numbers from 1 to n
n = int(input("Enter the Value : "))
for i in range(1, n+1):
    print(i)


# Section 2: While Loop (11–15)
# Task 11 - Print numbers from 1 to 20 using while
i = 1
while i<=20:
    print(i)
    i+=1


# Task 12 - Find factorial of a number using while
n = int(input("Enter a number: "))
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial =", fact)



# Task 13 - Reverse a number using while
n = int(input("Enter the number : "))
rev = 0
while n:
    rev = rev * 10 + n % 10
    n //= 10
print(rev)


# Task 14 - Count digits in a number
n = int(input("Enter a number: "))
count = 0
while n != 0:
    n //= 10
    count += 1
print("Number of digits =", count)


# Task 15 - Keep asking input until user enters "stop"
x=[]
while True:
    user_input = input("Enter something (type 'stop' to end): ")   
    if user_input.lower() == "stop":
        break
    x.append(user_input)
print(x)


# Section 3: Nested Loop (16–20)
# Task 16 - Print pattern:
# *
# **
# ***
# ****
for i in range(1, 5):
    print("*" * i)


# Task 17 - Print pattern:
# 1
# 12
# 123
# 1234
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end="")
    print()


# Task 18 - Print multiplication table (1 to 5) using nested loop
for i in range(1, 6):
    print(f"Table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()


# Task 19 - Print:
# A B C
# A B C
# A B C
for i in range(3):
    for j in ["A", "B", "C"]:
        print(j, end=" ")
    print()


# Task 20 - Print:
# 1 2 3
# 4 5 6
# 7 8 9
num = 1
for i in range(3):
    for j in range(3):
        print(num, end=" ")
        num += 1
    print()


# Section 4: String Basics (21–25)
# Task 21 - Count total characters in a string
text = input("Enter a string: ")
print("Total characters =", len(text))


# Task 22 - Count vowels in a string
text = input("Enter a string: ").lower()
vowels = "aeiou"
count = 0
for ch in text:
    if ch in vowels:
        count += 1
print("Vowels =", count)


# Task 23 - Count consonants in a string
text = input("Enter a string: ").lower()
count = 0
for ch in text:
    if ch.isalpha() and ch not in "aeiou":
        count += 1
print("Consonants =", count)


# Task 24 - Reverse a string using loop
text = input("Enter a string: ")
emt = ""
for i in text:
    emt = i + emt
print("Reversed =", emt)


# Task 25 - Check if string is palindrome
text = input("Enter a string: ")
palin = text[::-1]
if text == palin:
    print("Palindrome")
else:
    print("Not Palindrome")


# Section 5: String Slicing (26–30)
# Task 26 - Print first 5 characters of a string
a = input("Enter a Word : ")
print(a[:5])


# Task 27 - Print last 3 characters
a  = input("Enter the Word : ")
print(a[-3:])


# Task 28 - Print string in reverse using slicing
a = input("Enter the word : ")
print(a[::-1])


# Task 29 - Print every 2nd character
text = input("Enter the Word : ")
print(text[1])


# Task 30 - Remove first and last character from string
text = input("Enter the word")
print(text[1:-1])


# Section 6: List Basics (31–35)
# Task 31 - Create a list of 5 numbers and print sum
list = [10, 20, 30, 40, 50]
print("Sum =", sum(list))



# Task 32 - Find maximum value in list
list1 = [10, 20, 30, 40, 80]
print("Max =", max(list1))


# Task 33 - Find minimum value in list
list2 = [10, 20, 30, 40, 50]
print("Min =", min(list2))


# Task 34 - Count total elements in list
list3 = [10, 20, 30, 40, 50]
print("Total elements =", len(list3))


# Task 35 - Check if element exists in list
list4 = [10, 20, 30, 40, 50]
x = int(input("Enter number to check: "))
if x in list4:
    print("Exists")
else:
    print("Not Exists")


# Section 7: List Operations (36–40)
# Task 36 - Add 3 elements using append()
num = []
num.append(10)
num.append(20)
num.append(30)
print(num)


# Task 37 - Insert element at specific index
x = [10, 20, 30, 40]
x.insert(2, 25)
print(x)


# Task 38 - Remove element using remove()
y = [10, 20, 30, 40]
y.remove(20)  
print(y)


# Task 39 - Reverse list without using .reverse()
z = [10, 20, 30, 40]
reverse = z[::-1]
print(reverse)


# Task 40 - Sort list without using .sort()
value = [40, 10, 30, 20]
for i in range(len(value)):
    for j in range(i + 1, len(value)):
        if value[i] > value[j]:
            value[i], value[j] = value[j], value[i]
print(value)