from db.db import db

def calculate_expenses(ssn):
    planes = {
        1:1000,
        2:2000,
        3:3000
    }
    main_customer_plane = db(f'''SELECT plane FROM Customers WHERE ssn = "{ssn}"; ''')[0][0] 
    main_customer_fees = planes[main_customer_plane]
    dependentes_plane = db(f'''SELECT plane FROM dependant WHERE belongs_to = "{ssn}"; ''')
    dep_fees = 0
    num_of_dep = len(dependentes_plane)
    for dep_plane in range(num_of_dep):
        p_index = dependentes_plane[dep_plane][0]
        dep_fees += planes[p_index]
    dep_fees = dep_fees *0.8
    return dep_fees + main_customer_fees




# print(calculate_expenses("01234567891234"))
