# Task 1: User Info Manager (Functions + Dictionary)
def create_user(name, age, role):
    user = {
        "name": name.title(), 
        "age": age,
        "role": role
    }
    return user

users = []

users.append(create_user("vimal", 22, "developer"))
users.append(create_user("john doe", 25, "manager"))
users.append(create_user("anushka", 23, "designer"))

for user in users:
    print(user)


# Task 2: Dynamic Calculator (*args)
def calculate_total(*numbers):
    total = sum(numbers)

    if len(numbers) == 0:
        average = 0
    else:
        average = total / len(numbers)
    
    return total, average

result = calculate_total(10, 20, 30, 40)

print("Total:", result[0])
print("Average:", result[1])


# Task 3: Keyword Config System (**kwargs)
def system_config(**settings):
    for key, value in settings.items():
        print(f"{key}: {value}")

system_config(mode="debug", version="1.0")


#  Task 4: Factorial Service (Recursion)    
def factorial(n):
    if n < 0:
        return "Error: Factorial not defined for negative numbers"

    elif n == 0:
        return 1
    
    else:
        return n * factorial(n - 1)

# I used both static and dynamic inputs
print(factorial(int(input("Enter the number : "))))   

# This is for example reference
print(factorial(5))   
print(factorial(-3)) 


# Task 5: Memory Optimization (Generator)
def square_generator(n):
    for i in range(n):
        yield i * i

def square_list(n):
    return [i * i for i in range(n)]

gen = square_generator(5)
lst = square_list(5)

print("Generator values:")
for val in gen:
    print(val)

print("\nList values:")
for val in lst:
    print(val)

print("\nType of generator:", type(square_generator(5)))
print("Type of list:", type(lst))


# Task 6: Exception Handling Module
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator / denominator
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter valid numbers")

finally:
    print("Program Completed")


# Task 7: File Handling
file = open("vimal_data.txt", "w")

file.write("Name: Vimal\n")
file.write("Age: 22\n")
file.write("Role: Developer\n")

file.close()

print("File closed after writing:", file.closed)

file = open("vimal_data.txt", "r")

content = file.read()
print("\nFile Content: ")
print(content)

file.close()

# This is to check again file is closed after reading
print("File closed after reading:", file.closed)