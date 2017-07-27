def searchTrips_Screen(self):
        self.setWindowTitle("Search Trips")

        _from = QLabel("From:",self)
        date1 = QLabel("Date:",self)
        time1 = QLabel("Time:",self)
        to = QLabel("To:",self)
        date2 = QLabel("Date:",self)
        time2 = QLabel("Time:",self)
        

        self._from = QLineEdit(self)
        self.date1 = QLineEdit(self)
        self.time1 = QLineEdit(self)
        self.to = QLineEdit(self)
        self.date2 = QLineEdit(self)
        self.time2 = QLineEdit(self)

        self._from.setText('')
        self.date1.setText('')
        self.time1.setText('')
        self.to.setText('')
        self.date2.setText('')
        self.time2.setText('')

        cancel = QPushButton("Cancel",self)
        back.clicked.connect(self.changeDisplayreg)
        search = QPushButton("Search",self)
        submit.clicked.connect(self.searchResults)
        book = QPushButton("Book",self)
        submit.clicked.connect(self.bookTrip)

        flayout1 = QFormLayout()
        flayout1.addRow(_from, self._from)
        flayout1.addRow(date1, self.date1)
        flayout1.addRow(time1, self.time1)

        flayout2 = QFormLayout()
        flayout2.addRow(to, self.to)
        flayout2.addRow(date2, self.date2)
        flayout2.addRow(time2, self.time2)

        buttons = QHBoxLayout()
        buttons.addWidget(cancel)
        buttons.addWidget(search)
        buttons.addWidget(book)

        layout1 = QHBoxLayout()
        layout1.addLayout(flayout1)
        layout1.addLayout(flayout2)

        layout2 = QVBoxLayout()
        layout2.addWidget(direction)
        layout2.addLayout(layout1)
        layout2.addLayout(buttons)

        self.setLayout(layout)
        self.stack1.setLayout(layout)

