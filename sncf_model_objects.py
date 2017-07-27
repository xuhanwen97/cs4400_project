import pprint as pprint

# train_result object is for the trains listed when a user searches for trains to take
class train_result(object):

# holds id, capacity, price_per_km, arrival
# How do I do multiple constructors
    def __init__(self, train_id = None, arrival_station_id = None, arrival_time = None, departure_station_id = None, departure_time = None, distance = None):

        self.train_id = train_id
        self.arrival_station_id = arrival_station_id
        self.arrival_time = arrival_time
        self.departure_station_id = departure_station_id
        self.departure_time = departure_time
        self.distance = distance

    def __repr__(self):
        return pprint.pformat(vars(self))

    def populate_train_result_with_nonstop_query_response_dict(self,query_response_dict):

            self.train_id = query_response_dict['train_id']
            self.departure_station_id = query_response_dict['station_id']
            self.departure_time = query_response_dict['departure_time']
            self.arrival_station_id = query_response_dict['stop1.station_id']
            self.arrival_time = query_response_dict['stop1.arrival_time']
            self.distance = query_response_dict['distance']

    def get_readable_string(self):
        var_dict_keys = vars(self).keys()

        readable_string = "["

        for key in var_dict_keys:
            readable_string = readable_string + str(key) + ": " + str(vars(self)[key]) + ", "

        readable_string = readable_string[:-3] + "]"

        return readable_string





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

        print(self.last_name)



