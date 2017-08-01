use sncf_team3;

-- List the two train trips from Metz to Aix including the customer who booked the trip
select station_id into @metz_station_id from station where name = 'Metz';
select station_id into @aix_station_id from station where name = 'Aix';

\! echo attempt to grab trains that leave from metz and arrive in aix that share the same intermediate stop
select * from
    (
        select stop.station_id, stop.train_id, stop.departure_time, stop2.station_id as station2_id, stop2.train_id as train2_id, stop2.arrival_time as stop2_time from stop join stop as stop2
        where stop.station_id = (select station_id from station where name = 'Metz')
    ) as metz_depart
    join
    (
        select stop.station_id, stop.train_id, stop.departure_time, stop2.station_id as station2_id, stop2.train_id as train2_id, stop2.arrival_time as stop2_time from stop join stop as stop2
        where stop2.station_id = (select station_id from station where name = 'Aix')
    ) as aix_arrive
    -- departs from metz, doesn't go from metz - metz for leg 1, same train id during leg 1, leg 1 ending station = leg 2 beginning station, same train id during leg 2, doesn't go from aix - aix for leg 2, arrives at aix
    on metz_depart.station_id = (select station_id from station where name = 'Metz')
        and metz_depart.station_id != metz_depart.station2_id
        and metz_depart.train_id = metz_depart.train2_id
        and metz_depart.station2_id = aix_arrive.station_id
        and aix_arrive.train_id = aix_arrive.train2_id
        and metz_depart.train_id != aix_arrive.train_id
        and aix_arrive.station_id != aix_arrive.station2_id
        and aix_arrive.station2_id = (select station_id from station where name = 'Aix')
        and timestampdiff(minute, metz_depart.stop2_time, aix_arrive.departure_time) >= 10;


select * from (select stop.station_id, stop.train_id, stop.departure_time, stop2.station_id as station2_id, stop2.train_id as train2_id, stop2.arrival_time as stop2_time from stop join stop as stop2 where stop.station_id = (select station_id from station where name = 'Metz') ) as metz_depart join (select stop.station_id, stop.train_id, stop.departure_time, stop2.station_id as station2_id, stop2.train_id as train2_id, stop2.arrival_time as stop2_time from stop join stop as stop2 where stop2.station_id = (select station_id from station where name = 'Aix') ) as aix_arrive on metz_depart.station_id = (select station_id from station where name = 'Metz') and metz_depart.station_id != metz_depart.station2_id and metz_depart.train_id = metz_depart.train2_id and metz_depart.station2_id = aix_arrive.station_id and aix_arrive.train_id = aix_arrive.train2_id and metz_depart.train_id != aix_arrive.train_id and aix_arrive.station_id != aix_arrive.station2_id and aix_arrive.station2_id = (select station_id from station where name = 'Aix') and timestampdiff(minute, metz_depart.stop2_time, aix_arrive.departure_time) >= 10;










