import tkinter as tk

#import sqlite3 as sq

from uuid import uuid4

from datetime import datetime

from db_requests import *

from tkinter.messagebox import *

initial_connect_with_db()


class Testing:
    pat_names_list = []
    delete_list = []

# Import languages funktions

    def imp_rus(self):
        """import Russian"""
        def inner():
            from languages import lrus as lang
            self.destr_menu1()
            return lang
        self.lang = inner()
        self.make()

    def imp_ukr(self):
        """import Ukrainian"""
        def inner():
            from languages import lukr as lang
            self.destr_menu1()
            return lang
        self.lang = inner()
        self.make()

    def imp_eng(self):
        """import English"""
        def inner():
            from languages import leng as lang
            self.destr_menu1()
            return lang
        self.lang = inner()
        self.make()

# Create-funktions

    def create(self):
        """init the window"""
        self.win = tk.Tk()
        self.win.title("Triage")
        self.win.geometry("600x500")
        self.logo = tk.PhotoImage(file="images/red_cross.png")
        self.win.iconphoto(False, self.logo)
        self.win.config(bg="lightgreen")


    def first_menu(self):
        """Create menu 'Choose the language'"""
        self.lang_choice = tk.Label(self.win, text="Chose the option", bg="lightgreen", fg="darkgreen", font=("Arial", 14, "bold"),
                               pady=10)
        self.lang_choice.grid(row=1, column=1, columnspan=3, stick="we")

        self.ukr = tk.Button(self.win, text="Ukrainian", command=self.imp_ukr)
        self.rus = tk.Button(self.win, text="Russian", command=self.imp_rus)
        self.eng = tk.Button(self.win, text="English", command=self.imp_eng)

        self.ukr.grid(row=2, column=1, stick="we", padx=5, pady=5)
        self.eng.grid(row=2, column=2, stick="we", padx=5, pady=5)
        self.rus.grid(row=2, column=3, stick="we", padx=5, pady=5)

        self.win.grid_columnconfigure(0, minsize=80)
        self.win.grid_columnconfigure(1, minsize=150)
        self.win.grid_columnconfigure(2, minsize=150)
        self.win.grid_columnconfigure(3, minsize=150)

        self.win.grid_rowconfigure(0, minsize=70)
        self.win.grid_rowconfigure(1, minsize=70)
        self.win.grid_rowconfigure(2, minsize=70)

    def db_menu(self):
        """Create menu connecting with data base"""
        self.destr_menu2()

        self.print_question(self.lang.menu1, 0, 1, 1)

        self.watch_patients_list = tk.Button(self.win, text=self.lang.view, font=("Arial", 14), command=self.select_patients)
        self.find_the_patient = tk.Button(self.win, text=self.lang.find_info, font=("Arial", 14), command=self.select_all)

        self.watch_patients_list.grid(row=2, column=1, stick="wens", padx=5, pady=5)
        self.find_the_patient.grid(row=3, column=1, stick="wens", padx=5, pady=5)


        self.previous_menu_in_db = tk.Button(self.win, text=self.lang.pr_menu, font=("Arial", 14),
                                               command=self.prev_menu_from_db)
        self.previous_menu_in_db.grid(row=4, column=1, stick="wens", padx=5, pady=5)

        self.win.grid_columnconfigure(0, minsize=90)
        self.win.grid_columnconfigure(1, minsize=450)

        self.win.grid_rowconfigure(0, minsize=80)
        self.win.grid_rowconfigure(1, minsize=50)
        self.win.grid_rowconfigure(2, minsize=50)
        self.win.grid_rowconfigure(3, minsize=50)
        self.win.grid_rowconfigure(4, minsize=50)

    def make_write_in_db(self):
        """Create first button in main menu"""
        self.write_in_db = tk.Button(self.win, text=self.lang.t_w_db, font=("Arial", 14),
                                command=self.instruct)
        self.write_in_db.grid(row=2, column=1, stick="wens", padx=5, pady=5)

    def make_quick_test(self):
        """Create second button in main menu"""
        self.quick_test = tk.Button(self.win, text=self.lang.t_itself, font=("Arial", 14),
                                    command=self.test_beggining)
        self.quick_test.grid(row=3, column=1, stick="wens", padx=5, pady=5)

    def make_watch_db(self):
        """Create third button in main menu"""
        self.watch_db = tk.Button(self.win, text=self.lang.db_menu, font=("Arial", 14), command=self.db_menu)
        self.watch_db.grid(row=4, column=1, stick="wens", padx=5, pady=5)

    def prev_menu1(self):
        """Destroy  for returning to the main menu"""
        self.destr_menu3()
        self.destr_menu2()
        self.make()

    def prev_menu_in_test(self):
        """Destroy all in test questions for returning to the main menu. Create main menu"""
        self.destr_test()
        self.make()

    def prev_menu_from_db(self):
        """Destroy all in data menu for returning to the main menu. Create main menu"""
        self.destr_db_menu()
        self.make()

    def make(self):
        """Create main menu"""
        self.print_question(self.lang.menu1 , 1, 1, 1)
        self.make_write_in_db()
        self.make_quick_test()
        self.make_watch_db()

        self.win.grid_columnconfigure(0, minsize=80)
        self.win.grid_columnconfigure(1, minsize=450)

        self.win.grid_rowconfigure(0, minsize=80)
        self.win.grid_rowconfigure(1, minsize=50)
        self.win.grid_rowconfigure(2, minsize=50)
        self.win.grid_rowconfigure(3, minsize=50)
        self.win.grid_rowconfigure(4, minsize=50)

    def print_question(self, text, rown, columnn, columnspann):
        """Create text in different menu"""
        self.question = tk.Label(self.win, text=text, bg="lightgreen",
                            fg="darkgreen", font=("Arial", 12, "bold"), padx=15, pady=5)#, anchor="w")
        self.question.grid(row=rown, column=columnn, columnspan=columnspann)#, stick="we", padx=15, pady=15)

    def create_yes_no(self, funk1, funk2):
        """Create buttons 'yes' and 'no' in test"""
        self.image_yes = tk.PhotoImage(file="images/yes_green4.png")
        self.image_yes = self.image_yes.subsample(17, 17)
        self.button_yes = tk.Button(self.win, height=100, width=100, image=self.image_yes, padx=10, pady=10, command=funk1,
                               bg="lightgreen", activebackground="lightgreen", bd=0)
        self.button_yes.grid(row=1, column=1)

        self.image_no = tk.PhotoImage(file="images/red_cross5.png")
        self.image_no = self.image_no.subsample(5, 5)
        self.button_no = tk.Button(self.win, height=100, width=100, image=self.image_no, padx=10, command=funk2,
                              pady=10, bg="lightgreen", activebackground="lightgreen", bd=0)
        self.button_no.grid(row=1, column=3)

    def prev_btn_in_test(self):
        """Create button 'return to the previous menu' in test"""
        self.previous_menu_in_test = tk.Button(self.win, text=self.lang.pr_menu, command=self.prev_menu_in_test)
        self.previous_menu_in_test.grid(row=2, column=2, stick="wens", padx=10, pady=30)

        self.win.grid_columnconfigure(0, minsize=100)
        self.win.grid_columnconfigure(1, minsize=100)
        self.win.grid_rowconfigure(0, minsize=100)

    def instruct(self):
        """Create menu to write data of the patient"""
        self.destr_menu2()
        self.instruction = tk.Label(self.win, text=self.lang.text_in_db, bg="lightgreen",
                               fg="darkgreen", font=("Arial", 14, "bold"), padx=15, pady=5, anchor="w")
        self.paragraph1 = tk.Label(self.win, text=self.lang.full_name, bg="lightgreen", fg="darkgreen", font=("Arial", 11, "bold"),
                              padx=10, pady=5, anchor="w")
        self.paragraph2 = tk.Label(self.win, text=self.lang.age_in_db, bg="lightgreen", fg="darkgreen", font=("Arial", 11, "bold"),
                              padx=10, pady=5, anchor="w")
        self.paragraph3 = tk.Label(self.win, text=self.lang.obj, bg="lightgreen", fg="darkgreen",
                              font=("Arial", 11, "bold"),
                              padx=10, pady=5, anchor="w")
        self.paragraph4 = tk.Label(self.win, text=self.lang.pulse_in_db, bg="lightgreen", fg="darkgreen", font=("Arial", 11, "bold"),
                              padx=10, pady=5, anchor="w")
        self.paragraph5 = tk.Label(self.win, text=self.lang.breath_in_db, bg="lightgreen", fg="darkgreen", font=("Arial", 11, "bold"),
                              padx=10, pady=5, anchor="w")
        self.paragraph6 = tk.Label(self.win, text=self.lang.pressure, bg="lightgreen", fg="darkgreen", font=("Arial", 11, "bold"),
                              padx=10, pady=5, anchor="w")
        self.paragraph7 = tk.Label(self.win, text=self.lang.consciousness_in_db, bg="lightgreen", fg="darkgreen", font=("Arial", 11, "bold"),
                              padx=10, pady=5, anchor="w")
        self.paragraph8 = tk.Label(self.win, text=self.lang.concentration, bg="lightgreen", fg="darkgreen", font=("Arial", 11, "bold"),
                              padx=10, pady=5, anchor="w")

        self.instruction.grid(row=0, column=0, columnspan=3, stick="we")
        self.paragraph1.grid(row=1, column=0, stick="we")
        self.paragraph2.grid(row=2, column=0, stick="we")
        self.paragraph3.grid(row=3, column=0, stick="we")
        self.paragraph4.grid(row=4, column=0, stick="we")
        self.paragraph5.grid(row=5, column=0, stick="we")
        self.paragraph6.grid(row=6, column=0, stick="we")
        self.paragraph7.grid(row=7, column=0, stick="we")
        self.paragraph8.grid(row=8, column=0, stick="we")

        self.item1 = tk.Entry(self.win)
        self.item2 = tk.Entry(self.win)
        self.item3 = tk.Entry(self.win)
        self.item4 = tk.Entry(self.win)
        self.item5 = tk.Entry(self.win)
        self.item6 = tk.Entry(self.win)
        self.item7 = tk.Entry(self.win)
        self.item8 = tk.Entry(self.win)

        self.item1.grid(row=1, column=1, pady=5, stick="wens")
        self.item2.grid(row=2, column=1, pady=5, stick="wens")
        self.item3.grid(row=3, column=1, pady=5, stick="wens")
        self.item4.grid(row=4, column=1, pady=5, stick="wens")
        self.item5.grid(row=5, column=1, pady=5, stick="wens")
        self.item6.grid(row=6, column=1, pady=5, stick="wens")
        self.item7.grid(row=7, column=1, pady=5, stick="wens")
        self.item8.grid(row=8, column=1, pady=5, stick="wens")

        self.previous_menu = tk.Button(self.win, text=self.lang.pr_menu, command=self.prev_menu1)
        self.submit = tk.Button(self.win, text=self.lang.submit, command=self.submit_data)

        self.previous_menu.grid(row=9, column=0, stick="wens", padx=10, pady=5)
        self.submit.grid(row=9, column=1, stick="wens", pady=5)

        self.win.grid_columnconfigure(0, minsize=80)
        self.win.grid_columnconfigure(1, minsize=360)
        for i in range(9):
            self.win.grid_rowconfigure(i, minsize=45)
        self.win.grid_rowconfigure(9, minsize=50)

    def return_db_menu(self):
        self.destr_name_print()
        self.db_menu()

    def return_from_list_pations_names(self):
        for i in self.pat_names_list:
            i.destroy()
        self.return_menu.destroy()
        self.db_menu()

#Db_connect-funktions

    def submit_data(self):
        full_name = self.item1.get()
        age = self.item2.get()
        if not full_name or not age:
            showinfo(self.lang.warning, self.lang.warning_field_required)
        else:
            obj_status = self.item3.get()
            pulse = self.item4.get()
            breathing_rate = self.item5.get()
            blood_preassure = self.item6.get()
            consciousness = self.item7.get()
            paO2 = self.item8.get()
            len_list = []
            for num in [full_name, age, obj_status, pulse, blood_preassure, consciousness, paO2]:
                if len(num) > 30:
                    len_list.append(False)
                else:
                    len_list.append(True)
            if not all(len_list):
                    showinfo(self.lang.warning, self.lang.warning_too_long)
            else:
                self.destr_menu3()
                self.test_beggining()
                id = str(uuid4())
                date_of_survey = str(datetime.now())[0:-6]
                patient = {
                    'full_name': full_name,
                    'age': age,
                    'obj_status': obj_status,
                    'pulse': pulse,
                    'breathing_rate': breathing_rate,
                    'blood_preassure': blood_preassure,
                    'consciousness': consciousness,
                    'paO2': paO2,
                    'date_of_survey': date_of_survey,
                    'id': id
                }
                create_patient(patient)


    def select_all(self):
        """Menu to enter patient's name to find information"""
        self.destr_db_menu()
        self.del_pat_name_age_list = []
        self.print_question(self.lang.pr_name, 1, 1, 1)
        self.del_pat_name_age_list.append(self.question)
        self.print_question(self.lang.pr_age, 3, 1, 1)
        self.del_pat_name_age_list.append(self.question)
        self.pat_name = tk.Entry(self.win)
        self.pat_name.grid(row=2, column=1, pady=5, stick="wens")
        self.pat_age = tk.Entry(self.win)
        self.pat_age.grid(row=4, column=1, pady=5, stick="wens")
        self.return_prev_menu = tk.Button(self.win, text=self.lang.pr_menu1, font=("Arial", 14), command=self.return_db_menu)
        self.return_prev_menu.grid(row=5, column=1, stick="wens", padx=5, pady=5)

        self.view_info = tk.Button(self.win, text=self.lang.show_info, font=("Arial", 14), command=self.select_info)
        self.view_info.grid(row=6, column=1, stick="wens", padx=5, pady=5)

        self.win.grid_columnconfigure(0, minsize=80)
        self.win.grid_columnconfigure(1, minsize=450)

        self.win.grid_rowconfigure(0, minsize=80)
        self.win.grid_rowconfigure(1, minsize=50)
        self.win.grid_rowconfigure(2, minsize=50)
        self.win.grid_rowconfigure(3, minsize=50)
        self.win.grid_rowconfigure(4, minsize=50)

    def select_info(self):
        """Show patients information in tab"""
        name_from_entry = self.pat_name.get()
        age_from_entry = self.pat_age.get()
        id_info = select_patient_info_from_db(name_from_entry, age_from_entry)
        if id_info:
            self.destr_name_print()
            information = select_patient_by_id(id_info)
            self.print_question(name_from_entry, 0, 0, 1)
            self.delete_list.append(self.question)
            age_pat = select_patient_by_name(name_from_entry)
            self.print_question(age_pat[0][0], 0, 1, 1)
            self.delete_list.append(self.question)
            list_tab = ["time", "objective_status", "pulse", "breathing_rate",
                "pressure", "consciousness", "concentration"]

            for i in list_tab:
                ro = 1
                for i in list_tab:
                    self.print_question(i, ro, 0, 1)
                    self.delete_list.append(self.question)
                    ro += 1
            col = 1

            for row in information:
                ro = 1
                for word in row[2::]:
                    self.print_question(word, ro, col, 1)
                    self.delete_list.append(self.question)
                    ro += 1
                col += 1
            self.return_menu = tk.Button(self.win, text=self.lang.pr_menu, font=("Arial", 14), command=self.delete_pat_info_tab)
            self.return_menu.grid(row=9, column=1, columnspan=1, stick="wens", padx=5, pady=5)

            self.win.grid_columnconfigure(0, minsize=80)
            self.win.grid_columnconfigure(1, minsize=50)
        else:
            showinfo(self.lang.warning, self.lang.no_pat)

    def select_patients(self):
        self.destr_db_menu()
        try:
            self.destr_menu3()
            self.destr_menu2()
            self.destr_test1()
            self.destr_db_menu()
        except AttributeError:
            pass
        self.print_question(self.lang.menu1, 0, 1, 1)
        self.pat_names_list.append(self.question)
        text1 = select_name_age()
        e = 0
        for word in text1:
            name_age = " ".join(word)
            self.print_question(name_age, e, 0, 1)

            self.pat_names_list.append(self.question)
            self.deleter = tk.Button(self.win, text=self.lang.delete_text, font=("Arial", 12),
                                        command=lambda : self.del_pat(self.question))
            self.pat_names_list.append(self.deleter)
            self.deleter.grid(row=e, column=1, stick="wens", padx=8, pady=8)
            e += 1
        self.return_menu = tk.Button(self.win, text=self.lang.pr_menu,
                                         font=("Arial", 14), command=self.return_from_list_pations_names)
        self.return_menu.grid(row=e, column=1, columnspan=1, stick="wens", padx=5, pady=5)
        self.win.grid_columnconfigure(0, minsize=200)
        self.win.grid_columnconfigure(1, minsize=100)

        self.win.grid_rowconfigure(0, minsize=50)
        self.win.grid_rowconfigure(1, minsize=50)
        self.win.grid_rowconfigure(2, minsize=50)
        self.win.grid_rowconfigure(3, minsize=50)
        self.win.grid_rowconfigure(4, minsize=50)

#Destroy-funktions

    def delete_pat_info_tab(self):
        self.destr_name_print()
        for i in self.delete_list:
            i.destroy()
            self.return_menu.destroy()
            self.db_menu()

    def destr_name_print(self) :
        """Destroy Label, Entry and returning-button in patient's name-entry-menu"""
        for i in self.del_pat_name_age_list:
            i.destroy()
        self.pat_name.destroy()
        self.pat_age.destroy()
        self.return_prev_menu.destroy()
        self.view_info.destroy()

    def del_pat(self, patient):
        ind = patient['text'].rfind(" ")
        name_text = patient['text'][:ind]
        age_text = patient['text'][(ind+1)::]
        select_and_delete_patient(name_text, age_text)
        self.pat_names_list.remove(patient)
        patient.destroy()
        self.deleter.destroy()

    def destr_menu1(self):
        """Destroy menu of chosing language"""
        self.lang_choice.destroy()
        self.ukr.destroy()
        self.eng.destroy()
        self.rus.destroy()

    def destr_menu2(self):
        """Destroy main menu"""
        self.question.destroy()
        self.write_in_db.destroy()
        self.quick_test.destroy()
        self.watch_db.destroy()

    def destr_menu3(self):
        """Destroy menu of writing data"""
        self.instruction.destroy()
        self.paragraph1.destroy()
        self.paragraph2.destroy()
        self.paragraph3.destroy()
        self.paragraph4.destroy()
        self.paragraph5.destroy()
        self.paragraph6.destroy()
        self.paragraph7.destroy()
        self.paragraph8.destroy()
        self.item1.destroy()
        self.item2.destroy()
        self.item3.destroy()
        self.item4.destroy()
        self.item5.destroy()
        self.item6.destroy()
        self.item7.destroy()
        self.item8.destroy()
        self.previous_menu.destroy()
        self.submit.destroy()

    def destr_db_menu(self):
        self.question.destroy()
        self.previous_menu_in_db.destroy()
        self.watch_patients_list.destroy()
        self.find_the_patient.destroy()

    def destr_test(self):
        """Destroy all in test questions for returning to the main menu"""
        self.question.destroy()
        self.previous_menu_in_test.destroy()
        self.button_yes.destroy()
        self.button_no.destroy()

    def destr_test1(self):
        """Destroy all (exept button 'return to prev.menu) in test questions for going to the next question"""
        self.question.destroy()
        self.button_yes.destroy()
        self.button_no.destroy()

# Test-funktions

    def test_beggining(self):
        """The begining of test. First question"""
        self.destr_menu2()
        self.print_question(self.lang.stand, 0, 1, 3)
        self.create_yes_no(self.green, self.no)
        self.prev_btn_in_test()

    def green(self):
        self.destr_test1()
        self.print_question(self.lang.g, 0, 1, 3)
        return self.lang.g

    def yellow(self):
        self.destr_test1()
        self.print_question(self.lang.y, 0, 1, 3)

    def red(self):
        self.destr_test1()
        self.print_question(self.lang.r, 0, 1, 3)

    def black(self):
        self.destr_test1()
        self.print_question(self.lang.b, 0, 1, 3)

    def yes4(self):
        self.destr_test1()
        self.print_question(self.lang.breath3, 0, 1, 3)
        self.create_yes_no(self.red, self.black)

    def no3(self):
        self.destr_test1()
        self.print_question(self.lang.age, 0, 1, 3)
        self.create_yes_no(self.yes4, self.black)

    def yes3(self):
        self.destr_test1()
        self.print_question(self.lang.conscious, 0, 1, 3)
        self.create_yes_no(self.yellow, self.red)

    def no2(self):
        self.destr_test1()
        self.print_question(self.lang.pulse, 0, 1, 3)
        self.create_yes_no(self.yes3, self.red)

    def yes1(self):
        self.destr_test1()
        self.print_question(self.lang.breathing_rate, 0, 1, 3)
        self.create_yes_no(self.red, self.no2)

    def no1(self):
        self.destr_test1()
        self.print_question(self.lang.breath, 0, 1, 3)
        self.create_yes_no(self.red, self.no3)

    def no(self):
        self.destr_test1()
        self.print_question(self.lang.airways, 0, 1, 3)
        self.create_yes_no(self.yes1, self.no1)

    def start(self):
        self.win.mainloop()


exam = Testing()
exam.create()
exam.first_menu()
exam.start()
