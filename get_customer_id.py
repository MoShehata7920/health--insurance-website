from core.db.db import db

def get_customer_id(ssn):
    return db(f''' SELECT C_id FROM Customers where ssn ="{ssn}"; ''')[0][0]


