import sncf_queries
import sncf_model_objects
import pymysql
import json
import requests
import sys
import pprint as pprint

# returns a list of all city combinations
def get_city_combos():
    city_list = sncf_queries.get_city_list()
    route_list = []
    for city1 in city_list:
        for city2 in city_list:
            if city1 != city2:
                route_list.append((city1,city2))
    return(route_list)


# returns the city_id for the corresponding city name
def get_city_id(city_name):
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with db_connection.cursor() as db_cursor:
            select_city_id_sql = "select address_id from station where name = %s"
            db_cursor.execute(select_city_id_sql, city_name)

            response = db_cursor.fetchone()

            return(response['address_id'])
    finally:
        db_connection.close()


# takes in a response dict from google distance matrix api, inserts data into route
def insert_route_using_dict(response_dict):
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)

    try:
        with db_connection.cursor() as db_cursor:

            start_city_id = get_city_id(response_dict['origin_city'])
            end_city_id = get_city_id(response_dict['destination_city'])

            trip_duration_minutes = int(response_dict['trip_duration_seconds']) / 60

            base_insert_sql = "insert into route (start_city_address_id, end_city_address_id, distance, duration) values (%s,%s,%s,%s)"

            data = (start_city_id, end_city_id, response_dict['km_distance'], trip_duration_minutes)

            db_cursor.execute(base_insert_sql, data)

            db_connection.commit()

    finally:
        db_connection.close()


# returns a dictionary containing the google distance matrix api
# response data from city1 to city2 city names
def make_distance_request(city1, city2):
    apikey = "AIzaSyCseiSYJM8q6Xcv6arZD_M3nIv1wSwbxtQ"
    distance_url = "https://maps.googleapis.com/maps/api/distancematrix/json"

    if city1 == 'Aix':
        city1 = city1 + ', France'
    elif city2 == 'Aix':
        city2 = city2 + ', France'


    myparams = {'origins': city1,
                'destinations': city2,
                'mode': 'transit',
                'transit_mode': 'train',
                'key': apikey}


    response = requests.get( distance_url, params = myparams )
    response = response.json()

    print(response)

    origin_city = response['origin_addresses'][0].split(',')[0]
    destination_city = response['destination_addresses'][0].split(',')[0]

    elements = response['rows'][0]['elements'][0]

    if 'distance' in elements:
        km_distance = response['rows'][0]['elements'][0]['distance']['text']
        km_distance = km_distance.split()[0].replace(',','')
        km_distance = int(km_distance)

        km_distance_id = response['rows'][0]['elements'][0]['distance']['value']

        trip_duration = response['rows'][0]['elements'][0]['duration']['text']
        trip_duration_seconds = response['rows'][0]['elements'][0]['duration']['value']
    else:
        km_distance = None
        km_distance_id = None
        trip_duration = None
        trip_duration_seconds = None

    trip_info = {}
    trip_info['origin_city'] = origin_city.split()
    trip_info['destination_city'] = destination_city.split()
    trip_info['km_distance'] = km_distance
    trip_info['distance_id'] = km_distance_id
    trip_info['trip_duration'] = trip_duration
    trip_info['trip_duration_seconds'] = trip_duration_seconds


    return trip_info

# populate database with data for all routes from all possible city combinations ----- NOTE LIMITED TO 5 QUERIES TO GOOGLE API
def populate_db_with_routes():
    count = 0;
    api_request_count = 2;

    city_combos = get_city_combos()

    print(city_combos)

    for city_combo in city_combos:
        if count < api_request_count:
            start_city_address_id = city_combo[0].city_name
            end_city_address_id = city_combo[1].city_name


            city_combo_response = make_distance_request(start_city_address_id, end_city_address_id)
            print(city_combo_response)
            insert_route_using_dict(city_combo_response)
            count += 1

# returns the distance between two cities in KM, given two city ids
def get_distance(city1_id, city2_id):
    db_connection = pymysql.connect(host = 'localhost',
                             user = 'root',
                             password = '',
                             db = 'sncf_team3',
                             cursorclass = pymysql.cursors.DictCursor)
    try:
        with db_connection.cursor() as db_cursor:
            select_distance_sql = "select distance from route where start_city_address_id = %s and end_city_address_id = %s"
            data = (city1_id, city2_id)
            db_cursor.execute(select_distance_sql, data)
            return(db_cursor.fetchone()['distance'])
    finally:
        db_connection.close()
