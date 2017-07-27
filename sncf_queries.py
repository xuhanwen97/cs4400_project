import pymysql
import json
import requests
import sys
import pprint as pprint
import sncf_model_objects

'''
Returns a list of admin dictionaries with keys:
    user_id - int(11)
    email - char(32)
    password - char(128)
    first_name - varchar(32)
    last_name - varchar(64)
    customer_id - int(11) - admin should be null
    address_id - int(11) - admin should be null
    birthdate - date - admin should be null
    credit_card_no - char(17) - admin should be null
    credit_card_expiry - date - admin should be null
'''
def get_admins():
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)

    try:
        with db_connection.cursor() as db_cursor:

            sql = "select * from user left join customer using (user_id) where customer_id is NULL"
            db_cursor.execute(sql)
            admin_dict = db_cursor.fetchall()

    finally:
        db_connection.commit()
        db_connection.close()

    if len(admin_dict) != 0:
        return(admin_dict)

'''
Returns a list of customer dictionaries with keys:
    user_id - int(11)
    email - char(32)
    password - char(128)
    first_name - varchar(32)
    last_name - varchar(64)
    customer_id - int(11)
    address_id - int(11)
    birthdate - date
    credit_card_no - char(17)
    credit_card_expiry - date
'''
def get_customers():
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)

    try:
        # Set up the databse with schema from schema file
        with db_connection.cursor() as db_cursor:
            # Read a single record
            sql = "select * from user join customer using (user_id)"
            db_cursor.execute(sql)
            customer_dict = db_cursor.fetchall()

    finally:
        db_connection.commit()
        db_connection.close()

    if len(customer_dict) != 0:
        return(customer_dict)


'''
Returns a list of non-stop trains from one city to another
input:
    city1 - String Starting city name
    city2 - String Ending city name

return:
    List of train_result objects returned by the query
'''
def get_non_stop_train(city1, city2):
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)

    try:
        # Set up the databse with schema from schema file
        with db_connection.cursor() as db_cursor:
            # Read a single record
            sql = "select * from stop join stop as stop1 using (train_id) where stop.station_id = (select station_id from station where name = %s) and stop1.station_id = (select station_id from station where name = %s) and stop.departure_time < stop1.arrival_time order by stop.departure_time"
            data = (city1, city2)
            db_cursor.execute(sql, data)
            train_dict = db_cursor.fetchall()

    finally:
        db_connection.commit()
        db_connection.close()

    if len(train_dict) != 0:
        list_of_train_dict = []
        # Parses the response from SQL into a useable train
        for train in train_dict:

            temp_train_result = sncf_model_objects.train_result()
            temp_train_result.populate_train_result_with_nonstop_query_response_dict(train)

            list_of_train_dict.append(temp_train_result)


        return(list_of_train_dict)

'''
Sends the login info to the database and sees if the user exists there
input login_email, login_password

returns
User object if login is successful
Message string if login is not successful
'''
def login_query(login_email, login_password):

    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)

    try:
        # Set up the databse with schema from schema file
        with db_connection.cursor() as db_cursor:
            # Read a single record
            sql = "select * from user where email = %s and password = %s"
            data = (login_email, login_password)
            db_cursor.execute(sql, data)
            login_response = db_cursor.fetchall()

    finally:
        db_connection.commit()
        db_connection.close()

    if len(login_response) != 0:
        temp_user = sncf_model_objects.user()
        temp_user.populate_user_with_login_response_dict(login_response[0])
        return( temp_user )
    else:
        return( "Invalid login, invalid username and password combination!" )
