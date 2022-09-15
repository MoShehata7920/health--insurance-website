from mysql.connector import connect, Error


def db(sqlquery):
    myhost = 'db4free.net'
    mydatabase = ' healthinsurance'
    myuser = 'mohamedalnawagy'
    mypass = 'e374baa6'

    con = connect(host = myhost,
                  database = mydatabase,
                  user = myuser,
                  password = mypass)
    cur = con.cursor()
    cur.execute("USE healthinsurance;")
    try:
        cur.execute(sqlquery)
    except Error as e:
        print("Eception", e)
    # try:
    #     records = cur.fetchall()
    # except:
    #     records = 0
    records = cur.fetchall()
    con.commit()
    con.close()
    return records