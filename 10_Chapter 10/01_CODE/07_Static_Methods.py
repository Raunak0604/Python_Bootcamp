class Employee:
    company = "Google"

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9AM in the morning")

rabbit = Employee()
rabbit.greet() # Employee.greet()
rabbit.time()

