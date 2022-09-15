from core.db.db import db


def hospitals_on_plane(plane):
    return db(f'''SELECT H_name, phone, address, email, website FROM hospital WHERE H_id IN(SELECT hospital FROM hospital_planes WHERE plane = {plane});''')


