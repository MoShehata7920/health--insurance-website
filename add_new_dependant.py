from core.db.db import db
from get_customer_id import get_customer_id
from datetime import date


def add_new_dependant(main_Customer_id,list_of_data):
    name = list_of_data[0]
    birth_date = list_of_data[1]
    plane = list_of_data[2]
    main_id = main_Customer_id
    price = db(f"select Price from plane where P_id = {plane}")[0][0]
    today = date.today() 
    db(f'''INSERT INTO dependant (`name`, birth_date, plane, belongs_to) VALUES("{name}", "{birth_date}", {plane}, {main_id}); ''')

    db(f'''INSERT INTO Payments (amount, date, Customer) VALUES ({price},"{today}", {main_id});''')
    return "successfuly"

# add_new_dependant("30001602421037",["ali", "2005-5-17", 2] )
# add_new_dependant("01234567891234",["asmaa", "2007-6-12", 1] )