from orm import Model

class Employee(Model):
    def __init__(self, emp_id=0, name=None, designation=None, salary=0):
        self.id = emp_id
        self.name = name
        self.designation = designation
        self.salary = salary
