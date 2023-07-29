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

def create_patient(full_name, age, obj_status, pulse, breathing_rate, blood_preassure, consciousness, paO2, date_of_survey, id):
    with sq.connect("testing.db") as cons:
        curs = cons.cursor()
        curs.execute(f"""SELECT id_pat FROM patients WHERE full_name == '{full_name}' and age == '{age}'""")
        j = curs.fetchall()
        if j:
            curs.execute(f"""INSERT INTO patients_info 
                        (id_in_tab, id_pat, time, objective_status, pulse, breathing_rate, 
                        pressure, consciousness, concentration) 
                        VALUES("{id}", "{j[0][0]}", "{date_of_survey}", "{obj_status}", "{pulse}", "{breathing_rate}", "{blood_preassure}", "{consciousness}", "{paO2}")""")
        else:
            j = str(uuid4())
            curs.execute(f"""INSERT INTO patients 
                (id_pat, full_name, age)
                VALUES("{j}", "{full_name}", "{age}")""")
            curs.execute(f"""INSERT INTO patients_info 
                (id_in_tab, id_pat, time, objective_status, pulse, breathing_rate, 
                pressure, consciousness, concentration) 
                VALUES("{id}", "{j}", "{date_of_survey}", "{obj_status}", "{pulse}", "{breathing_rate}", "{blood_preassure}", "{consciousness}", "{paO2}")""")
        curs.close()

def select_patient_info_from_db(name_from_entry, age_from_entry):
    with sq.connect("testing.db") as cons:
        curs = cons.cursor()
        curs.execute(
            f"""SELECT id_pat FROM patients WHERE full_name == '{name_from_entry}' AND age == '{age_from_entry}'""")
        return curs.fetchall()

def select_patient_by_id(id_info):
    with sq.connect("testing.db") as cons:
        curs = cons.cursor()
        curs.execute(f"""SELECT * FROM patients_info WHERE id_pat == '{id_info[0][0]}'""")
        return curs.fetchall()

def select_patient_by_name(name_from_entry):
    with sq.connect("testing.db") as cons:
        curs = cons.cursor()
        curs.execute(f"""SELECT age FROM patients WHERE full_name == '{name_from_entry}'""")
        return curs.fetchall()

def select_name_age():
    with sq.connect("testing.db") as con:
        cur = con.cursor()
        cur.execute("""SELECT full_name, age FROM patients""")
        return cur.fetchall()

def select_and_delete_patient(name_text, age_text):
    with sq.connect("testing.db") as con:
        cur = con.cursor()
        cur.execute(f"""SELECT id_pat FROM patients WHERE full_name=='{name_text}' AND age = '{age_text}'""")
        key_delete = cur.fetchall()
        cur.execute(f"""DELETE FROM patients_info WHERE id_pat=='{key_delete[0][0]}'""")
        cur.execute(f"""DELETE FROM patients WHERE full_name=='{name_text}' AND age = '{age_text}'""")
        cur.close()