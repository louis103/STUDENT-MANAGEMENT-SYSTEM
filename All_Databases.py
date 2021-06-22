import sqlite3
CREATE_TABLE_LOGIN = "CREATE TABLE IF NOT EXISTS login_table (id INTEGER PRIMARY KEY, username TEXT, password TEXT, admin TEXT,login_status TEXT,security_quiz TEXT,security_ans TEXT)"
INSERT_PAS_USER = "INSERT INTO login_table (username , password , admin,login_status,security_quiz,security_ans) VALUES (?,?,?,?,?,?)"
SELECT_USER_BY_USERNAME_PASS = "SELECT * FROM login_table WHERE (username,password) = (?,?)"
CREATE_TABLE_STUDENTS_DATA = "CREATE TABLE IF NOT EXISTS students_marks_table (id INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT,class INTEGER, marks INTEGER)"
CREATE_TABLE_TEACHERS_DATA = "CREATE TABLE IF NOT EXISTS teachers_data_table (id INTEGER PRIMARY KEY, name TEXT, tsc_no INTEGER,subjects TEXT, type_of_teacher TEXT)"
SELECT_USER_BY_ADMIN_PREVILAGES = "SELECT admin FROM login_table WHERE username = ?"
SELECT_USER_BY_LOGIN_PREVILAGES = "SELECT login_status FROM login_table WHERE username = ?"
SELECT_ONE_USER = "SELECT * FROM login_table"
SELECT_MULTIPLE_USERS = "SELECT username FROM login_table"
INSERT_STUDENT = "INSERT INTO students_marks_table (firstname , lastname ,class, marks) VALUES (?,?,?,?)"
INSERT_TEACHER = "INSERT INTO teachers_data_table (name , tsc_no ,subjects, type_of_teacher) VALUES (?,?,?,?)"
GET_ALL_STUDENTS = "SELECT * FROM students_marks_table"
GET_ALL_TEACHERS = "SELECT * FROM teachers_data_table"
GET_ALL_USERS = "SELECT * FROM login_table"
DELETE_ALL_STUDENTS = "DELETE FROM students_marks_table"
DELETE_ALL_TEACHERS = "DELETE FROM teachers_data_table"
DELETE_SPECIFIC_USER = "DELETE FROM login_table WHERE username = ?"
UPDATE_USER_LOGIN_STATUS_TO_FALSE = "UPDATE login_table SET login_status ='0' WHERE username = ?"
UPDATE_USER_LOGIN_STATUS_TO_TRUE = "UPDATE login_table SET login_status ='1' WHERE username = ?"
MAKE_USER_ADMIN = "UPDATE login_table SET admin ='1' WHERE username = ?"
RESET_PASSWORD = "UPDATE login_table SET password = ? WHERE username = ?"

def connect():
    '''
    connecting to our database for login users
    :return:
    '''
    return sqlite3.connect("LOGIN_DB.db")
def reset_password(connection,password,username):
    """
    reset password in database
    :param connection:
    :param password:
    :param username:
    :return:
    """
    with connection:
        connection.execute(RESET_PASSWORD,(password,username))
def make_user_admin(connection,user):
    """
    make a selected user admin
    :param connection:
    :param user:
    :return:
    """
    with connection:
        connection.execute(MAKE_USER_ADMIN,(user,))
def delete_one_from_students(connection,first,last,class_n,marks):
    """
    delete one student
    :param connection:
    :param first:
    :param last:
    :param class_n:
    :param marks:
    :return:
    """
    with connection:
        connection.execute("DELETE from students_marks_table WHERE (firstname,lastname,class,marks) = (?,?,?,?)",
                           (first,last,class_n,marks))

def delete_one_from_teachers(connection,name , tsc_no ,subjects, type_of_teacher):
    """
    delete one teacher
    :param connection:
    :param name:
    :param tsc_no:
    :param subjects:
    :param type_of_teacher:
    :return:
    """
    with connection:
        connection.execute("DELETE from teachers_data_table WHERE (name , tsc_no ,subjects, type_of_teacher) = (?,?,?,?)",
                           (name , tsc_no ,subjects, type_of_teacher))

def update_one_student(connection,first,last,class_n,marks,_first):
    """
    update one student
    :param connection:
    :param first:
    :param last:
    :param class_n:
    :param marks:
    :return:
    """
    with connection:
        connection.execute("""UPDATE students_marks_table SET (firstname , lastname ,class, marks) = (?,?,?,?) WHERE firstname =?""",
                           (first,last,class_n,marks,_first))

def update_one_teacher(connection,name , tsc_no ,subjects, type_of_teacher,_teacher):
    """
    update one teacher
    :param connection:
    :param name:
    :param tsc_no:
    :param subjects:
    :param type_of_teacher:
    :return:
    """
    with connection:
        connection.execute("""UPDATE teachers_data_table SET (name , tsc_no ,subjects, type_of_teacher) = (?,?,?,?) WHERE name = ?""",
                           (name , tsc_no ,subjects, type_of_teacher,_teacher))

def get_all_users(connection):
    """
    help us retrieve no of logged in users
    :param connection:
    :return:
    """
    with connection:
        return len(connection.execute(GET_ALL_USERS).fetchall())
def get_usernames_from_users(connection):
    '''
    get usernames for multiple users
    :param connection:
    :return:
    '''
    with connection:
        s = connection.execute(SELECT_MULTIPLE_USERS)
        return s.fetchall()
def select_one_user(connection):
    '''
    select one user
    :param connection:
    :return:
    '''
    with connection:
        c = connection.execute(SELECT_ONE_USER)
        return c.fetchone()
def get_all_users_for_admin_purposes(connection):
    """
    get all usernames for making admin
    :param connection:
    :return:
    """
    with connection:
        return connection.execute(GET_ALL_USERS).fetchall()[1]
def user_logged_out(connection,user):
    """
    update login status to false when user has logged out
    :param connection:
    :param user:
    :return:
    """
    with connection:
        return connection.execute(UPDATE_USER_LOGIN_STATUS_TO_FALSE,(user,))
def delete_all_students(connection):
    """
    delete all students by admin
    :param connection:
    :return:
    """
    with connection:
        return connection.execute(DELETE_ALL_STUDENTS)
def delete_all_teachers(connection):
    """
    delete all students by admin
    :param connection:
    :return:
    """
    with connection:
        return connection.execute(DELETE_ALL_TEACHERS)
def delete_user_account(connection,user):
    """
    delete user when clicked on delete account
    :param connection:
    :return:
    """
    with connection:
        connection.execute(DELETE_SPECIFIC_USER,(user,))
def create_table(connection):
    '''
    Helps us to create tables if they dont exist in our database
    :param connection:
    :return:
    '''
    with connection:
        connection.execute(CREATE_TABLE_LOGIN)

def put_login_credentials(connection,username,password,admin_previlages,loggin,quiz,answer):
    '''
    This will help us put login credentials for our database
    :param connection:
    :return:
    '''
    with connection:
        connection.execute(INSERT_PAS_USER, (username, password,admin_previlages,loggin,quiz,answer))

def check_if_login_is_true(connection,username,password):
    '''
    Help us to make sure that user is logged in
    :param connection:
    :return:
    '''
    with connection:
        c = connection.execute(SELECT_USER_BY_USERNAME_PASS,(username,password))
        return c.fetchone()
def if_user_isback_update_login_session(connection,user):
    """
    update loggin session after user gets back!
    :param connection:
    :param user:
    :return:
    """
    with connection:
        return connection.execute(UPDATE_USER_LOGIN_STATUS_TO_TRUE, (user,))
def check_if_admin(connection,username):
    """
    check if the user is an admin or not!!!
    :param connection:
    :param username_adm:
    :return:
    """
    with connection:
        c = connection.execute(SELECT_USER_BY_ADMIN_PREVILAGES,(username,))
        return c.fetchone()
def check_if_should_always_be_logged_in(connection,username_log):
    """
    check if user should be always loggin or not
    :param connection:
    :param username_log:
    :return:
    """
    with connection:
        c = connection.execute(SELECT_USER_BY_LOGIN_PREVILAGES, (username_log,))
        return c.fetchone()
def connect_to_student_db():
    '''
    connecting to our database for login users
    :return:
    '''
    return sqlite3.connect("STUDENTS_DATABASE.db")

def create_student_db(connection):
    """
    creating a students database for storage of their data
    :param connection:
    :return:
    """
    with connection:
        connection.execute(CREATE_TABLE_STUDENTS_DATA)
def len_of_teachers_db(connection):
    return len(connection.execute(GET_ALL_TEACHERS).fetchall())
def len_of_students_db(connection):
    return len(connection.execute(GET_ALL_STUDENTS).fetchall())

def connect_to_teachers_db():
    '''
    connecting to our database for login users
    :return:
    '''
    return sqlite3.connect("TEACHERS_DATABASE.db")
def connect_to_reports():
    """
    connect to report db
    :param connection:
    :return:
    """
    return sqlite3.connect("REPORTS.db")
def create_report_db(connection):
    """
    create reports db
    :param connection:
    :return:
    """
    with  connection:
        connection.execute("CREATE TABLE IF NOT EXISTS reports_table (id INTEGER PRIMARY KEY, Name TEXT, category TEXT, report TEXT)")

def insert_to_reports(connection,name_,category,report):
    """
    insert into report table
    :param connection:
    :param name_:
    :param category:
    :param report:
    :return:
    """
    with connection:
        connection.execute("INSERT INTO reports_table (Name , category ,report) VALUES (?,?,?)",
                           (name_,category,report))
def create_teachers_db(connection):
    """
    creating a teachers database for storage of their data
    :param connection:
    :return:
    """
    with connection:
        connection.execute(CREATE_TABLE_TEACHERS_DATA)

def add_student_data(connection,fname,lname,class_n,marks):
    """
    help us insert student data to database
    :param connection:
    :param fname:
    :param lname:
    :param class_n:
    :param marks:
    :return:
    """
    with connection:
        connection.execute(INSERT_STUDENT,(fname,lname,class_n,marks))

def add_teacher_data(connection,name,tsc_no,subjects,type_of_teacher):
    """
    insert data in our teachers database
    :param connection:
    :param name:
    :param tsc_no:
    :param subjects:
    :param type_of_teacher:
    :return:
    """
    with connection:
        connection.execute(INSERT_TEACHER,(name,tsc_no,subjects,type_of_teacher))
def select_all_from_students_db(connection):
    """
    help us to retrieve everything from the database
    :param connection:
    :return:
    """
    with connection:
        r = connection.execute(GET_ALL_STUDENTS)
        return r.fetchall()
def select_all_from_teachers_db(connection):
    """
    help us to retrieve everything from the database
    :param connection:
    :return:
    """
    with connection:
        f = connection.execute(GET_ALL_TEACHERS)
        return f.fetchall()