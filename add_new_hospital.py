from core.db.db import db
def add_new_hospital(list_of_data, lista_of_planes):
    hospital_name = list_of_data[0]
    phone = list_of_data[1]
    address = list_of_data[2]
    email = list_of_data[3]
    website = list_of_data[4]
    db(f'''INSERT INTO hospital (H_name, phone, address, email, website) VALUES("{hospital_name}", "{phone}", "{address}", "{email}", "{website}"); ''')
    H_id = db(f"""SELECT H_id from hospital WHERE H_name = '{hospital_name}'""")
    for my_plane in lista_of_planes:
      db(f'''INSERT INTO hospital_planes VALUES({H_id[0][0]}, {my_plane}); ''')
    return "successfuly"


# add_new_hospital(["almenshamwy", "002010457118", "algeesh st", "almenshawy@hospital.com", "www.almenshawy.com"],[1, 2])