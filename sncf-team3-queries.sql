use sncf_team3;

\! echo List emails and names of all the admin users
select email, user.first_name, user.last_name from user left join customer using (user_id) where customer_id is NULL;

\! echo Emails and names of all the customers
select email, user.first_name, user.last_name from user join customer using (user_id);

\! echo List the direct trips ,single trains, from Metz to Aix
select * from stop join stop as stop1 using (train_id) where stop.station_id = (select station_id from station where name = 'Metz') and stop1.station_id = (select station_id from station where name = 'Aix') and stop.departure_time < stop1.arrival_time;

\! echo List the one-change trips from Metz to Aix

select * from (select stop.station_id, stop.train_id, stop.departure_time, stop2.station_id as station2_id,stop2.train_id as train2_id, stop2.arrival_time as arrival_time from stop join stop as stop2 where stop.station_id = (select station_id from station where name = 'Metz')) as metz_depart join (select stop.station_id, stop.train_id, stop.arrival_time, stop2.station_id as station2_id, stop2.train_id as train2_id,stop2.departure_time as departure_time from stop join stop as stop2 where stop2.station_id = (select station_id from station where name = 'Aix')) as aix_arrive on metz_depart.station_id = (select station_id from station where name = 'Metz') and metz_depart.station_id != metz_depart.station2_id and metz_depart.train_id = metz_depart.train2_id and metz_depart.station2_id = aix_arrive.station_id and aix_arrive.train_id = aix_arrive.train2_id and aix_arrive.station_id = aix_arrive.station2_id and aix_arrive.station2_id = (select station_id from station where name = 'Aix');

\! echo Book a trip from Metz to Aix on 8 August 2017 for two passengers ,including the customer booking the trip.
select user_id into @new_customer from user where first_name = 'Josh' and last_name = 'Rubin';
insert into trip (customer_id, price) values (@new_customer, 100.00);
set @trip_id = last_insert_id();
insert into passenger (first_name, last_name, birthdate, trip_id) values
	('Scooby','Doo','1969-10-13',@trip_id),
	('Josh','Rubin','1997-01-14',@trip_id);
select station_id into @Metz from station where name = 'Metz';
select station_id into @Aix from station where name = 'Aix';
insert into trip_train (trip_id, embark_stop_id, disembark_stop_id) values
	(@trip_id, @Metz, @Aix);

\! echo Show the passenger manifest passenger first names and last names for the leg Metz to Strasbourg for a the train that originates in Metz and terminates in Aix.

select first_name,last_name from (select first_name,last_name,embark_stop_id,disembark_stop_id from passenger join trip_train using (trip_id)) as a join (select * from (select stop.station_id,stop2.station_id as station2_id from stop join stop as stop2 where stop.station_id = (select station_id from station where name = 'Metz') and stop2.station_id = (select station_id from station where name = 'Strasbourg') and stop.train_id = stop2.train_id) as trip_1 join (select stop3.station_id as station3_id, stop4.station_id as station4_id from stop as stop3 join stop as stop4 where stop3.station_id = (select station_id from station where name = 'Strasbourg') and stop4.station_id = (select station_id from station where name = 'Aix') and stop3.train_id = stop4.train_id) as trip_2 on trip_1.station2_id = trip_2.station3_id limit 1) as b where a.embark_stop_id = b.station_id;
