import pprint as pprint
from datetime import datetime

# train_result object is for the trains listed when a user searches for trains to take
class train_result(object):

# holds id, capacity, price_per_km, arrival
# How do I do multiple constructors
    def __init__(self, train1_id = None, train2_id = None, arrival_station_id = None, arrival_time = None, departure_station_id = None, departure_time = None, inter_station_id = None, inter_time = None, distance = None, is_multi_legged = None):

        self.train1_id = train1_id
        self.train2_id = train2_id
        self.arrival_station_id = arrival_station_id
        self.arrival_time = arrival_time
        self.inter_station_id = inter_station_id
        self.inter_time = inter_time
        self.departure_station_id = departure_station_id
        self.departure_time = departure_time
        self.distance = distance
        self.is_multi_legged = is_multi_legged

    def __repr__(self):
        return pprint.pformat(vars(self))

    def populate_train_result_with_nonstop_query_response_dict(self,query_response_dict):

            self.train1_id = query_response_dict['train_id']
            self.departure_station_id = query_response_dict['station_id']
            self.departure_time = query_response_dict['departure_time']
            self.arrival_station_id = query_response_dict['stop1.station_id']
            self.arrival_time = query_response_dict['stop1.arrival_time']
            self.distance = query_response_dict['distance']
            self.is_multi_legged = False;

    def populate_train_result_with_one_change_query_response_dict(self, query_response_dict):

            self.train1_id = query_response_dict['train_id']
            self.train2_id = query_response_dict['aix_arrive.train_id']
            self.departure_station_id = query_response_dict['station_id']
            self.departure_time = query_response_dict['departure_time']
            self.arrival_station_id = query_response_dict['aix_arrive.station2_id']
            self.arrival_time = query_response_dict['aix_arrive.stop2_time']
            self.inter_station_id = query_response_dict['station2_id']
            self.inter_time = query_response_dict['stop2_time']
            self.is_multi_legged = True;

    def get_readable_string(self):
        var_dict_keys = vars(self).keys()

        readable_string = "["

        for key in var_dict_keys:
            readable_string = readable_string + str(key) + ": " + str(vars(self)[key]) + ", "

        readable_string = readable_string[:-3] + "]"

        return readable_string


class temp_passenger(object):

    def __init__(self, first_name = None, last_name = None, birthdate = None):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate

    def __repr__(self):
        return pprint.pformat(vars(self))

    #takes in first name, last name strings, birthdate datetime, and trip_id
    def populate_passenger(self, first_name, last_name, birthdate):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate


class user(object):

    def __init__(self, user_id = None, email = None, password = None, first_name = None, last_name = None ):
        self.user_id = user_id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return pprint.pformat(vars(self))

    def populate_user_with_login_response_dict(self, query_response_dict):

        self.user_id = query_response_dict['user_id']
        self.email = query_response_dict['email']
        self.password = query_response_dict['password']
        self.first_name = query_response_dict['first_name']
        self.last_name = query_response_dict['last_name']

class City(object):

    def __init__(self, address_id = None, city_name = None):
        self.address_id = address_id
        self.city_name = city_name

    def __repr__(self):
        return pprint.pformat(vars(self))

    def populate_city_with_station_query_response_dict(self, query_response_dict):

        self.address_id = query_response_dict['address_id']
        self.city_name = query_response_dict['name']

