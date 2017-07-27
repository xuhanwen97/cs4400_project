use sncf_team3;

insert into user (email, first_name, last_name, password) values
  ('aharitsa3@gatech.edu', 'Ashwin', 'Haritsa', 'CS4400'),
  ('xuhanwen97@gmail.com', 'Hanwen', 'Xu', 'is'),
  ('rubinjoshua4@gmail.com', 'Josh', 'Rubin', 'the'),
  ('daniellamichelle@gmail.com', 'Daniella', 'Nieves', 'best'),
  ('1', 'Test', 'User', '1'),
  ('simpkins@cc.gatech.edu', 'Chris', 'Simpkins', 'class');

insert into address (line1, line2, city, state, country, post_code) values
  ('1 Place du Général de Gaulle', NULL, 'Metz', NULL, 'France', '57000'),
  ('Route Départementale 9', NULL, 'Aix-en-Provence', NULL, 'France', '13290'),
  ('11 Place de la Gare', NULL, 'Luxembourg', NULL, 'Luxembourg', '1130'),
  ('Place du 11 Novembre 1918', NULL, 'Paris', NULL, 'France', '75010'),
  ('3 Place Thiers', NULL, 'Nancy', NULL, 'France', '54000'),
  ('Place de la gare', NULL, 'Strasbourg', NULL, 'France', '67000'),
  ('Place de la gare', NULL, 'Reims', NULL, 'France', '51100'),
  ('Avenue Thiers', NULL, 'Nice', NULL, 'France', '06008'),
  ('Square Narvik', NULL, 'Marseille', NULL, 'France', '13232'),
  ('Gare de Dijon-ville', NULL, 'Dijon', NULL, 'France', '21000'),
  ('4400 gatech Way',NULL,'Atlanta','Georgia','USA','30313'),
  ('2316 UGAsux Road',NULL,'Atlanta','Georgia','USA','30313'),
  ('28-27 techwon',NULL,'Atlanta','Georgia','USA','30313'),
  ('2 Rue Marconi',NULL,'Metz',NULL,'France','57000'),
  ('2304 Cadet Drive',NULL,'US Air Force Academy','Colorado','USA','80840-0000');

insert into customer (user_id, address_id, birthdate, credit_card_no, credit_card_expiry) values
    (2, 11, '1997-01-01', 3833869948671938, '1992-07-12'),
    (1, 12, '1920-07-04', 9499603839590682, '1940-03-18'),
    (3, 13, '1969-11-11', 1023885039687923, '1960-06-23'),
    (4, 14, '2012-12-24', 4920386749182940, '1923-02-19');

insert into trip (customer_id, price) values
  (1,100.00),
  (2,100.00),
  (3,100.00),
  (4,100.00);

insert into passenger (first_name, last_name, birthdate, trip_id) values
  ('Daniella','Nieves','1998-05-05',1),
  ('Ashwin','Haritsa','1998-04-29',2),
  ('Hanwen','Xu','1997-05-24',3),
  ('Josh','Rubin','1997-01-14',4),
  ('Santa','Claus','0001-12-25',3),
  ('Donald','Trump','2016-07-04',3),
  ('George','Burdell','1927-09-17',4),
  ('Lonzo','Ball','1997-10-27',2),
  ('Bud','Peterson','1954-09-21',1);

insert into station (station_id, name, address_id) values
  (1, 'Metz', 1),
  (2, 'Aix', 2),
  (3, 'Luxenbourg', 3),
  (4, 'Paris', 4),
  (5, 'Nancy', 5),
  (6, 'Strasbourg', 6),
  (7, 'Reims', 7),
  (8, 'Nice', 8),
  (9, 'Marseille', 9),
  (10, 'Dijon', 10);

insert into train (train_id, capacity, price_per_km) values
  (1,500, 0.1),
  (2,500, 0.1),
  (3,500, 0.1),
  (4,500, 0.1),
  (5,500, 0.1),
  (6,500, 0.1),
  (7,500, 0.1),
  (8,500, 0.1),
  (9,500, 0.1),
  (10,500, 0.1),
  (11,500, 0.1);

insert into stop (stop_id, station_id,train_id,arrival_time,departure_time,distance) values
  (1,1,1,'05:16:00','05:26:00',100),
  (2,2,1,'12:26:00','12:36:00',100),
  (3,1,2,'10:05:00','10:15:00',100),
  (4,6,2,'11:45:00','11:55:00',100),
  (5,6,11,'11:45:00','11:55:00',100),
  (6,2,11,'17:00:00','17:10:00',100),
  (7,1,3,'09:16:00','09:26:00',100),
  (8,4,3,'10:55:00','11:05:00',100),
  (9,4,4,'14:59:00','15:09:00',100),
  (10,1,4,'17:38:00','17:48:00',100),
  (11,5,5,'18:04:00','18:14:00',100),
  (12,1,5,'18:51:00','19:01:00',100),
  (13,1,5,'19:01:00','19:11:00',100),
  (14,3,5,'19:51:00','20:01:00',100),
  (15,9,6,'09:50:00','10:00:00',100),
  (16,8,6,'12:40:00','12:50:00',100),
  (17,7,7,'15:35:00','15:45:00',100),
  (18,10,7,'19:25:00','19:35:00',100),
  (19,8,8,'12:16:00','12:26:00',100),
  (20,9,8,'15:02:00','15:12:00',100),
  (21,9,9,'15:28:00','15:38:00',100),
  (22,1,9,'23:19:00','23:29:00',100),
  (23,4,10,'17:29:00','17:39:00',100),
  (24,1,10,'19:05:00','19:15:00',100),
  (25,3,10,'19:51:00','20:01:00',100),
  (26,6,1, '06:26:00','06:36:00',100);

insert into trip_train (trip_id,embark_stop_id,disembark_stop_id) values
    (1,3,4),
    (2,4,5),
    (3,6,7),
    (4,8,9);
