# Mini Project 1: Employee Management System

employees = []

# Add Employee
def add_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    role = input("Enter Role: ")
    salary = float(input("Enter Salary: "))

    emp = {
        "name": name,
        "age": age,
        "role": role,
        "salary": salary
    }

    employees.append(emp)
    print("Employee Added Successfully!\n")


# Display Employee
def display_employees():
    if not employees:
        print("No employees found!\n")
        return

    for i, emp in enumerate(employees, start=1):
        print(f"{i}. Name: {emp['name']}, Age: {emp['age']}, Role: {emp['role']}, Salary: {emp['salary']}")
    print()


# Update Employee
def update_employee():
    display_employees()
    index = int(input("Enter employee number to update: ")) - 1

    if 0 <= index < len(employees):
        employees[index]['name'] = input("Enter New Name: ")
        employees[index]['age'] = int(input("Enter New Age: "))
        employees[index]['role'] = input("Enter New Role: ")
        employees[index]['salary'] = float(input("Enter New Salary: "))
        print("Employee Updated Successfully!\n")
    else:
        print("Invalid Employee Number!\n")


# Delete Employee
def delete_employee():
    display_employees()
    index = int(input("Enter employee number to delete: ")) - 1

    if 0 <= index < len(employees):
        employees.pop(index)
        print("Employee Deleted Successfully!\n")
    else:
        print("Invalid Employee Number!\n")


# Main Menu
def main():
    while True:
        print(" Employee Management System ")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_employee()
        elif choice == '2':
            display_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            print("Exiting Program...")
            break
        else:
            print("Invalid Choice! Try again.\n")

main()



# Mini Project 2: Student Report Card
# calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"


# report card
def create_report():
    name = input("Enter Student Name: ")
    
    print("Enter marks for 3 subjects:")
    sub1 = int(input("Subject 1: "))
    sub2 = int(input("Subject 2: "))
    sub3 = int(input("Subject 3: "))

    student = {
        "name": name,
        "marks": [sub1, sub2, sub3]
    }

    total = sum(student["marks"])
    average = total / 3
    grade = calculate_grade(average)

    # formatted report
    print("\n   REPORT CARD ")
    print(f"Name     : {student['name']}")
    print(f"Marks    : {student['marks']}")
    print(f"Total    : {total}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")

create_report()


# Mini Project 3: Shopping Cart System
cart = []

# Add product
def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    cart.append(product)
    print("Product added to cart!\n")


# Display cart
def display_cart():
    if not cart:
        print("Cart is empty!\n")
        return

    print("\n===== CART ITEMS =====")
    for i, item in enumerate(cart, start=1):
        total = item["price"] * item["quantity"]
        print(f"{i}. {item['name']} | Price: {item['price']} | Qty: {item['quantity']} | Total: {total}")
    print()


# total bill
def calculate_total():
    total_bill = 0
    for item in cart:
        total_bill += item["price"] * item["quantity"]

    print(f"Total Bill: {total_bill}\n")


# Remove product
def remove_item():
    display_cart()
    index = int(input("Enter item number to remove: ")) - 1

    if 0 <= index < len(cart):
        removed = cart.pop(index)
        print(f"{removed['name']} removed from cart!\n")
    else:
        print("Invalid item number!\n")

def main():
    while True:
        print(" Shopping Cart ")
        print("1. Add Product")
        print("2. View Cart")
        print("3. Remove Product")
        print("4. Total Bill")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            display_cart()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            print("Thank you for shopping!")
            break
        else:
            print("Invalid choice!\n")

main()


# Mini Project 4: Login & User Validation
# Stored users (username: password)
users = {
    "admin": "1234",
    "vimal": "pass123",
    "user1": "abc123"
}

def login():
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in users:
        if users[username] == password:
            print("Login Successful!")
        else:
            print("Incorrect Password!")
    else:
        print("Username not found!")

login()


# Mini Project 5: Unique Visitor Counter
visitors = set()

def add_visitor():
    name = input("Enter visitor name: ")
    
    if name in visitors:
        print("Visitor already counted!\n")
    else:
        visitors.add(name)
        print("Visitor added!\n")


def show_visitors():
    print("\nUnique Visitors:")
    for v in visitors:
        print(v)
    
    print(f"\nTotal Unique Visitors: {len(visitors)}\n")


def main():
    while True:
        print("===== Visitor Counter =====")
        print("1. Add Visitor")
        print("2. Show Visitors")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_visitor()
        elif choice == '2':
            show_visitors()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

main()


# Mini Project 6: String Formatter Tool
def format_string():
    name = input("Enter your name: ")
    product = input("Enter product name: ")

    # Formatted sentence
    print("\n FORMATTED OUTPUT ")
    sentence = f"{name} purchased {product} successfully."
    print(sentence)

    # Padded
    print("\n PADDING OUTPUT ")
    print("Left Justified  :", name.ljust(20, '-'))
    print("Right Justified :", name.rjust(20, '-'))
    print("Center Justified:", name.center(20, '-'))

format_string()


# Mini Project 7: Bank Account System
account = {}

# Create account
def create_account():
    name = input("Enter Account Holder Name: ")
    balance = float(input("Enter Initial Balance: "))

    account["name"] = name
    account["balance"] = balance

    print("Account Created Successfully!\n")


# Deposit
def deposit():
    if not account:
        print("Create account first!\n")
        return

    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    print("Amount Deposited Successfully!\n")


# Withdraw
def withdraw():
    if not account:
        print("Create account first!\n")
        return

    amount = float(input("Enter amount to withdraw: "))
    
    if amount > account["balance"]:
        print("Insufficient Balance!\n")
    else:
        account["balance"] -= amount
        print("Withdrawal Successful!\n")


# Check balance
def check_balance():
    if not account:
        print("Create account first!\n")
        return

    print(f"Account Holder: {account['name']}")
    print(f"Current Balance: {account['balance']}\n")


def main():
    while True:
        print("Bank Account System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Thank you!")
            break
        else:
            print("Invalid choice!\n")

main()


# Mini Project 8: Voting System
votes = {
    "stark": 0,
    "doom": 0,
    "vivek": 0
}


def add_vote():
    print("Candidates:", ", ".join(votes.keys()))
    choice = input("Enter your vote: ")

    if choice in votes:
        votes[choice] += 1
        print("Vote added successfully!\n")
    else:
        print("Invalid candidate!\n")


def display_results():
    print("\n===== Voting Results =====")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")

    # winner
    winner = max(votes, key=votes.get)
    print(f"\nWinner: {winner}\n")


def main():
    while True:
        print("===== Voting System =====")
        print("1. Cast Vote")
        print("2. Show Results")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_vote()
        elif choice == '2':
            display_results()
        elif choice == '3':
            print("Thank you for voting!")
            break
        else:
            print("Invalid choice!\n")

main()



# Mini Project 9: Course Enrollment System
students = []

# Add student
def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(",")

    student = {
        "name": name,
        "courses": [c.strip() for c in courses]
    }

    students.append(student)
    print("Student added successfully!\n")


# Display students
def display_students():
    if not students:
        print("No students found!\n")
        return

    print("\n===== Student Details =====")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}")
        print(f"   Courses: {', '.join(student['courses'])}")
    print()


def update_courses():
    display_students()
    index = int(input("Enter student number to update: ")) - 1

    if 0 <= index < len(students):
        new_courses = input("Enter new courses (comma separated): ").split(",")
        students[index]["courses"] = [c.strip() for c in new_courses]
        print("Courses updated successfully!\n")
    else:
        print("Invalid student number!\n")


def main():
    while True:
        print("===== Course Enrollment System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Courses")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            update_courses()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice!\n")

main()



# Mini Project 10: Number Utility Tool
def convert_number(num):
    print("\n Number Conversions ")
    print(f"Binary      : {bin(num)}")
    print(f"Octal       : {oct(num)}")
    print(f"Hexadecimal : {hex(num)}")


# Format large number
def format_number(num):
    print("\n Formatted Number")
    print(f"With commas : {num:,}")


# Scientific notation
def scientific_notation(num):
    print("\n Scientific Notation ")
    print(f"Scientific  : {num:.2e}")

def main():
    num = float(input("Enter a number: "))

    convert_number(int(num))
    format_number(num)
    scientific_notation(num)

main()