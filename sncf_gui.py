#!/usr/bin/env python3

import pymysql
import sys
from datetime import datetime, date
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *
import sncf_queries
import sncf_model_objects


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow,self).__init__()

        conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'sncf_team3')
        curr = conn.cursor()

        self.conn = conn

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.login_window()
        self.register()
        self.searchTrips_Screen()
        self.book_trip()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)
        self.Stack.addWidget(self.stack3)
        self.Stack.addWidget(self.stack4)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.setWindowTitle("SNCF Login")


    def login_window(self):
        self.setWindowTitle("SNCF Login")

        pic = QLabel(self)
        self.pixmap =QPixmap('train.jpg')
        pic.setPixmap(self.pixmap)

        email = QLabel("Email",self)
        passw = QLabel("Password",self)
        self.luser = QLineEdit(self)
        self.lpass = QLineEdit(self)
        self.luser.setText('')
        self.lpass.setText('')

        register = QPushButton("Create Account",self)
        register.clicked.connect(self.change_to_create_account)

        login_btn = QPushButton("Login",self)
        login_btn.clicked.connect(self.login)

        layout1 = QFormLayout()
        layout1.addRow(email, self.luser)
        layout1.addRow(passw, self.lpass)

        buttons = QHBoxLayout()
        buttons.addWidget(login_btn)
        buttons.addWidget(register)
        layout1.addRow(buttons)

        layout = QVBoxLayout()
        layout.addLayout(layout1)
        layout.addWidget(pic)

        ######TEST
        hbox1 = QHBoxLayout()
        blank = QLabel("",self)
        departure = QLabel("Departure",self)
        arrival = QLabel("Arrival",self)

        hbox1.addWidget(blank)
        hbox1.addWidget(departure)
        hbox1.addWidget(arrival)

        hbox2 = QHBoxLayout()
        train = QLabel("Train",self)
        station1 = QLabel("Station",self)
        time1 = QLabel("Time",self)
        station2 = QLabel("Station",self)
        time2 = QLabel("Time",self)

        hbox2.addWidget(train)
        hbox2.addWidget(station1)
        hbox2.addWidget(time1)
        hbox2.addWidget(station2)
        hbox2.addWidget(time2)

        text_boxes_hbox = QHBoxLayout()
        text_boxes_hbox.setContentsMargins(0,0,0,0)
        text_boxes_hbox.setSpacing(0)

        #TODO - Turn off editing in these QTextEdits
        text_box1 = QTextEdit()
        text_box2 = QTextEdit()
        text_box3 = QTextEdit()
        text_box4 = QTextEdit()
        text_box5 = QTextEdit()

        text_boxes_hbox.addWidget(text_box1)
        text_boxes_hbox.addWidget(text_box2)
        text_boxes_hbox.addWidget(text_box3)
        text_boxes_hbox.addWidget(text_box4)
        text_boxes_hbox.addWidget(text_box5)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(text_boxes_hbox)


        layout.addLayout(vbox)
        #####TEST

        self.setLayout(layout)

        self.stack1.setLayout(layout)

    def register(self):
        self.setWindowTitle("Create Customer")

        first = QLabel("* First Name",self)
        last = QLabel("* Last Name",self)
        email = QLabel("* Email",self)
        confirm_email = QLabel("* Confirm Email",self)
        password = QLabel("* Password",self)
        confirm_password = QLabel("* Confirm Password",self)
        address1 = QLabel("* Address Line 1",self)
        address2 = QLabel("  Address Line 2",self)
        city = QLabel("* City",self)
        state = QLabel("* State",self)
        postal = QLabel("* Postal Code",self)
        country = QLabel("* Country",self)
        cc_num = QLabel("* Credit Card Number",self)
        cc_exp = QLabel("* Credit Card Exp. Date",self)
        ccv = QLabel("* CCV",self)
        bday = QLabel("* Date of Birth",self)

        # Enable the editing of text boxes
        self.first = QLineEdit(self)
        self.last = QLineEdit(self)
        self.email = QLineEdit(self)
        self.confirm_email = QLineEdit(self)
        self.password = QLineEdit(self)
        self.confirm_password = QLineEdit(self)
        self.address1 = QLineEdit(self)
        self.address2 = QLineEdit(self)
        self.city = QLineEdit(self)
        self.state = QLineEdit(self)
        self.postal = QLineEdit(self)
        self.cc_num = QLineEdit(self)
        self.ccv = QLineEdit(self)

        datelist = [str(num) for num in range(1,32)]

        self.birthdate = QComboBox(self)
        self.birthdate.addItem("DD")
        for date in datelist:
            self.birthdate.addItem(date)

        monthlist = [str(num) for num in range(1,13)]

        self.birthmonth = QComboBox(self)
        self.birthmonth.addItem("MM")
        for month in monthlist:
            self.birthmonth.addItem(month)

        yearlist = [str(num) for num in range(1925,2035)]

        self.birthyear = QComboBox(self)
        self.birthyear.addItem("YYYY")
        for year in yearlist:
            self.birthyear.addItem(year)

        self.cc_exp_month = QComboBox(self)
        self.cc_exp_month.addItem("MM")
        for month in monthlist:
            self.cc_exp_month.addItem(month)

        self.cc_exp_year = QComboBox(self)
        self.cc_exp_year.addItem("YYYY")
        for year in yearlist:
            self.cc_exp_year.addItem(year)

        country_list = ["USA", "Belgium", "Czech Republic", "France", "Germany", "Italy", "Ireland", "Luxembourg", "Netherlands", "Portugal", "Spain", "Switzerland", "United Kingdom"]

        self.countries = QComboBox(self)
        self.countries.addItem("Country")
        self.countries.addItem("----")
        for country_item in country_list:
            self.countries.addItem(country_item)

        # Sets default text for each text box
        self.first.setText('')
        self.last.setText('')
        self.email.setText('')
        self.confirm_email.setText('')
        self.password.setText('')
        self.confirm_password.setText('')
        self.address1.setText('')
        self.address2.setText('')
        self.city.setText('')
        self.state.setText('')
        self.postal.setText('')
        self.cc_num.setText('')
        self.ccv.setText('')

        back = QPushButton("Back",self)
        back.clicked.connect(self.change_to_login)
        submit = QPushButton("Register",self)
        submit.clicked.connect(self.addCustomer)
        direction = QLabel("Fill out the following information. Fields marked with * are required.")

        bday_form = QHBoxLayout()
        bday_form.addWidget(self.birthdate)
        bday_form.addWidget(self.birthmonth)
        bday_form.addWidget(self.birthyear)

        cc_form = QHBoxLayout()
        cc_form.addWidget(self.cc_exp_month)
        cc_form.addWidget(self.cc_exp_year)

        flayout1 = QFormLayout()
        flayout1.addRow(first, self.first)
        flayout1.addRow(last, self.last)
        flayout1.addRow(email, self.email)
        flayout1.addRow(confirm_email, self.confirm_email)
        flayout1.addRow(password, self.password)
        flayout1.addRow(confirm_password, self.confirm_password)
        flayout1.addRow(cc_num, self.cc_num)
        flayout1.addRow(cc_exp, cc_form)
        flayout1.addRow(ccv, self.ccv)

        flayout2 = QFormLayout()
        flayout2.addRow(address1, self.address1)
        flayout2.addRow(address2, self.address2)
        flayout2.addRow(city, self.city)
        flayout2.addRow(state, self.state)
        flayout2.addRow(postal, self.postal)
        flayout2.addRow(country, self.countries)
        flayout2.addRow(bday, bday_form)

        buttons = QHBoxLayout()
        buttons.addWidget(back)
        buttons.addWidget(submit)

        layout1 = QHBoxLayout()
        layout1.addLayout(flayout1)
        layout1.addLayout(flayout2)

        layout2 = QVBoxLayout()
        layout2.addWidget(direction)
        layout2.addLayout(layout1)
        layout2.addLayout(buttons)

        self.setLayout(layout2)
        self.stack2.setLayout(layout2)

    def changeDisplayreg(self):
        i = (self.Stack.currentIndex()+1)%2
        self.Stack.setCurrentIndex(i)

    def changeDisplayregToIndex(self, index):
        self.Stack.setCurrentIndex(index)

    def change_to_login(self):
        self.setWindowTitle("SNCF Login")
        self.changeDisplayregToIndex(0)

    def change_to_create_account(self):
        self.setWindowTitle("Create Customer")
        self.changeDisplayregToIndex(1)

    def change_to_search_trips(self):
        self.setWindowTitle("Search Trips")
        self.changeDisplayregToIndex(2)

    def change_to_book_trips(self):
        self.setWindowTitle("Book Trips")
        self.changeDisplayregToIndex(3)

    def login(self):

        if len(self.luser.text()) == 0 or len(self.lpass.text()) == 0:
            error = QMessageBox.critical(self, "Invalid Login", "Please complete all fields")
        else:
            temp_user = sncf_queries.login_query(self.luser.text(), self.lpass.text())

            # if the response from the login_query function is a user object, then login was successful. Otherwise it failed
            if type(temp_user) is sncf_model_objects.user:
                self.change_to_search_trips()
            elif type(temp_user) is str:
                error = QMessageBox.critical(self,"Invalid Login","Invalid Email or Password")

        self.luser.setText('')
        self.lpass.setText('')

    def addCustomer(self):
        curs = self.conn.cursor()
        if len(self.first.text()) == 0 or len(self.last.text()) == 0 or len(self.email.text()) == 0 or len(self.confirm_email.text()) == 0 or len(self.password.text()) == 0 or len(self.confirm_password.text()) == 0 or len(self.address1.text()) == 0 or len(self.city.text()) == 0 or len(self.state.text()) == 0 or len(self.postal.text()) == 0 or len(self.cc_num.text()) == 0 or len(self.ccv.text()) == 0:
            error = QMessageBox.critical(self, "Invalid Registration","Please complete all required fields")
        elif self.email.text() != self.confirm_email.text():
            error = QMessageBox.critical(self, "Invalid Registration","Emails do not match")
        elif self.password.text() != self.confirm_password.text():
            error = QMessageBox.critical(self, "Invalid Registration","Passwords do not match")
        elif len(self.ccv.text()) != 3 or len(self.cc_num.text()) != 16:
            error = QMessageBox.critical(self, "Invalid Registration","Please check your credit card information")
        else:
            cur.execute('insert into user (email, password, first_name, last_name) values (self.email.text(), self.password.text(), self.first.text(), self.last.text())')
            self.conn.commit()
            userid = cur.lastrowid

            cur.execute('insert into address (line1, line2, city, state, post_code, country) values (self.address1.text(), self.address2.text(), self.city.text(), self.state.text(), self.postal.text(), self.countries.text())')
            self.conn.commit()

            birthday = (self.birthyear.currentText() + '-' + self.birthmonth.currentText() + '-' + self.birthdate.currentText())
            formatter = "%Y-%B-%d"
            bday = datetime.strptime(birthday, formatter).date()
            exp = self.cc_exp_year.currentText() + '-' + self.cc_exp_month.currentText() + '-' + '01'
            formatting = '%Y-%m-%d'
            expire = datetime.strptime(exp, formatting).date()

            addid = cur.lastrowid

            cur.excute('insert into customer (user_id, address_id, birthdate, credit_card_no, credit_card_expiry) values (userid, addid, bday, self.cc_num.text(), expire)')
            self.conn.commit()

            self.changeDisplayreg

            self.first.setEnabled(True)
            self.last.setEnabled(True)
            self.email.setEnabled(True)
            self.confirm_email.setEnabled(True)
            self.password.setEnabled(True)
            self.confirm_password.setEnabled(True)
            self.address1.setEnabled(True)
            self.address2.setEnabled(True)
            self.city.setEnabled(True)
            self.state.setEnabled(True)
            self.postal.setEnabled(True)
            self.cc_num.setEnabled(True)
            self.ccv.setEnabled(True)

    def book_trip(self):
        print("Book")

    def search_results(self):

        if len(self.start_city_drop_down.currentText().strip()) != 0 and len(self.end_city_drop_down.currentText().strip()) != 0:

            train_result_list = sncf_queries.get_non_stop_train(self.start_city_drop_down.currentText(), self.end_city_drop_down.currentText())

            train_result_text = ""

            for train_result in train_result_list:
                train_result_text = train_result_text + train_result.get_readable_string() + "\n"

            self.search_results_text_edit.setText(train_result_text)

        else:
            error = QMessageBox.information(self, "Form Not Complete", "Please fill in all required fields")

    def searchTrips_Screen(self):
        self.setWindowTitle("Search Trips")

        _from = QLabel("From:",self)
        date1 = QLabel("Date:",self)
        time1 = QLabel("Time:",self)
        to = QLabel("To:",self)
        date2 = QLabel("Date:",self)
        time2 = QLabel("Time:",self)

        self.start_city_drop_down = QComboBox(self)
        self.start_city_drop_down.addItem("Paris")

        self.end_city_drop_down = QComboBox(self)
        self.end_city_drop_down.addItem("Metz")

        self.date1 = QLineEdit(self)
        self.time1 = QLineEdit(self)
        self.date2 = QLineEdit(self)
        self.time2 = QLineEdit(self)

        self.date1.setText('')
        self.time1.setText('')
        self.date2.setText('')
        self.time2.setText('')

        cancel = QPushButton("Cancel",self)
        cancel.clicked.connect(self.change_to_login)
        search = QPushButton("Search",self)
        search.clicked.connect(self.search_results)
        book = QPushButton("Book",self)
        book.clicked.connect(self.change_to_book_trips)

        flayout1 = QFormLayout()
        flayout1.addRow(_from, self.start_city_drop_down)
        flayout1.addRow(date1, self.date1)
        flayout1.addRow(time1, self.time1)

        flayout2 = QFormLayout()
        flayout2.addRow(to, self.end_city_drop_down)
        flayout2.addRow(date2, self.date2)
        flayout2.addRow(time2, self.time2)

        buttons = QHBoxLayout()
        buttons.addWidget(cancel)
        buttons.addWidget(search)
        buttons.addWidget(book)

        layout1 = QHBoxLayout()
        layout1.addLayout(flayout1)
        layout1.addLayout(flayout2)

        direction = QLabel("Fill out the following information. Fields marked with * are required.")

        self.search_results_text_edit = QTextEdit( "This is some test data" )

        layout2 = QVBoxLayout()
        layout2.addWidget(direction)
        layout2.addLayout(layout1)
        layout2.addWidget(self.search_results_text_edit)
        layout2.addLayout(buttons)

        self.setLayout(layout2)
        self.stack3.setLayout(layout2)

    def addPassenger():
        print("Add Passenger")

    def add_booking():
        print("Add Passenger")

    def book_trip(self):
        self.setWindowTitle("Book a Trip")

        self.lastname = QLabel("Last Name",self)
        self.firstname = QLabel("First Name",self)
        self.dob = QLabel("Birthdate",self)

        self.cancel = QPushButton("Cancel",self)
        self.cancel.clicked.connect(self.change_to_search_trips)

        self.add_passenger = QPushButton("Add Passenger",self)
        self.add_passenger.clicked.connect(self.addPassenger)

        self.book = QPushButton("Book",self)
        self.book.clicked.connect(self.add_booking)

        direction = QLabel("Passengers:")

        book_form = QHBoxLayout()
        book_form.addWidget(self.lastname)
        book_form.addWidget(self.firstname)
        book_form.addWidget(self.book)

        buttons = QHBoxLayout()
        buttons.addWidget(self.cancel)
        buttons.addWidget(self.add_passenger)
        buttons.addWidget(self.book)

        book_trip_layout = QVBoxLayout()
        book_trip_layout.addWidget(direction)
        book_trip_layout.addLayout(book_form)
        book_trip_layout.addLayout(buttons)

        self.setLayout(book_trip_layout)
        self.stack4.setLayout(book_trip_layout)

    def customerDashboard(self):
        temp = []

    def start_gui(self):
        import sys
        conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'sncf_team3')
        curr = conn.cursor()
        app = QApplication(sys.argv)
        main = MainWindow()
        main.show()
        sys.exit(app.exec_())
        main(sys.argv)


if __name__ == "__main__":
    import sys
    conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'sncf_team3')
    curr = conn.cursor()
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    main(sys.argv)

