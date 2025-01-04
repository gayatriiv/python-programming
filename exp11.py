class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_employee_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee ID: {self.emp_id}")

class Manager(Employee):
    def __init__(self, name, emp_id, post, no_of_employees):
        super().__init__(name, emp_id)
        self.post = post
        self.no_of_employees = no_of_employees

    def display_manager_info(self):
        self.display_employee_info()
        print(f"Post: {self.post}")
        print(f"Number of Employees: {self.no_of_employees}")

manager = Manager("Juni", 101, "Team Lead", 5)
manager.display_manager_info()
