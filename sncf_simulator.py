import pymysql
import json
import requests
import sys
import pprint as pprint
import sncf_queries
import sncf_gui
import sncf_web_requests
from datetime import datetime, date
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtSql import *


# Creates the database using schema files with hard coded file names
def setup_database():
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '')

    try:
        # Set up the databse with schema from schema file
        with db_connection.cursor() as db_cursor:
            f = open("sncf-team3-schema.sql")
            full_sql = f.read()
            sql_commands = full_sql.split(';')
            for sql_command in sql_commands:
                sql_commands = full_sql.replace('\n', '').split(';')[:-1]
                if len(sql_command.strip()) != 0:
                    db_cursor.execute(sql_command)

            db_connection.commit();

        # Populate the databse with initial data from data file
        with db_connection.cursor() as db_cursor:
            f = open("sncf-team3-data.sql")
            full_sql = f.read()
            sql_commands = full_sql.split(';')
            for sql_command in sql_commands:
                sql_commands = full_sql.replace('\n', '').split(';')[:-1]
                if len(sql_command.strip()) != 0:
                    db_cursor.execute(sql_command)

            db_connection.commit();


    finally:
        db_connection.close()







if __name__ == "__main__":
    print("SNCF Simulator Started")
    setup_database()

    #sncf_web_requests.populate_db_with_routes()

    print("Database Setup Completed")


    app = QApplication(sys.argv)
    main= sncf_gui.MainWindow()
    main.show()
    sys.exit(app.exec_())

