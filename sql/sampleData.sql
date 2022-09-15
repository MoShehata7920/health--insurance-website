INSERT INTO plane values (1, "Basic", 1000);
INSERT INTO plane values (2, "Premium", 2000);
INSERT INTO plane values (3, "Golden", 3000);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01234567891234","mohamed Alnawagy", "2000-9-27", "M", 7000, "tanta 13 wallStreat", "00201097601669", false, 180, 65, "ex1@gmail.com", 3);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01234567820144","ahmed fares", "1998-07-3", "M", 2000, "tanta 13 wallStreat", "00201097601663", true, 175, 80, "ex2@gmail.com", 1);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01234510091234","mahmoud saeed", "1990-01-12", "M", 3000, "tanta new village", "00201097771669", false, 182, 70, "ex3@gmail.com", 1);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01234567891888","adel fahmy", "2000-05-24", "M", 6900, "tanta old village", "00201097600165", true, 187, 88, "ex4@gmail.com", 2);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("85334567891234","khaled ali", "1970-01-18", "M", 3500, "tanta new city", "00201137601680", true, 179, 90, "ex5@gmail.com", 1);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01266667891234","aya ahmed", "1975-01-13", "F", 3000, "tanta 13 old city", "00201097622229", false, 157, 70, "ex6@gmail.com", 2);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01234567876201","karim khaled", "1980-01-22", "M", 3100, "tanta 15 wallStreat", "00201097108623", false, 60, 65, "ex7@gmail.com", 1);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01230107891234","moustafa hamed", "1988-01-12", "M", 10000, "tanta 10 new city", "00201097771623", false, 189, 100, "ex8@gmail.com", 3);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01204567891234","ali khaled", "1993-01-19", "M", 7250, "tanta 20 albahr st", "00201097601365", true, 170, 70, "ex9@gmail.com", 2);
INSERT INTO Customers (ssn, `name`, birth_date, gender, income, address, phone, has_chronic_dis, tall, weight, email, plane) VALUES 
("01234567842235","mohamed adel", "1992-03-21", "M", 4200, "tanta 10 saeed st", "00201137601670", false, 181, 75, "ex10@gmail.com", 1);

select *from Customers;


INSERT INTO hospital (H_name, phone, address, email, website) VALUES 
("Dar Alshefaa", "00201085641189", "Tanta 13 Algeesh st", "Alshefaa@hospital.com", "www.Alshefaa.com");
INSERT INTO hospital (H_name, phone, address, email, website) VALUES 
("Kenana", "00201085641189", "Tanta Estad st", "Kenana@hospital.com", "www.Kenana.com");
INSERT INTO hospital (H_name, phone, address, email, website) VALUES 
("ibn sina", "00201085620049", "Tanta almahtta st", "IbnSina@hospital.com", "www.IbnSina.com");
INSERT INTO hospital (H_name, phone, address, email, website) VALUES 
("Alsalam", "00201085648861", "Tanta alhelw st", "Alsalam@hospital.com", "www.Alsalam.com");
INSERT INTO hospital (H_name, phone, address, email, website) VALUES 
("OmAlkora", "00201085648013", "Tanta alagezy st", "OmAlkora@hospital.com", "www.OmAlkora.com");
INSERT INTO hospital (H_name, phone, address, email, website) VALUES 
("Dar Alfoaad", "00201085641234", "Tanta Algeesh st", "DarAlfoaad@hospital.com", "www.DarAlfoaad.com");
INSERT INTO hospital (H_name, phone, address, email, website) VALUES 
("Dar Alkemma", "00201085647802", "Tanta 10 Algeesh st", "DarAlkemma@hospital.com", "www.DarAlkemma.com");

INSERT INTO hospital_planes VALUES (1, 1);
INSERT INTO hospital_planes VALUES (1, 2);
INSERT INTO hospital_planes VALUES (2, 1);
INSERT INTO hospital_planes VALUES (3, 3);
INSERT INTO hospital_planes VALUES (4, 2);
INSERT INTO hospital_planes VALUES (5, 1);
INSERT INTO hospital_planes VALUES (5, 2);
INSERT INTO hospital_planes VALUES (5, 3);
INSERT INTO hospital_planes VALUES (6, 3);
INSERT INTO hospital_planes VALUES (7, 2);
INSERT INTO hospital_planes VALUES (7, 3);


-- select * from hospital where H_id in(select hospital from
-- hospital_planes where plane = 3) ;


select * from Customers where plane = 1;
