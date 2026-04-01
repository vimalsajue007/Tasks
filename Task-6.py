# Task 1: Encapsulation (User Class)
class User:
    def __init__(self):

        self.__user_name = ""
        self.__pwd = ""

    def set_user(self, user_name, pwd):
        self.__user_name = user_name
        self.__pwd = pwd

    def get_user(self):
        return self.__user_name

    def register(self):
        print("Registering user:", self.__user_name)

    def login(self):
        print("Logging in:", self.__user_name)

user1 = User()

user1.set_user("john", "1234")

user1.register()
user1.login()


# Task 2: Inheritance (User → Student, Faculty)
class User:
    def register(self):
        print("user registered")

    def login(self):
        print("user logged in")

class Student(User):
    def student_greet(self):
        print("Hello Student")

class Faculty(User):
    def faculty_greet(self):
        print("Hello Faculty")

class TempFaculty(Faculty):
    def tempFaculty_greet(self):
        print("Hello Temp Faculty")

print(" Student Object ")
s = Student()
s.register()        
s.login()           
s.student_greet()   


print("\n Faculty Object ")
f = Faculty()
f.register()        
f.login()           
f.faculty_greet()   

print("\n TempFaculty Object ")
t = TempFaculty()
t.register()            
t.login()               
t.faculty_greet()       
t.tempFaculty_greet()   



# Task 3: Method Overriding
class User:
    def greet(self):
        print("Welcome User")

class Student(User):
    def greet(self):   
        print("Welcome Student")

class Faculty(User):
    def greet(self):  
        print("Welcome Faculty")

student = Student()
faculty = Faculty()

student.greet()
faculty.greet()


# Task 4: Method Chaining
class User:
    
    def register(self):
        print("registered")
        return self   

    def login(self):
        print("logined")
        return self   

    def greet(self):
        print("enjoy everyone")
        return self   

user = User()

user.login().greet().register()


# Task 5: Combined Task (Real-Time)
class User:
    users_count = 0   

    def __init__(self, username, pwd):
        
        self.__username = username
        self.__pwd = pwd

        User.users_count += 1

    def get_user(self):
        return self.__username

    def register(self):
        print("registered")
        return self

    def login(self):
        print("logined")
        return self

    def greet(self):
        print("Welcome User")
        return self

class Student(User):
    def greet(self):   
        print("Welcome Student")
        return self

class Faculty(User):
    def greet(self):   
        print("Welcome Faculty")
        return self

student = Student("john", "1234")
faculty = Faculty("smith", "5678")

print(" Student ")
student.login().greet().register()

print("\n Faculty ")
faculty.login().greet().register()

print("\nTotal Users:", User.users_count)