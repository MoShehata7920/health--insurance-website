from db.db import db

def add_payment(list_of_data):
    amount = list_of_data[0]
    date = list_of_data[1]
    customer = list_of_data[2]


    db(f'''INSERT INTO dependant (amount, date, Customer) VALUES({amount}, "{date}", {customer}); ''')
    return "successfuly"

