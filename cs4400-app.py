#!/usr/bin/env python3

import pymysql
import sys
from datetime import datetime, date
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow,self).__init__()
        self.conn = conn

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.login_window()
        self.register()

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.stack1)
        self.Stack.addWidget(self.stack2)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)


    def login_window(self):
        self.setWindowTitle("")

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
        register.clicked.connect(self.changeDisplayreg)

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

        self.setLayout(layout)

        self.stack1.setLayout(layout)

    def register(self):
        self.setWindowTitle("")

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
        for country in country_list:
            self.countries.addItem(country)

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
        back.clicked.connect(self.changeDisplayreg)
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

    def login(self):
        if len(self.luser.text()) == 0 or len(self.lpass.text()) == 0:
            error = QMessageBox.critical(self, "Invalid Login", "Please complete all fields")
        else:
            cur.execute('select * from user where email = %s and password = %s;',(self.email,self.password))
            self.row = cur.fetchone()
            if self.row == None:
                error = QMessageBox.critical(self,"Invalid Login","Invalid Email or Password")
            else:
                self.luser.setText('')
                self.lpass.setText('')

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

    def customerDashboard(self):
        temp = []

if __name__ == "__main__":
    import sys
    conn = pymysql.connect(host = 'localhost', user = 'root', password = '', db = 'sncf_team3')
    curr = conn.cursor()
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
    main(sys.argv)

