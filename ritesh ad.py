import json
import os

class Employee:
    def __init__(self, employee_id, name, email, department, salary, experience):
        self.employee_id = employee_id
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary
        self.experience = experience
        
    def display_details(self):
        print("\n-------------------")
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Department:", self.department)
        print("Salary:", self.salary)
        print("Experience:", self.experience)
        print("bonus:", self.calculate_bonus())
        print("-------------------\n")
        
    def update_details(self):
        self.name = input("Enter New Name:")
        self.email = input("Enter New Email:")
        self.department = input("Enter New Department:")
        self.salary = float(input("Enter New Salary:"))
        self.experience = int(input("Enter New Experience:"))
        print("Employee details updated successfully!")
        
    def calculate_bonus(self):
        return self.salary * 0.10
    
    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "email": self.email,
            "department": self.department,
            "salary": self.salary,
            "experience": self.experience
        }
        
class EmployeeManager:
    def __init__(self):
        self.employees = []
        self.load_data()
        
    def add_employee(self):
        employee_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        email = input("Enter Email: ")
        department = input("Enter Department: ")
        salary = float(input("Enter salary:"))
        experience = int(input("Enter Experience:"))
        
        emp = Employee(
            employee_id,
            name,
            email,
            department,
            salary,
            experience
        )
        
        self.employees.append(emp)
        self.save_data()
        print("Employee added successfully!")
        
    def view_employees(self):
        if not self.employees:
            print("No employees found.")
        else:
            for emp in self.employees:
                emp.display_details()
                
    def search_employee(self):
        employee_id = input("Enter Employee ID to Search:")
        
        for emp in self.employees:
            if emp.employee_id == employee_id:
                emp.display_details()
                return emp
            
        print("Employee not found.")
        return None
    def update_employee(self):
        emp = self.search_employee()
        
        if emp:
            emp.update_details()
            self.save_data()
            
    def delete_employee(self):
        emp_id = input("Enter Employee ID to Delete:")
        
        for emp in self.employees:
            if emp.employee_id == emp_id:
                self.employees.remove(emp)
                self.save_data()
                print("Employee deleted successfully!")
                return
        print("Employee not found.")
        
    def save_data(self):
        data = []
        
        for emp in self.employees:
            data.append(emp.to_dict())
            
        with open("employees.json", "w") as f:
            json.dump(data, f)
            
    def load_data(self):
        if os.path.exists("employees.json"):
            with open("employees.json", "r") as f:
                data = json.load(f)
                
                for emp in data:
                    employee = Employee(
                        emp["employee_id"],
                        emp["name"],
                        emp["email"],
                        emp["department"],
                        emp["salary"],
                        emp["experience"]
                    )
                    self.employees.append(employee)

manager = EmployeeManager()

while True:
    print("\n===== Employee Management system =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")         
    print("5. Delete Employee")
    print("6. Exit")        
    
    choice = input("enter your choice:")
    
    if choice == "1":
        manager.add_employee()
        
    elif choice == "2":
        manager.view_employees()
        
    elif choice == "3":
        manager.search_employee()
        
    elif choice == "4":
        manager.update_employee()
        
    elif choice == "5":
        manager.delete_employee()
        
    elif choice == "6":
        print("Thank you!")
        break 
    
    else:
        print("Invalid choice. Please try again.")