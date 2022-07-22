class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Salary for this employee working in {self.company} is {self.salary}")

rabbit = Employee()
rabbit.salary = 100000
rabbit.getSalary() # Employee.getSalary(rabbit)