import tkinter
from tkinter import *
import ttkthemes
import ttkthemes.themed_tk as Tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from PIL import ImageTk,Image
from tkinter import messagebox
import All_Databases as database
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


class MainApp:
    def __init__(self):
        self.loggin_status = False
        self.admin = False

    def start_login(self):
        self.win = Tk.ThemedTk()
        self.win.focus_force()
        self.win.set_theme("arc")
        self.win.title("Second software")
        self.win.geometry("700x650+300+20")
        self.win.resizable(0,0)
        self.win.iconbitmap("pd-icon.ico")
        self.font = ("Courier", 18, "bold")
        self.lab = ttk.Label(self.win,text="Welcome Login or create account here!")
        self.lab.pack(pady=10)
        self.font_global = ("Courier", 16, "bold")
        self.username = ttk.Label(self.win,text="Username")
        self.username.pack(pady=10)
        self.name = StringVar()
        self.user_entry = ttk.Entry(self.win,width=40,textvariable=self.name,font=("Arial",17))
        self.user_entry.pack(pady=10)
        self.pass_1var = StringVar()
        self.pass_ = ttk.Label(self.win, text="Password")

        self.pass_.pack(pady=10)
        self.pass_entry = ttk.Entry(self.win, width=40, textvariable=self.pass_1var, font=("Arial", 17),show="*")
        self.pass_entry.pack(pady=10)
        self.pass_2var = StringVar()

        self.fr = ttk.Frame(self.win)
        self.login_btn = ttk.Button(self.fr,text="LOGIN",width=16,command=self.login_to_app)
        self.login_btn.pack(pady=10)
        self.fr.pack(pady=10)

        self.ask_login = ttk.Label(self.win, text="If you are not registered,create account instead.")
        self.ask_login.pack(pady=15)
        self.signin_btn = ttk.Button(self.win, text="CREATE ACCOUNT INSTEAD",width=40,command=self.change_to_signup)
        self.signin_btn.pack(pady=10)

        self.forget_btn = Button(self.win,text="Forgot Password?",command=self.reset_password,font=("Courier",12),fg="red",relief=FLAT,width=20,borderwidth=0)
        self.forget_btn.pack(pady=10)
        self.sn = IntVar()
        self.check = ttk.Checkbutton(self.win,text="Keep me signed in...",variable=self.sn,command=self.check_signin)
        self.check.pack(pady=10)
        self.win.mainloop()
    def check_signin(self):
        if self.sn.get() == 0:
            self.loggin_status = False
        else:
            self.loggin_status = True

    def reset_password(self):
        if self.user_entry.get()=="":
            messagebox.showerror("USERNAME ERROR","Username field should not be empty!!!")
        else:
            self.reset_win = tkinter.Toplevel()
            self.reset_win.title("Reset Password Window")
            self.reset_win.geometry("500x600+400+30")
            self.reset_win.iconbitmap("pd-icon.ico")
            self.reset_win.resizable(0,0)
            self.reslabel = ttk.Label(self.reset_win,text="Reset Your Password!")
            self.reslabel.pack(pady=10)

            self.quiz1 = ttk.Label(self.reset_win, text="Security Question")
            self.quiz1.pack(pady=20)
            self.quiz_combo1 = ttk.Combobox(self.reset_win, width=40, font=("Courier", 14))
            self.quiz_combo1['values'] = ["--Select--", "Your Favourite Pet", "Your Birth Place", "Your country oof Origin",
                                         "Your President's Name", "Your University Name", "Your Mother's Last Name"]
            self.quiz_combo1.set(self.quiz_combo1['values'][0])
            self.quiz_combo1.pack(pady=20)
            self.quiz_ans1 = ttk.Label(self.reset_win, text="Security Question Answer")
            self.quiz_ans1.pack(pady=20)
            self.ans1 = ttk.Entry(self.reset_win, width=40, font=("Courier", 14))
            self.ans1.pack(pady=20)
            self.pass_3 = ttk.Label(self.reset_win, text="New Password")
            self.pass_3.pack(pady=20)
            self.pass_entry2 = ttk.Entry(self.reset_win, width=30, font=("Arial", 17), show="*")
            self.pass_entry2.pack(pady=20)

            self.rstbtn = ttk.Button(self.reset_win,text="RESET PASSWORD",command=self.reset_password_now)
            self.rstbtn.pack(pady=20)


            self.reset_win.mainloop()
    def reset_password_now(self):
        self.con = database.connect()
        self.p = database.select_one_user(self.con)
        if not self.p:
            self.signup_page()
        self.prev_user = self.p[1:][0]
        self.prev_quiz = self.p[1:][4]
        self.prev_ans = self.p[1:][5]
        if self.quiz_combo1.get()=="" or self.ans1.get()=="":
            messagebox.showerror("Error","Please fill all the required boxes!")
        else:
            try:
                if self.quiz_combo1.get() == self.prev_quiz and self.ans1.get() == self.prev_ans and self.user_entry.get()==self.prev_user:
                    database.reset_password(self.con, self.pass_entry2.get(), self.user_entry.get())
                    messagebox.showinfo("","Your Password was changed successfully")
                    self.start_login()
                else:
                    messagebox.showerror("ERROR","That user does not exist")
            except Exception as err:
                print("Error : ",err)

    def signup_page(self):
        self.win2 = Tk.ThemedTk()
        self.win2.set_theme("arc")
        self.win2.title("Sign up Page")
        self.win2.geometry("600x650+400+25")
        self.win2.resizable(0, 0)
        self.win2.iconbitmap("pd-icon.ico")
        self.font = ("Courier", 18, "bold")
        self.lab = ttk.Label(self.win2, text="Sign Up here!!!")
        self.lab.pack(pady=10)
        # self.new_image1 = ImageTk.PhotoImage(Image.open("analusis-icon.ico"))
        # self.img_welcome1 = Label(self.win2, image=self.new_image1)
        # self.img_welcome1.pack(pady=10)
        self.font_global = ("Courier", 16, "bold")
        self.username = ttk.Label(self.win2, text="Username")
        self.username.pack(pady=20)
        self.name = StringVar()
        self.user_entry1 = ttk.Entry(self.win2, width=40, textvariable=self.name,font=("Arial", 17))
        self.user_entry1.pack(pady=10)
        self.pass_1var = StringVar()
        self.pass_ = ttk.Label(self.win2, text="Password")

        self.pass_.pack(pady=20)
        self.pass_entry1 = ttk.Entry(self.win2, width=40, textvariable=self.pass_1var,font=("Arial", 17),show="*")
        self.pass_entry1.pack(pady=20)
        self.pass_2var = StringVar()

        self.quiz = ttk.Label(self.win2, text="Security Question")
        self.quiz.pack(pady=20)
        self.quiz_combo = ttk.Combobox(self.win2, width=40, font=("Courier", 14))
        self.quiz_combo['values'] = ["--Select--", "Your Favourite Pet", "Your Birth Place", "Your country oof Origin",
                                     "Your President's Name","Your University Name","Your Mother's Last Name"]
        self.quiz_combo.set(self.quiz_combo['values'][0])
        self.quiz_combo.pack(pady=20)
        self.quiz_ans = ttk.Label(self.win2, text="Security Question Answer")
        self.quiz_ans.pack(pady=20)
        self.ans = ttk.Entry(self.win2, width=40, font=("Courier", 14))
        self.ans.pack(pady=10)
        self.chvar = IntVar()

        self.check1 = ttk.Checkbutton(self.win2, text="Make me an ADMIN!", variable=self.chvar,
                                      command=self.checkbtn_changed)
        self.check1.pack()

        self.login_btn = ttk.Button(self.win2, text="CREATE ACCOUNT",width=50,command=self.return_to_login_screen)
        self.login_btn.pack(pady=10)

        self.win2.mainloop()

    def checkbtn_changed(self):
        if self.chvar.get() == 0:
            self.admin = False
        else:
            self.admin = True
    def change_to_signup(self):
        self.win.destroy()
        self.signup_page()
    def login_to_app(self):
        self.connection1 = database.connect()
        if self.user_entry.get()=="" or self.pass_entry.get()=="":
            messagebox.showerror("BLANKS", "Please make sure you fill all entry boxes!!!")
        else:
            self.result = database.check_if_login_is_true(self.connection1,self.user_entry.get(),self.pass_entry.get())
            if self.result:
                database.if_user_isback_update_login_session(self.connection1,self.user_entry.get())
                messagebox.showinfo("Success", "You can now login successfully")
                self.win.destroy()
                self.main_panel()
            else:
                messagebox.showerror("USER NOT EXIST","The user does not exist in database!!!")
    def return_to_login_screen(self):
        self.connection = database.connect()
        if self.user_entry1.get()=="" or self.pass_entry1.get()=="" or self.quiz_combo.get()=="" or self.ans.get()=="":
            messagebox.showerror("BLANKS","Please make sure you fill all entry boxes!!!")
        else:
            database.create_table(connection=self.connection)
            database.put_login_credentials(self.connection,self.user_entry1.get(),self.pass_entry1.get(),
                                           self.admin,self.loggin_status,self.quiz_combo.get(),self.ans.get())
            messagebox.showinfo("Success","Your User Account has been created successfully!!!")
            self.win2.destroy()
            self.start_login()

    def check_if_the_user_is_loggedinorfalse(self):
        #('Louis Wambua', 'wambua254', '1', '1', 'Your Favourite Pet', 'cat')
        self.connection2 = database.connect()
        self.r = database.select_one_user(self.connection2)
        if not self.r:
            self.signup_page()
        self.global_username = self.r[1:][0]
        self.global_admin = self.r[1:][2]
        self.global_password = self.r[1:][1]
        self.global_loggin_status = self.r[1:][3]

        self.loggin_status_now = database.check_if_should_always_be_logged_in(self.connection2,self.global_username)
        # ('1',)
        if self.loggin_status_now == ('1',):
            self.main_panel()
        else:
            self.start_login()
    def user_has_logged_out(self):
        self.connection3 = database.connect()
        database.user_logged_out(self.connection3,self.global_username)
        self.main_win.destroy()
        self.start_login()
    def user_deleted_their_account(self):
        self.connection4 = database.connect()
        database.delete_user_account(self.connection4,self.global_username)
        self.main_win.destroy()
        self.signup_page()
    def access_admin_dashboard(self):
        self.connection5 = database.connect()
        self.k = database.check_if_admin(self.connection5,self.global_username)
        if self.k == ('1',):
            self.btn_redadmin.state = ACTIVE
            self.admin_dashboard()
        else:
            self.btn_redadmin.state = DISABLED
            messagebox.showinfo("ERROR","You are not an ADMIN!!!")
    def initialize_student_data_window(self):
        self.root = Tk.ThemedTk()
        self.root.set_theme("breeze")
        self.style = ttk.Style()
        self.style.theme_use("arc")
        self.root.iconbitmap("pd-icon.ico")
        self.style.configure('.', font=('Courier', 13), background='white')
        self.style.configure(
            "Treeview",
            background="grey",
            foreground="black",
            rowheight=35,
            fieldbackground="white"
        )
        self.root.geometry("1200x700")
        self.root.resizable(0,0)
        self.root.title("Student Data Table")
        self.ent_all = StringVar()
        self.names=['First Name',"Last Name","Class","Marks Obtained"]
        self.btn_names=['Add Student',"Remove Student","Update Student","Report Student"]
        self.item_fr = ttk.Frame(self.root)

        self.v1 = Label(self.item_fr,text=self.names[0],font=("Courier",13)).grid(row=0,column=0,padx=10)
        self.v2 = Label(self.item_fr,text=self.names[1],font=("Courier",13)).grid(row=0,column=1,padx=10)
        self.v3 = Label(self.item_fr,text=self.names[2],font=("Courier",13)).grid(row=0,column=2,padx=10)
        self.v4 = Label(self.item_fr,text=self.names[3],font=("Courier",13)).grid(row=0,column=3,padx=10)

        self.e1 = ttk.Entry(self.item_fr,width=20, font=("Courier", 17))
        self.e1.grid(row=1,column=0,padx=20,pady=10)
        self.e2 = ttk.Entry(self.item_fr,width=20, font=("Courier", 17))
        self.e2.grid(row=1,column=1,padx=20,pady=10)
        self.e3 = ttk.Entry(self.item_fr,width=10, font=("Courier", 17))
        self.e3.grid(row=1,column=2,padx=20,pady=10)
        self.e4 = ttk.Entry(self.item_fr,width=15, font=("Courier", 17))
        self.e4.grid(row=1,column=3,padx=20,pady=10)

        self.b1 = ttk.Button(self.item_fr,text=self.btn_names[0],command=self.add_student).grid(row=2,column=0,padx=10)
        self.b2 = ttk.Button(self.item_fr,text=self.btn_names[1], command=self.remove_student).grid(row=2,column=1,padx=10)
        self.b3 = ttk.Button(self.item_fr,text=self.btn_names[2], command=self.update_student).grid(row=2,column=2,padx=10)
        self.b4 = ttk.Button(self.item_fr,text=self.btn_names[3],command=self.put_report).grid(row=2,column=3,padx=10)
        self.item_fr.pack()
        self.search_fr = ttk.Frame(self.root)
        self.serleb =ttk.Label(self.root,text="Search Table By")
        self.serleb.pack(pady=10)
        self.my_entry = ttk.Entry(self.search_fr, width=30, font=("Courier", 17))
        self.my_entry.grid(row=0,column=0,padx=30)
        self.my_entry.bind("<KeyRelease>",self.search_a_student)
        self.my_search_combo = ttk.Combobox(self.search_fr,values=(self.names), width=25)
        self.my_search_combo.grid(row=0,column=1,padx=50)
        self.my_search_combo.set(self.names[0])
        self.updbtn = ttk.Button(self.search_fr,text="REFRESH TABLE",command=self.fill_from_student_db_to_treeview)
        self.updbtn.grid(row=0,column=3)
        self.selbtn = ttk.Button(self.search_fr, text="SELECT VALUES", command=self.select_values)
        self.selbtn.grid(row=0, column=4,padx=15)
        self.search_fr.pack()

        ttk.Style().configure('Treeview.Heading', foreground="red", font=('Courier', 13, 'bold'))
        ttk.Style().configure('.', font=('Courier', 12), background='white')

        self.tree_frame = ttk.Frame(self.root)
        self.tree = ttk.Treeview(self.tree_frame,height=16,show="headings",columns=self.names)
        self.tree.column(self.names[0], width=285, minwidth=120, anchor=CENTER)
        self.tree.column(self.names[1], width=285, minwidth=120, anchor=CENTER)
        self.tree.column(self.names[2], width=285, minwidth=120, anchor=CENTER)
        self.tree.column(self.names[3], width=285, minwidth=120, anchor=CENTER)

        self.tree.heading(self.names[0], text=self.names[0])
        self.tree.heading(self.names[1], text=self.names[1])
        self.tree.heading(self.names[2], text=self.names[2])
        self.tree.heading(self.names[3], text=self.names[3])
        self.tree.pack(fill=BOTH,padx=15,expand=1)
        self.tree_frame.pack(pady=20)
        self.btn_plot = ttk.Frame(self.root)
        self.btnames = ["Scatter plot the marks","Line plot the marks","View pie-chart of marks"]

        self.scatterbtn = ttk.Button(self.btn_plot,text=self.btnames[0],command=self.plot_scatter).grid(row=0,column=0,padx=20)
        self.linebtn = ttk.Button(self.btn_plot,text=self.btnames[1],command=self.plot_line).grid(row=0,column=1,padx=20)
        self.piebtn = ttk.Button(self.btn_plot,text=self.btnames[2],command=self.plot_pie).grid(row=0,column=2,padx=20)
        self.btn_plot.pack()
        self.fill_from_student_db_to_treeview()
        self.root.mainloop()
    def plot_scatter(self):
        self.NAMES = []
        self.MARKS = []
        self.conn = database.connect_to_student_db()
        self.plot_data = database.select_all_from_students_db(self.conn)
        for pl in self.plot_data:
            self.full_name = pl[1] +" "+ pl[2]
            self.NAMES.append(self.full_name)
            self.MARKS.append(pl[4])
        plt.scatter(self.NAMES,self.MARKS)
        plt.xlabel("Name Of Student")
        plt.ylabel("Marks Obtained")
        plt.title("Students Overall Perfomance")
        plt.tight_layout()
        plt.show()
    def plot_line(self):
        self.NAMES = []
        self.MARKS = []
        self.conn = database.connect_to_student_db()
        self.plot_data = database.select_all_from_students_db(self.conn)
        for pl in self.plot_data:
            self.full_name = pl[1] + " " + pl[2]
            self.NAMES.append(self.full_name)
            self.MARKS.append(pl[4])
        plt.plot(self.NAMES, self.MARKS)
        plt.xlabel("Name Of Student")
        plt.ylabel("Marks Obtained")
        plt.title("Students Overall Perfomance")
        plt.tight_layout()
        plt.show()
    def plot_pie(self):
        self.NAMES = []
        self.MARKS = []
        self.conn = database.connect_to_student_db()
        self.plot_data = database.select_all_from_students_db(self.conn)
        for pl in self.plot_data:
            self.full_name = pl[1] + " " + pl[2]
            self.NAMES.append(self.full_name)
            self.MARKS.append(pl[4])

        plt.style.use('fivethirtyeight')
        # shadow=True
        plt.pie(self.MARKS, labels=self.NAMES, wedgeprops={'edgecolor': 'blue'}, startangle=90,
                autopct='%1.1f%%',radius=1.2,shadow=True,labeldistance=1.2)

        plt.title("Students Overall Perfomance".upper())
        plt.tight_layout()
        plt.show()




    def select_values(self):
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

        self.selected = self.tree.focus()
        self.values = self.tree.item(self.selected, "values")
        # print(values)
        self.e1.insert(0, self.values[0])
        self.e2.insert(0, self.values[1])
        self.e3.insert(0, self.values[2])
        self.e4.insert(0, self.values[3])
    def remove_student(self):
        self.connection15 = database.connect_to_student_db()
        self.selection = self.tree.selection()
        if self.e1.get()=="" or self.e2.get()=="" or self.e3.get()=="" or self.e4.get()=="":
            messagebox.showerror(
                "ERROR",
                "Please select a record from the treeview below!"
            )
        else:
            self.tree.delete(self.selection)
            database.delete_one_from_students(self.connection15,self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get())
            messagebox.showinfo("Success!","The record was deleted successfully!!!")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
    def update_student(self):
        self.connection16 = database.connect_to_student_db()
        self.selected = self.tree.focus()
        if self.e1.get() == "" or self.e2.get() == "" or self.e3.get() == "" or self.e4.get() == "":
            messagebox.showerror(
                "ERROR",
                "Please select a record from the treeview below!"
            )
        else:
            self.total_items_ = self.tree.selection()
            for u in self.total_items_:
                self.ref_username = self.tree.item(u)['values'][0]
                print(self.ref_username)
            self.tree.item(self.selected, text="",values=(self.e1.get(), self.e2.get(), self.e3.get(), self.e4.get()))
            database.update_one_student(self.connection16,self.e1.get(),self.e2.get(),self.e3.get(),self.e4.get(),self.ref_username)
            messagebox.showinfo("Success!", "The record was updated successfully!!!")
            self.e1.delete(0, END)
            self.e2.delete(0, END)
            self.e3.delete(0, END)
            self.e4.delete(0, END)
    def update(self):
        self.connection17 = database.connect_to_student_db()
        self.sel = self.tree.get_children()
        for it in self.sel:
            self.tree.delete(it)
        self.new_data = database.select_all_from_students_db(self.connection17)
        for new in self.new_data:
            self.tree.insert("", END, values=(new[1], new[2], new[3],new[4]))
    def search_a_student(self,e):
        self.total_items = self.tree.get_children()
        self.search = self.my_entry.get()
        if self.search.lower() == "":
            self.update()
        else:
            for item in self.total_items:
                if self.search in self.tree.item(item)['values'][0].lower():
                    self.searched_result = self.tree.item(item)['values']
                    self.tree.delete(item)
                    self.tree.insert("", 0, values=self.searched_result)

    def fill_from_student_db_to_treeview(self):
        self.connection14 = database.connect_to_student_db()
        self.all_data2 = database.select_all_from_students_db(self.connection14)
        if self.tree.get_children():
            self.tree.delete(*self.tree.get_children())
            for item in self.all_data2:
                self.tree.insert("", END, values=(item[1], item[2], item[3],item[4]))
        else:
            for item in self.all_data2:
                self.tree.insert("", END, values=(item[1], item[2], item[3],item[4]))
    def main_panel(self):
        self.main_win = Tk.ThemedTk()
        self.main_win.title("Main Dashboard")
        self.main_win.geometry("1000x380")
        self.main_win.iconbitmap("pd-icon.ico")
        self.main_win.set_theme('arc')
        self.main_win.resizable(0,0)
        self.show_user = Label(self.main_win,text=f'You are Logged in as -> "{self.global_username}"',font=("Courier",14),fg="green")
        self.show_user.pack(pady=15)
        self.btn_redteacher = ttk.Button(self.main_win,text="Open Teachers Dashboard",command=self.teacher_dashboard)
        self.btn_redteacher.pack(pady=10)
        self.btn_redstudent = ttk.Button(self.main_win, text="Open Students Dashboard",command=self.initialize_student_data_window)
        self.btn_redstudent.pack(pady=10)
        self.btn_redadmin = ttk.Button(self.main_win, text="Open Admin Dashboard",command=self.access_admin_dashboard)
        self.btn_redadmin.pack(pady=10)

        self.btn_logout = ttk.Button(self.main_win, text="Logout",command=self.user_has_logged_out)
        self.btn_logout.pack(pady=10)
        self.btn_delacc = ttk.Button(self.main_win, text="Delete Account", command=self.user_deleted_their_account)
        self.btn_delacc.pack(pady=10)

        self.btn_exit = ttk.Button(self.main_win, text="Exit Application",command=self.main_win.quit)
        self.btn_exit.pack(pady=10)


        self.main_win.mainloop()
    def admin_dashboard(self):
        self.admwin = Tk.ThemedTk()
        self.admwin.title("Admin Dashboard")
        self.admwin.geometry("800x420")
        self.admwin.iconbitmap("pd-icon.ico")
        self.admwin.resizable(0,0)
        self.admwin.set_theme('arc')
        validation_admin = "AN ADMIN"
        self.lebel_info = ttk.Label(self.admwin,text="Below are the admin rules! "
                                                 "They can only be accessed by users "
                                                 "logged in as\n admin.")
        self.lebel_info.pack(pady=10)
        self.lebel_val = ttk.Label(self.admwin, text=f"[INFO] you are an: {validation_admin}")
        self.lebel_val.pack(pady=10)
        self.clear_all_teachers = ttk.Button(self.admwin, text="Remove all Teachers from Database",command=self.removeallTeachers)
        self.clear_all_teachers.pack(pady=10)
        self.clear_all_students = ttk.Button(self.admwin, text="Remove all Students from Database",command=self.removeallStudents)
        self.clear_all_students.pack(pady=10)

        self.make_adm = ttk.Button(self.admwin, text="Make a User Admin",command=self.make_user_admin)
        self.make_adm.pack(pady=10)
        self.seeusers = ttk.Button(self.admwin, text="View all available users",command=self.count_users)
        self.seeusers.pack(pady=10)

        self.add_student_now = ttk.Button(self.admwin, text="Add Student", command=self.add_student)
        self.add_student_now.pack(pady=10)

        self.add_teacher = ttk.Button(self.admwin, text="Add Teacher",command=self.add_teacher_win)
        self.add_teacher.pack(pady=10)


        self.admwin.mainloop()
    def removeallTeachers(self):
        self.connection9 = database.connect_to_teachers_db()
        # database.create_teachers_db(self.connection9)
        self.l1 = database.len_of_teachers_db(self.connection9)
        if self.l1 <= 0:
            messagebox.showerror("Error","Nothing to delete since table is empty!")
        else:
            database.delete_all_teachers(self.connection9)
            messagebox.showinfo("Success","You have deleted every teacher in the database!")
    def removeallStudents(self):
        self.connection10 = database.connect_to_student_db()
        # database.create_student_db(self.connection10)
        self.l2 = database.len_of_students_db(self.connection10)
        if self.l2 <= 0:
            messagebox.showerror("Error", "Nothing to delete since table is empty!")
        else:
            database.delete_all_students(self.connection10)
            messagebox.showinfo("Success", "You have deleted every student in the database!")
    def count_users(self):
        self.connection6 = database.connect()
        self.all = database.get_all_users(self.connection6)
        messagebox.showinfo("USERS INFO",f"The number of registered users is : {self.all}")
    def add_teacher_win(self):
        self.add_t = Tk.ThemedTk()
        self.add_t.title("Add Teacher Info")
        self.add_t.set_theme("arc")
        self.add_t.geometry("1200x350")
        self.add_t.iconbitmap("pd-icon.ico")
        self.add_t.configure(padx=10)
        self.add_t.resizable(0,0)
        self.labels = ["Name","Tsc No(8)","Subjects They Teach","Type(T practice/Govt hired)"]
        self.inf = ttk.Label(self.add_t,text="You can add as many subjects as you want "
                                         "simply separate them by commas(,)")
        self.inf.pack()
        self.fr_t = ttk.Frame(self.add_t)

        self.tclebels1 = ttk.Label(self.fr_t,text=self.labels[0]).grid(row=0,column=0,pady=10,padx=10)
        self.tclebels2 = ttk.Label(self.fr_t,text=self.labels[1]).grid(row=0,column=1,pady=10,padx=10)
        self.tclebels3 = ttk.Label(self.fr_t,text=self.labels[2]).grid(row=0,column=2,pady=10,padx=10)
        self.tclebels4 = ttk.Label(self.fr_t,text=self.labels[3]).grid(row=0,column=3,pady=10,padx=10)

        self.tcentry1 = ttk.Entry(self.fr_t,width=25,font=("Courier",13))
        self.tcentry1.grid(row=1,column=0,pady=10,padx=10)
        self.tcentry2 = ttk.Entry(self.fr_t,width=25,font=("Courier",13))
        self.tcentry2.grid(row=1,column=1,pady=10,padx=10)
        self.tcentry3 = ttk.Entry(self.fr_t,width=25,font=("Courier",13))
        self.tcentry3.grid(row=1,column=2,pady=10,padx=10)
        self.tcentry4 = ttk.Entry(self.fr_t,width=25,font=("Courier",13))
        self.tcentry4.grid(row=1,column=3,pady=10,padx=10)
        self.fr_t.pack()
        self.insert = ttk.Button(self.add_t, text="ADD TEACHER",width=30,command=self.add_teachernow)
        self.insert.pack(pady=20)
        self.inff = ttk.Label(self.add_t, text="Only admins can add teachers...")
        self.inff.pack(pady=10)

        self.add_t.mainloop()
    def add_teachernow(self):
        if self.tcentry1.get()=="" or self.tcentry2.get()=="" or self.tcentry3.get()=="" or self.tcentry4.get()=="":
            messagebox.showerror("ERROR","Please fill all blank spaces!")
        else:
            self.connection12 = database.connect_to_teachers_db()
            database.create_teachers_db(self.connection12)
            database.add_teacher_data(self.connection12,self.tcentry1.get(),self.tcentry2.get(),self.tcentry3.get(),self.tcentry4.get())
            messagebox.showinfo("SUCCESS","The teacher record was added successfully!")
    def add_student(self):
        self.add_stud = Tk.ThemedTk()
        self.add_stud.title("Add Student Info Window")
        self.add_stud.set_theme("arc")
        self.add_stud.geometry("1200x350")
        self.add_stud.iconbitmap("pd-icon.ico")
        self.add_stud.configure(padx=10)
        self.add_stud.resizable(0, 0)
        self.labels = ["First Name","Last Name","Class","Marks Obtained"]
        self.fr_t = ttk.Frame(self.add_stud)

        self.st_lebels1 = ttk.Label(self.fr_t, text=self.labels[0]).grid(row=0, column=0, pady=10, padx=10)
        self.st_lebels2 = ttk.Label(self.fr_t, text=self.labels[1]).grid(row=0, column=1, pady=10, padx=10)
        self.st_lebels3 = ttk.Label(self.fr_t, text=self.labels[2]).grid(row=0, column=2, pady=10, padx=10)
        self.st_lebels4 = ttk.Label(self.fr_t, text=self.labels[3]).grid(row=0, column=3, pady=10, padx=10)

        self.st_ents1 = ttk.Entry(self.fr_t, width=20, font=("Courier", 16))
        self.st_ents1.grid(row=1, column=0, pady=10, padx=10)
        self.st_ents2 = ttk.Entry(self.fr_t, width=20, font=("Courier", 16))
        self.st_ents2.grid(row=1, column=1, pady=10, padx=10)
        self.st_ents3 = ttk.Entry(self.fr_t, width=20, font=("Courier", 16))
        self.st_ents3.grid(row=1, column=2, pady=10, padx=10)
        self.st_ents4 = ttk.Entry(self.fr_t, width=20, font=("Courier", 16))
        self.st_ents4.grid(row=1, column=3, pady=10, padx=10)
        self.fr_t.pack(pady=15)
        self.insert = ttk.Button(self.add_stud, text="ADD STUDENT",command=self.add_stnow)
        self.insert.pack(pady=20)
        self.inff = ttk.Label(self.add_stud, text="Both admins and normal users can add students...")
        self.inff.pack(pady=10)

        self.add_stud.mainloop()
    def add_stnow(self):
        if self.st_ents1.get()=="" or self.st_ents2.get()=="" or self.st_ents3.get()=="" or self.st_ents4.get()=="":
            messagebox.showerror("ERROR","Please fill all blank spaces!")
        else:
            self.connection11 = database.connect_to_student_db()
            database.create_student_db(self.connection11)
            database.add_student_data(self.connection11,self.st_ents1.get(),self.st_ents2.get(),self.st_ents3.get(),self.st_ents4.get())
            messagebox.showinfo("SUCCESS","The student record was added successfully!")
    def teacher_dashboard(self):
        self.td = Tk.ThemedTk()
        self.td.set_theme("arc")
        self.style = ttk.Style()
        self.td.iconbitmap("pd-icon.ico")
        self.style.theme_use("clam")
        self.style.configure('.', font=('Courier', 15), background='white')
        self.style.configure(
            "Treeview",
            background="grey",
            foreground="black",
            rowheight=35,
            fieldbackground="white"
        )
        self.td.geometry("1200x700")
        self.td.resizable(0, 0)
        self.td.title("Teachers Data Table")
        self.ent_all = StringVar()
        self.names = ['Teacher Name', "Tsc No(8 digits)", "Subjects They Teach", "Type(T.P/Gvt teacher)"]
        self.btn_names = ['Add Teacher', "Remove Teacher", "Update Teacher", "Report Teacher"]
        self.item_fr1 = ttk.Frame(self.td)
        for i in range(0,4):
            ttk.Label(self.item_fr1, text=self.names[i]).grid(row=0, column=i, padx=10)
            i+=1
        self.b10 = ttk.Entry(self.item_fr1, width=20, font=("Poppins", 17))
        self.b10.grid(row=1, column=0, padx=20, pady=10)
        self.b11 = ttk.Entry(self.item_fr1, width=20, font=("Poppins", 17))
        self.b11.grid(row=1, column=1, padx=20, pady=10)
        self.b12 = ttk.Entry(self.item_fr1, width=10, font=("Poppins", 17))
        self.b12.grid(row=1, column=2, padx=20, pady=10)
        self.b13 = ttk.Entry(self.item_fr1, width=15, font=("Poppins", 17))
        self.b13.grid(row=1, column=3, padx=20, pady=10)

        self.bt101 = ttk.Button(self.item_fr1, text=self.btn_names[0],command=self.add_teacher_win).grid(row=2, column=0, padx=10)
        self.bt111 = ttk.Button(self.item_fr1, text=self.btn_names[1],command=self.remove_teacher_).grid(row=2, column=1, padx=10)
        self.bt122 = ttk.Button(self.item_fr1, text=self.btn_names[2],command=self.update_teacher_).grid(row=2, column=2, padx=10)
        self.bt133 = ttk.Button(self.item_fr1, text=self.btn_names[3],command=self.report_window).grid(row=2, column=3, padx=10)
        self.item_fr1.pack(pady=10)
        self.search_fr1 = ttk.Frame(self.td)
        self.serleb1 = ttk.Label(self.td, text="Search Table By")
        self.serleb1.pack(pady=10)
        self.my_entry1 = ttk.Entry(self.search_fr1, width=30, font=("Poppins", 17))
        self.my_entry1.grid(row=0, column=0, padx=30)
        self.my_entry1.bind("<KeyRelease>",self.search_a_teacher)
        self.my_search_combo1 = ttk.Combobox(self.search_fr1, values=(self.names[:3]), font=('Courier', 14), width=25)
        self.my_search_combo1.grid(row=0, column=1, padx=50)
        self.my_search_combo1.set(self.names[0])
        self.updbtn1 = ttk.Button(self.search_fr1, text="REFRESH TABLE",command=self.fill_from_teacher_db_to_treeview)
        self.updbtn1.grid(row=0, column=3,padx=15)
        self.selbtn1 = ttk.Button(self.search_fr1, text="SELECT VALUES", command=self.select_values_teacher)
        self.selbtn1.grid(row=0, column=4)
        self.search_fr1.pack()

        ttk.Style().configure('Treeview.Heading', foreground="red", font=('Courier', 13, 'bold'))
        ttk.Style().configure('.', font=('Courier', 12), background='white')

        self.tree_frame1 = ttk.Frame(self.td)
        self.tree1 = ttk.Treeview(self.tree_frame1, height=20, show="headings", columns=self.names)
        self.tree1.column(self.names[0], width=285, minwidth=120, anchor=CENTER)
        self.tree1.column(self.names[1], width=285, minwidth=120, anchor=CENTER)
        self.tree1.column(self.names[2], width=285, minwidth=120, anchor=CENTER)
        self.tree1.column(self.names[3], width=285, minwidth=120, anchor=CENTER)

        self.tree1.heading(self.names[0], text=self.names[0])
        self.tree1.heading(self.names[1], text=self.names[1])
        self.tree1.heading(self.names[2], text=self.names[2])
        self.tree1.heading(self.names[3], text=self.names[3])
        self.tree1.pack(fill=BOTH, padx=15, expand=1)
        self.tree_frame1.pack(pady=20)
        self.fill_from_teacher_db_to_treeview()
        self.td.mainloop()

    def select_values_teacher(self):
        self.b10.delete(0, END)
        self.b11.delete(0, END)
        self.b12.delete(0, END)
        self.b13.delete(0, END)

        self.selected = self.tree1.focus()
        self.values = self.tree1.item(self.selected, "values")
        # print(values)
        self.b10.insert(0, self.values[0])
        self.b11.insert(0, self.values[1])
        self.b12.insert(0, self.values[2])
        self.b13.insert(0, self.values[3])
    def remove_teacher_(self):
        self.connection22 = database.connect_to_teachers_db()
        self.selection = self.tree1.selection()
        if self.b10.get()=="" or self.b11.get()=="" or self.b12.get()=="" or self.b13.get()=="":
            messagebox.showerror(
                "ERROR",
                "Please select a record from the treeview below!"
            )
        else:
            self.tree1.delete(self.selection)
            database.delete_one_from_teachers(self.connection22,self.b10.get(),self.b11.get(),self.b12.get(),self.b13.get())
            messagebox.showinfo("Success!","The record was deleted successfully!!!")
            self.b10.delete(0, END)
            self.b11.delete(0, END)
            self.b12.delete(0, END)
            self.b13.delete(0, END)
    def update_teacher_(self):
        self.connection23 = database.connect_to_teachers_db()
        self.selected = self.tree1.focus()
        if self.b10.get() == "" or self.b11.get() == "" or self.b12.get() == "" or self.b13.get() == "":
            messagebox.showerror(
                "ERROR",
                "Please select a record from the treeview below!"
            )
        else:
            self.total_items_1 = self.tree1.selection()
            for l in self.total_items_1:
                self.ref_username_ = self.tree1.item(l)['values'][0]
                print(self.ref_username_)
            self.tree1.item(self.selected, text="",values=(self.b10.get(), self.b11.get(), self.b12.get(), self.b13.get()))
            database.update_one_teacher(self.connection23,self.b10.get(),self.b11.get(),self.b12.get(),self.b13.get(),self.ref_username_)
            messagebox.showinfo("Success!", "The record was updated successfully!!!")
            self.b10.delete(0, END)
            self.b11.delete(0, END)
            self.b12.delete(0, END)
            self.b13.delete(0, END)
    def update_s(self):
        self.connection24 = database.connect_to_teachers_db()
        self.sel11 = self.tree1.get_children()
        for it in self.sel11:
            self.tree1.delete(it)
        self.new_data1 = database.select_all_from_teachers_db(self.connection24)
        for new in self.new_data1:
            self.tree1.insert("", END, values=(new[1], new[2], new[3],new[4]))

    def search_a_teacher(self,e):
        self.total_items1 = self.tree1.get_children()
        self.search1 = self.my_entry1.get()
        if self.search1.lower() == "":
            self.update_s()
        else:
            for item in self.total_items1:
                if self.search1 in self.tree1.item(item)['values'][0].lower():
                    self.searched_result = self.tree1.item(item)['values']
                    self.tree1.delete(item)
                    self.tree1.insert("", 0, values=self.searched_result)


    def fill_from_teacher_db_to_treeview(self):
        self.connection13 = database.connect_to_teachers_db()
        self.all_data = database.select_all_from_teachers_db(self.connection13)
        # print(self.all_data)#[(1, 'Teacher Karimi', 1234567, 'Kiswahili,History', 'Govt Hired'), (2, 'Teacher Muriuki', 2345678, 'Maths,Chemistry', 'Govt Hired')]
        if self.tree1.get_children():
            self.tree1.delete(*self.tree1.get_children())
            for item in self.all_data:
                # for new in item:
                self.tree1.insert("", END, values=(item[1], item[2], item[3],item[4]))

        else:
            for item in self.all_data:
                # for new in item:
                self.tree1.insert("", END, values=(item[1], item[2], item[3],item[4]))

    def report_window(self):
        self.rpwin = Tk.ThemedTk()
        self.rpwin.title("Report Window Dialog!")
        self.rpwin.geometry("800x520")
        self.rpwin.iconbitmap("pd-icon.ico")
        self.rpwin.resizable(0,0)
        #['clearlooks', 'blue', 'scidpink', 'arc', 'elegance', 'scidsand', 'breeze', 'kroc', 'itft1', 'plastik', 'alt', 'xpnative', 'winnative', 'radiance', 'scidpurple', 'vista', 'scidgreen', 'yaru', 'default', 'scidblue', 'ubuntu', 'classic', 'keramik', 'adapta', 'equilux', 'smog', 'aquativo', 'black', 'scidgrey', 'scidmint', 'winxpblue', 'clam']
        self.rpwin.set_theme('radiance')
        self.l1 = ttk.Label(self.rpwin,text="Name of client(the one being reported)",font=("Courier",14,"bold"))
        self.l1.pack(pady=10)
        self.lentry = ttk.Entry(self.rpwin,width=25,font=("Courier",15))
        self.lentry.pack(pady=10)

        self.l2 = ttk.Label(self.rpwin, text="Category (of the one being reported)", font=("Courier", 14, "bold"))
        self.l2.pack(pady=10)
        self.cate = ttk.Combobox(self.rpwin, font=('Courier', 15), width=30,values=("Student","Teacher"))
        self.cate.pack(pady=10)

        self.l3 = ttk.Label(self.rpwin, text="Your Message", font=("Courier", 14, "bold"))
        self.l3.pack(pady=10)
        self.text_box = ScrolledText(self.rpwin,width=70,height=10,font=("Courier",13))
        self.text_box.pack(pady=10)

        self.smbtn = ttk.Button(self.rpwin,text="Submit Report",width=30,command=self.put_report)
        self.smbtn.pack(pady=10)
        self.rpwin.mainloop()
    def put_report(self):
        self.connection12 = database.connect_to_reports()
        database.create_report_db(self.connection12)
        if self.lentry.get()=="" or self.cate.get()=="" or self.text_box.get(1.0,END)=="":
            messagebox.showerror("ERROR","Please fill all blank spaces!!!")
        else:
            database.insert_to_reports(self.connection12,self.lentry.get(),self.cate.get(),self.text_box.get(1.0,END))
            messagebox.showinfo("success","Your report was submitted successfully...")

    def make_user_admin(self):
        self.mkteacher = Tk.ThemedTk()
        self.mkteacher.title("Make user admin")
        self.mkteacher.set_theme('clearlooks')
        self.mkteacher.iconbitmap("pd-icon.ico")
        self.mkteacher.geometry("800x150")
        self.mkteacher.resizable(0,0)
        self.sellebel = ttk.Label(self.mkteacher,text="Select user...")
        self.sellebel.pack()
        self.select = ttk.Combobox(self.mkteacher,font=("Courier",15),width=30)
        self.select.pack(pady=10)

        self.add_now = ttk.Button(self.mkteacher,text="Make Admin",width=30)
        self.add_now.pack(pady=20)
        self.connection7 = database.connect()
        self.is_admin = database.check_if_admin(self.connection7,self.global_username)
        if self.is_admin == ('1',):
            self.select['values'] = ["The Logged in User is An ADMIN"]
            self.select.set(self.select['values'][0])
            self.add_now.state = DISABLED
        else:
            self.connection8 = database.connect()
            self.user_list = []
            self.usres = database.get_usernames_from_users(self.connection8)
            self.user_list.append(self.usres)
            self.select['values'] = self.user_list
            self.select.set(self.select['values'][0])
            database.make_user_admin(self.connection8,self.select.get())
        self.mkteacher.mainloop()



    def start_window(self):
        MainApp().check_if_the_user_is_loggedinorfalse()

# root = Tk.ThemedTk()
app = MainApp()
app.start_window()

