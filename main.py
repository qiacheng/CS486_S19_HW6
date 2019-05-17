import psycopg2 as pgdb

def main():
    dataB = "s19wdb21"
    hostname= "tanto.cs.pdx.edu"
    username = input("username>")
    password = input("password>")
    connection = pgdb.connect(host=hostname, user=username, password=password, sslmode='require')
    db = connection.cursor();

    query = "SELECT * FROM spy.Agent"

    db.execute(query)

    rows = db.fetchall()
    
    for row in rows:
        print(row)

    db.close()
    connection.close()

main()

