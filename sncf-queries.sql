use sncf_team3;

#list emails and names of all the admin users
select email, user.first_name, user.last_name from user left join customer using (user_id) where customer_id is NULL;

#list emails and names of all the customers
select email, user.first_name, user.last_name from user join customer using (user_id);

#list the direct trips (single trains) from Metz to Aix
select stop.station_id, stop.train_id, stop.stop_time, stop1.station_id as station2_id, stop1.stop_time as stop_time2 from stop join stop as stop1 where stop.station_id = (select station_id from station where name = 'Metz') and stop1.station_id = (select station_id from station where name = 'Aix') and stop.train_id = stop1.train_id;
#list the one-change trips from Metz to Aix


#Book a trip from Metz to Aix on 8 August 2017 for two passengers
#(including the customer booking the trip)


#Show the passenger manifest (passenger first names and last names)
#for the leg Metz to Strasbourg for a the train that originates in Metz and terminates in Aix.
