import psycopg2 as pgdb

def main():
    
    hostname= "tanto.cs.pdx.edu"
    username = input("username>")
    password = input("password>")
    dataB = username
    connection = pgdb.connect(host=hostname, user=username, password=password, sslmode='require')
    db = connection.cursor();
    print("1: Default Query")
    print("2: Custom Query")
    print("---------------")
    answer = input("choice: ")
    if answer == '1':
    	query = query = "SELECT * FROM spy.Agent limit 10"
    elif answer == '2':
    	query = input("Enter SQL Query: ")
    else:
        print("invalid input")
        return

    db.execute(query)

    rows = db.fetchall()
    
    for row in rows:
        print(row)

    db.close()
    connection.close()

main()

