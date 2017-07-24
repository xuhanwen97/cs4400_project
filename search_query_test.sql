use sncf_team3;
-- join train trip stop
\! echo List trains stops and stations nicely

select * from train join stop using(train_id)
    join station using(station_id)
    where train_id = 2;

\! echo List trains that start from Metz

select * from train join stop using(train_id)
    join station using(station_id)
    where station_id =
    (
        select station_id from station where name = 'Metz'
    );

\! echo List trip_trains have embark and disembark stations right, so I need to find trains that embark at the station I want to start at, and then find train numbers of those trains to see if any of those match where I need to go to. \n

\! echo This grabs what trains are on each of the trips that have been booked

-- This grabs what trains are on each of the trips that have been booked, join with trip using trip_id to get what customers booked these trips
select trip_train_id, trip_id, embark_stop_id, disembark_stop_id, train_id, stop_time from trip_train join stop on trip_train.embark_stop_id = stop.stop_id
    join station using(station_id)
    order by stop_time;

\! echo This grabs direct trains that go from one station to another
select stop.station_id, stop.train_id, stop.stop_time, stop1.station_id as station2_id, stop1.stop_time as stop_time2 from stop join stop as stop1 where stop.station_id = (select station_id from station where name = 'Metz') and stop1.station_id = (select station_id from station where name = 'Aix') and stop.train_id = stop1.train_id;




