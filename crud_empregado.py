def add_empregado(conn, empregado):
    sql = ''' INSERT INTO Employee (Name, Birthday, Salary, Department)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, empregado)
    conn.commit()
    return cur.lastrowid

def read_empregado(conn, employee_id):
    sql = ''' SELECT * FROM Employee WHERE EmployeeID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (employee_id,))
    empregado = cur.fetchone()
    return empregado

def update_empregado(conn, empregado):
    sql = ''' UPDATE Employee
              SET Name = ?, Birthday = ?, Salary = ?, Department = ?, JobID = ?
              WHERE EmployeeID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (empregado['Name'], empregado['Birthday'], empregado['Salary'], empregado['Department'], empregado['JobID'], empregado['EmployeeID']))
    conn.commit()
    
def delete_empregado(conn, employee_id):
    sql = ''' DELETE FROM Employee WHERE EmployeeID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (employee_id,))
    conn.commit()
