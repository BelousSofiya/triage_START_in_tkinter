import sqlite3 as sq
from uuid import uuid4

def initial_connect_with_db():
    with sq.connect("testing.db") as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS patients(
            id_pat VARCHAR(100) PRIMARY KEY,
            full_name VARCHAR(30),
            age VARCHAR(30)
            )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS patients_info(
            id_in_tab VARCHAR(100) PRIMARY KEY,
            id_pat VARCHAR(100), 
            time VARCHAR(30),
            objective_status VARCHAR(30) DEFAULT NULL,
            pulse VARCHAR(30) DEFAULT NULL,
            breathing_rate VARCHAR(30) DEFAULT NULL,
            pressure VARCHAR(30) DEFAULT NULL,
            consciousness VARCHAR(30) DEFAULT NULL,
            concentration VARCHAR(30) DEFAULT NULL
            )""")

def create_patient(patient):
    with sq.connect("testing.db") as cons:
        curs = cons.cursor()
        curs.execute(f"""SELECT id_pat FROM patients WHERE full_name == '{patient['full_name']}' and age == '{patient['age']}'""")
        j = curs.fetchall()
        if j:
            curs.execute(f"""INSERT INTO patients_info 
                        (id_in_tab, id_pat, time, objective_status, pulse, breathing_rate, 
                        pressure, consciousness, concentration) 
                        VALUES("{id}", "{j[0][0]}", "{patient['date_of_survey']}", "{patient['obj_status']}", 
                               "{patient['pulse']}", "{patient['breathing_rate']}", "{patient['blood_preassure']}", 
                               "{patient['consciousness']}", "{patient['paO2']}")""")
        else:
            j = str(uuid4())
            curs.execute(f"""INSERT INTO patients 
                (id_pat, full_name, age)
                VALUES("{j}", "{patient['full_name']}", "{patient['age']}")""")
            curs.execute(f"""INSERT INTO patients_info 
                (id_in_tab, id_pat, time, objective_status, pulse, breathing_rate, 
                pressure, consciousness, concentration) 
                VALUES("{id}", "{j}", "{patient['date_of_survey']}", "{patient['obj_status']}", "{patient['pulse']}", 
                       "{patient['breathing_rate']}", "{patient['blood_preassure']}", "{patient['consciousness']}", 
                       "{patient['paO2']}")""")
        curs.close()

def select_patient_info_from_db(name, age):
    with sq.connect("testing.db") as cons:
        curs = cons.cursor()
        curs.execute(
            f"""SELECT id_pat FROM patients WHERE full_name == '{name}' AND age == '{age}'""")
        return curs.fetchall()

def select_patient_by_id(info):
    with sq.connect("testing.db") as cons:
        curs = cons.cursor()
        curs.execute(f"""SELECT * FROM patients_info WHERE id_pat == '{info[0][0]}'""")
        return curs.fetchall()

def select_patient_by_name(name):
    with sq.connect("testing.db") as cons:
        curs = cons.cursor()
        curs.execute(f"""SELECT age FROM patients WHERE full_name == '{name}'""")
        return curs.fetchall()

def select_name_age():
    with sq.connect("testing.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT full_name, age FROM patients""")
        return cur.fetchall()

def select_and_delete_patient(name, age):
    with sq.connect("testing.db") as con:
        cur = con.cursor()
        cur.execute(f"""SELECT id_pat FROM patients WHERE full_name=='{name}' AND age = '{age}'""")
        key_delete = cur.fetchall()
        cur.execute(f"""DELETE FROM patients_info WHERE id_pat=='{key_delete[0][0]}'""")
        cur.execute(f"""DELETE FROM patients WHERE full_name=='{name}' AND age = '{age}'""")
        cur.close()
