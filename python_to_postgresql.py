import psycopg2 #import connection driver #change #another change #yet another change

hostname = 'localhost'
database = 'DataBrains'
username = 'postgres'
pwd = 'MLN@sql@7'
port_id = 5432

conn = None
cur = None

try:
    conn = psycopg2.connect(
                host = hostname,
                dbname = database,
                user = username,
                password = pwd,
                port = port_id)
    
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS employee')
    create_script = '''CREATE TABLE IF NOT EXISTS employee (
                            id      int PRIMARY KEY,
                            name    varchar(40) NOT NULL,
                            salary  int,
                            dept_id varchar(30))'''

    cur.execute(create_script)
 
    insert_script = 'INSERT INTO employee(id, name, salary, dept_id) VALUES (%s, %s, %s, %s)'
    insert_values = [(1, 'James', 12000, 'D1'), (2, 'Kamames', 15000, 'D2'), (3, 'Dane', 20000, 'D3')]
    
    for record in insert_values:
        cur.execute(insert_script, record)

    cur.execute('SELECT * FROM employee')
    
    for record in cur.fetchall():
        print(record)

    conn.commit()
   
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()

print("Completed")

