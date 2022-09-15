from core.db.db import db

def get_payments():
    result = db('select Payments.P_id, Payments.amount,Payments.`date`, Payments.`status`, Customers.ssn, Customers.`name`, Customers.phone from Payments inner join Customers on C_id = Customer;')
    return result

def verify_payment(P_id):
    db(f'''update Payments set `status` = true where P_id = {P_id};''')