
#Team Members: Joshua Rubin, Hanwen Xu, Ashwin Haritsa, Daniella Nieves

import pymysql
import json
import requests
import sys
import pprint as pprint
import sncf_model_objects
from datetime import datetime

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
Get city name for the city_id
'''
def get_city_name(city_id):
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with db_connection.cursor() as db_cursor:
            select_city_id_sql = "select name from station where address_id = %s"
            db_cursor.execute(select_city_id_sql, city_id)

            response = db_cursor.fetchone()

            return(response['name'])
    finally:
        db_connection.close()




# returns a list of cities from the distance databse *****FIX LATER
# INTEGRATE BETTER
def get_city_list():
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)

    city_dict = {};

    try:
        # Set up the databse with schema from schema file
        with db_connection.cursor() as db_cursor:
            # Read a single record
            sql = "select name, address_id from station;"
            db_cursor.execute(sql)
            city_dicts = db_cursor.fetchall()

    finally:
        db_connection.close()

    city_list = []

    if len(city_dicts) != 0:
        temp_city = sncf_model_objects.City()

        for city_dict in city_dicts:
            temp_city = sncf_model_objects.City()
            temp_city.populate_city_with_station_query_response_dict(city_dict)
            city_list.append(temp_city)

    return city_list


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
Returns a list of one stop trains from one city to another
input:
    city1 - String Starting city name
    city2 - String Ending city name

return:
    List of train_result objects returned by the query
'''
def get_one_stop_train(city1, city2):

    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)

    try:
        # Set up the databse with schema from schema file
        with db_connection.cursor() as db_cursor:
            # Read a single record
            sql = "select * from (select stop.station_id, stop.train_id, stop.departure_time, stop2.station_id as station2_id, stop2.train_id as train2_id, stop2.arrival_time as stop2_time from stop join stop as stop2 where stop.station_id = (select station_id from station where name = %s) ) as metz_depart join (select stop.station_id, stop.train_id, stop.departure_time, stop2.station_id as station2_id, stop2.train_id as train2_id, stop2.arrival_time as stop2_time from stop join stop as stop2 where stop2.station_id = (select station_id from station where name = %s) ) as aix_arrive on metz_depart.station_id = (select station_id from station where name = %s) and metz_depart.station_id != metz_depart.station2_id and metz_depart.train_id = metz_depart.train2_id and metz_depart.station2_id = aix_arrive.station_id and aix_arrive.train_id = aix_arrive.train2_id and metz_depart.train_id != aix_arrive.train_id and aix_arrive.station_id != aix_arrive.station2_id and aix_arrive.station2_id = (select station_id from station where name = %s) and timestampdiff(minute, metz_depart.stop2_time, aix_arrive.departure_time) >= 10"

            data = (city1, city2, city1, city2)
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
            temp_train_result.populate_train_result_with_one_change_query_response_dict(train)

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

'''
Returns customer_id if given user_id is valid, returns None if it isn't
'''
def get_customer_id_with_user_id(user_id):
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with db_connection.cursor() as db_cursor:
            select_customer_id_sql = "select customer_id from customer where user_id = %s"
            db_cursor.execute(select_customer_id_sql, user_id)

            response = db_cursor.fetchone()

            if response == None or response['customer_id'] == None:
                return None
            else:
                print(response)
                return response['customer_id']
    finally:
        db_connection.close()


'''
Takes in trip_details, customer, and passenger_list
'''
def add_trip_with_customer_passengers(trip_details, user, passenger_list):

    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)

    try:
        with db_connection.cursor() as db_cursor:
            # insert trip, get trip_id
            insert_trip_sql = "insert into trip (customer_id, price) values (%s, %s)"

            data = (get_customer_id_with_user_id(user.user_id), 100)
            db_cursor.execute(insert_trip_sql, data)
            trip_id = db_cursor.lastrowid

            # insert trip_train
            insert_trip_train_sql = "insert into trip_train (embark_stop_id, disembark_stop_id) values (%s, %s)"
            data = (trip_details.departure_station_id, trip_details.arrival_station_id)
            db_cursor.execute(insert_trip_train_sql, data)

            # insert passengers based on the trip_id
            if len(passenger_list) != 0:
                insert_passengers_sql = "insert into passenger (first_name, last_name, birthdate, trip_id) values "
                for passenger in passenger_list:
                    insert_passengers_sql = insert_passengers_sql + "('{!s}', '{!s}', '{!s}', {!s}),".format(passenger.first_name, passenger.last_name, datetime.strftime(passenger.birthdate, "%Y-%m-%d"), trip_id)

                insert_passengers_sql = insert_passengers_sql[:-1]

                print(insert_passengers_sql)

                db_cursor.execute(insert_passengers_sql)

    finally:
        db_connection.commit()
        db_connection.close()


