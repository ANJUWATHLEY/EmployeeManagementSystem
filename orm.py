import pyodbc

# Function to establish a connection
def getConnection():
    connection = r"Driver={MySQL ODBC 9.0 Unicode Driver};Server=localhost;Database=emspython;UID=root;PWD=W7301@jqir#;"
    connect = pyodbc.connect(connection)
    cursor = connect.cursor()  # Communication channel
    return cursor

# ORM model class
class Model:
    def fetch(self):
        cursor = getConnection()
        cursor.execute("SELECT * FROM employee")  # Fetch all rows from employee table
        rows = cursor.fetchall()
        return rows

    def save(self):
        cursor = getConnection()
        # Insert a new row into the employee table
        cursor.execute(f"INSERT INTO employee VALUES ({self.id}, '{self.name}', '{self.designation}', {self.salary})")
        cursor.commit()

    def update(self):
        cursor = getConnection()
        cursor.execute(f"UPDATE employee SET emp_name='{self.name}', designation='{self.designation}', salary={self.salary} WHERE emp_id={self.id}")
        cursor.commit()

    def delete(self):
        cursor = getConnection()  # Corrected the method call
        cursor.execute(f"DELETE FROM employee WHERE emp_id={self.id}")
        cursor.commit()
