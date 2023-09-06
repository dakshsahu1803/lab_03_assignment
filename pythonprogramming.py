#DAKSH SAHU E22CSEU1025
class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id, self.name, self.age, self.salary = emp_id, name, age, salary

    def __str__(self):
        return f"Employee ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Salary: {self.salary}"

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search(self, criteria):
        if criteria[0] == 'age':
            return [emp for emp in self.employees if emp.age == int(criteria[1])]
        elif criteria[0] == 'name':
            return [emp for emp in self.employees if criteria[1].lower() in emp.name.lower()]
        elif criteria[0] == 'salary':
            condition, salary = criteria[1], float(criteria[2])
            if condition == '>':
                return [emp for emp in self.employees if emp.salary > salary]
            elif condition == '<':
                return [emp for emp in self.employees if emp.salary < salary]
            elif condition == '>=':
                return [emp for emp in self.employees if emp.salary >= salary]
            elif condition == '<=':
                return [emp for emp in self.employees if emp.salary <= salary]
        return []

if __name__ == "__main__":
    db = EmployeeDatabase()
    
    data = [
        ("161E90", "Raman", 41, 56000),
        ("161F91", "Himadri", 38, 67500),
        ("161F99", "Jaya", 51, 82100),
        ("171E20", "Tejas", 30, 55000),
        ("171G30", "Ajay", 45, 44000)
    ]

    for emp_data in data:
        db.add_employee(Employee(*emp_data))

    print("Search options:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")
    option = int(input("Enter search option (1/2/3): "))

    criteria = []
    if option == 1:
        criteria = ['age', int(input("Enter age to search: "))]
    elif option == 2:
        criteria = ['name', input("Enter name to search: ")]
    elif option == 3:
        condition = input("Enter salary condition (>, <, >=, <=): ")
        salary = float(input("Enter salary: "))
        criteria = ['salary', condition, salary]

    result = db.search(criteria)

    if result:
        print("\nSearch results:")
        for emp in result:
            print(emp)
    else:
        print("No matching records found.")
