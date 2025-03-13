# Solution
employees = {}
def employee_id():
    return len(employees) + 1
def add_employee():
    emp_id = employee_id()
    while True:
        name = input("Enter employee name: ")
        if name.isalpha():
            break
        else:
            print("Invalid name. Name should contain only alphabets.")
    while True:
        try:
            age = int(input("Enter employee age: "))
            if age > 0:
                break
            else:
                print("Age must be a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")
    while True:
        department = input("Enter department: ")
        if department.isalpha():
            break
        else:
            print("Invalid department. Department should contain only alphabets.")
    employees[emp_id] = {"name": name, "age": age, "department": department}
    print(f"Employee {name} added successfully with ID {emp_id}.")
def remove_employee():
    emp_id = int(input("Enter the Employee ID to remove: "))
    if emp_id in employees:
        del employees[emp_id]
        print(f"Employee with ID {emp_id} removed successfully.")
    else:
        print("Employee ID not found.")
def update_employee():
    emp_id = int(input("Enter the Employee ID to update: "))
    if emp_id in employees:
        print("1. Update Name\n2. Update Age\n3. Update Department")
        choice = input("Choose the detail to update (1/2/3): ")

        if choice == "1":
            while True:
                name = input("Enter new name: ")
                if name.isalpha():
                    employees[emp_id]["name"] = name
                    break
                else:
                    print("Invalid name. Name should contain only alphabets.")
        
        elif choice == "2":
            while True:
                try:
                    age = int(input("Enter new age: "))
                    if age > 0:
                        employees[emp_id]["age"] = age
                        break
                    else:
                        print("Age must be a positive integer.")
                except ValueError:
                    print("Invalid input. Please enter a valid age.")
        
        elif choice == "3":
            while True:
                department = input("Enter new department: ")
                if department.isalpha():
                    employees[emp_id]["department"] = department
                    break
                else:
                    print("Invalid department. Department should contain only alphabets.")
        
        print(f"Employee with ID {emp_id} updated successfully.")
    else:
        print("Employee ID not found.")
def search_employee():
    search_type = input("Search by:\n1. Employee ID\n2. Name\nChoose (1/2): ")
    
    if search_type == "1":
        emp_id = int(input("Enter Employee ID: "))
        if emp_id in employees:
            emp = employees[emp_id]
            print(f"Employee Found - ID: {emp_id}, Name: {emp['name']}, Age: {emp['age']}, Department: {emp['department']}")
        else:
            print("Employee ID not found.")
    
    elif search_type == "2":
        name = input("Enter Name: ").lower()
        found = False
        for emp_id, details in employees.items():
            if details["name"].lower() == name:
                print(f"Employee Found - ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")
                found = True
        if not found:
            print("No employee found with the given name.")

def sort_employees():
    sort_by = input("Sort by:\n1. Name\n2. Age\n3. Department\nChoose (1/2/3): ")
    
    if sort_by == "1":
        sorted_employees = sorted(employees.items(), key=lambda x: x[1]['name'])
    elif sort_by == "2":
        sorted_employees = sorted(employees.items(), key=lambda x: x[1]['age'])
    elif sort_by == "3":
        sorted_employees = sorted(employees.items(), key=lambda x: x[1]['department'])
    
    print("\nSorted Employees:")
    for emp_id, details in sorted_employees:
        print(f"ID: {emp_id}, Name: {details['name']}, Age: {details['age']}, Department: {details['department']}")
def menu():
    while True:
        print("\n--- Employee Management System ---")
        print("1. Add a New Employee")
        print("2. Remove an Employee")
        print("3. Update Employee Details")
        print("4. Search Employees")
        print("5. Sort Employees")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            add_employee()
        elif choice == "2":
            remove_employee()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            search_employee()
        elif choice == "5":
            sort_employees()
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
menu()
