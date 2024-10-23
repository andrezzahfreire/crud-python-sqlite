
def add_trabalho(conn, project):
    sql = ''' INSERT INTO Job (Name, Description)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project) 
    conn.commit()
    return cur.lastrowid 

def read_trabalho(conn, job_id):
    sql = ''' SELECT * FROM Job WHERE JobID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (job_id,))
    trabalho = cur.fetchone()
    return trabalho


def update_trabalho(conn, trabalho):
    sql = ''' UPDATE Job
              SET Name = ?, Description = ?
              WHERE JobID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (trabalho['Name'], trabalho['Description'], trabalho['JobID']))
    conn.commit()

def delete_trabalho(conn, job_id):
    sql = ''' DELETE FROM Job WHERE JobID = ? '''
    cur = conn.cursor()
    cur.execute(sql, (job_id,))
    conn.commit()