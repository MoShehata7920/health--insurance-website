from core.db.db import db

def get_claim_details(IC_id):
    data = (db(f"SELECT * FROM insurance_claim WHERE IC_id = {IC_id}"))
    id = data[0][0]
    amount = data[0][1]
    date = data[0][2]
    description = data[0][3]
    status = data[0][4]
    mainly_for_id = data[0][5]
    mainly_for_name = db(f'''SELECT `name` from Customers WHERE C_id = {mainly_for_id};''')[0][0]
    dependent_id = data[0][6]
    try:
        dependent_name = db(f'''SELECT `name` FROM dependant WHERE D_id = {dependent_id};''')[0][0]
    except:
        dependent_name = None
    hospital_id = data[0][7]
    hospital_name = db(f'''SELECT H_name FROM hospital WHERE H_id = {hospital_id}''')[0][0]
    return[id, amount, date, description, status, mainly_for_id, mainly_for_name, dependent_name, hospital_name]


# print(get_claim_details(2))