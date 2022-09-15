from core.db.db import db

def get_list_of_customers():
    list_of_customers = db("SELECT * FROM Customers")
    return(list_of_customers)

