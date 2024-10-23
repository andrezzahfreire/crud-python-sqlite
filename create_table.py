import sqlite3

def create_tables():
    sql_statements = [ 
        """CREATE TABLE Job (
                JobID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR(50),
                Description VARCHAR(255)
);""",
        """CREATE TABLE Employee (
                EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name VARCHAR(50),
                Birthday DATE,
                Salary NUMERIC(10,2),
                Department VARCHAR(50),
                JobID INTEGER,
                FOREIGN KEY(JobID) REFERENCES Job(JobID)
);""",
        """CREATE TABLE JobHistory (
                JobHistoryID INTEGER PRIMARY KEY AUTOINCREMENT, 
                EmployeeID INTEGER,
                StartDate DATE,
                EndDate DATE,
                Salary NUMERIC(10,2),
                Job VARCHAR(50),
                FOREIGN KEY(EmployeeID) REFERENCES Employee(EmployeeID)
);"""]


    try:
        with sqlite3.connect('my.db') as conn:
            cursor = conn.cursor()
            for statement in sql_statements:
                cursor.execute(statement)
            
            conn.commit()
    except sqlite3.Error as e:
        print(e)
