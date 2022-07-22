class Employee:
    company = "Google"
    salary = 100

rabbit = Employee()
souvik = Employee()

# Creating instance attribute salary for both the objects
# rabbit.salary = 300
# souvik.salary = 400

rabbit.salary = 45
print (rabbit.salary)
print (souvik.salary)

# Below line throws an error as address is not present in instance/class 
# print(souvik.address) 