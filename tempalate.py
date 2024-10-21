import view

# User input
user_input = input("Enter F to fetch the data, S to save the data, U to update the data, D to delete the data: ").upper()

if user_input == "F":
    data = view.get_data()
    for row in data:
        print(row)

elif user_input == "S":
    emp_id = int(input("Enter your ID: "))
    emp_name = input("Enter your name: ")
    designation = input("Enter your designation: ")
    salary = float(input("Enter your salary: "))
    view.save_data(emp_id, emp_name, designation, salary)
    data = view.get_data()
    print(data)

elif user_input == "U":
    emp_id = int(input("Enter your ID: "))
    emp_name = input("Enter your name: ")
    designation = input("Enter your designation: ")
    salary = float(input("Enter your salary: "))
    view.update_data(emp_id, emp_name, designation, salary)
    data = view.get_data()
    print(data)

elif user_input == "D":
    emp_id = int(input("Enter your ID: "))
    view.delete_data(emp_id)
    data = view.get_data()
    print(data)
