def add_historico(conn, project):
    sql = ''' INSERT INTO JobHistory (EmployeeID, StartDate, EndDate, Salary, Job)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid

def read_historico(conn, job_history_id):
    sql = ''' SELECT * FROM JobHistory WHERE JobHistoryID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (job_history_id,))
    historico = cur.fetchone()
    return historico


def update_historico(conn, historico):
    sql = ''' UPDATE JobHistory
              SET EmployeeID = ?, StartDate = ?, EndDate = ?, Salary = ?, Job = ?
              WHERE JobHistoryID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (historico['EmployeeID'], historico['StartDate'], historico['EndDate'], historico['Salary'], historico['Job'], historico['JobHistoryID']))
    conn.commit()

def delete_historico(conn, job_history_id):
    sql = ''' DELETE FROM JobHistory WHERE JobHistoryID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (job_history_id,))
    conn.commit()
