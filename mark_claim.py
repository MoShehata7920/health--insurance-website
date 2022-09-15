from core.db.db import db


#if claim accepted it'll be true if not it will be false

def mark_claim(true_or_false, IC_id):
    db(f'''update insurance_claim set `status` = {true_or_false} where IC_id = {IC_id};''')
