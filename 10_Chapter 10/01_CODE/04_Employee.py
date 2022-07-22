class Employee:
    company = "Google"
    salary = 100

rabbit = Employee()
souvik = Employee()

print(rabbit.company)
print(souvik.company)

Employee.company = "YouTube"

print(rabbit.company)
print(souvik.company)
