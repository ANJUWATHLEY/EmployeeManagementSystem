from models import Employee

def get_data():
    empobj = Employee()
    rows = empobj.fetch()
    return rows

def save_data(emp_id, emp_name, designation, salary):
    empobj = Employee(emp_id, emp_name, designation, salary)
    empobj.save()

def update_data(emp_id, emp_name, designation, salary):
    empobj = Employee(emp_id, emp_name, designation, salary)
    empobj.update()

def delete_data(emp_id):
    empobj = Employee(emp_id)
    empobj.delete()
