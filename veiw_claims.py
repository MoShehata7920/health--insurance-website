from core.db.db import db

def get_all_claims():
    return db("select insurance_claim.IC_id, insurance_claim.amount ,insurance_claim.`status`, Customers.`name` from insurance_claim inner join Customers on mainly_for = C_id;")

def get_uresolved_claims():
    return db("select insurance_claim.IC_id, insurance_claim.amount, insurance_claim.`status`, Customers.`name` from insurance_claim inner join Customers on mainly_for = C_id where insurance_claim.`status` is null;")


# print(get_all_claims())
# print("--------------------------------------------------------------------")
# print(get_uresolved_claims())