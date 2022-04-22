-- @Ana Paula Afonso - Bases de Dados - DIFCUL - 2015


insert into Tripulante values (25100,'Abel','Antunes','piloto');
insert into Tripulante values (18200,'Carlos','Caldas','piloto'); 
insert into Tripulante values (31100,'Diana','Dias','piloto'); 
insert into Tripulante values (27900,'Gabriela','Gusmão','piloto'); 

insert into Tripulante values (23200,'Bernardo','Borges','pessoal_cabine');
insert into Tripulante values (22300,'Hilario','Hamas','pessoal_cabine');

insert into Tripulante values (29200,'Ernesto','Elvas','pessoal_cabine');
insert into Tripulante values (30300,'Fatima','Felgueiras','pessoal_cabine');
insert into Tripulante values (25600,'Ilda','Ignara','pessoal_cabine');
insert into Tripulante values (28900,'Jorge','Antunes','pessoal_cabine');

insert into Piloto values (25100,123,123,5900,'comandante');
insert into Piloto values (27900,123,123,5940,'comandante');
insert into Piloto values (18200,123,123,5490,'copiloto');
insert into Piloto values (31100,123,123,1590,'copiloto');

insert into TipoAviao values ('AB32','Airbus','A320',4000);
insert into TipoAviao values ('FK10','Fokker','100',3000);
insert into TipoAviao values ('AB34','Airbus','A340',5000);

insert into Habilitado values (25100,'AB32',34561,'2011-02-13');
insert into Habilitado values (25100,'AB34',34561,'2012-02-12');
insert into Habilitado values (25100,'FK10',34561,'2014-02-13');
insert into Habilitado values (18200,'AB32',34572,'2014-02-11');
insert into Habilitado values (18200,'FK10',34572,'2014-02-12');
insert into Habilitado values (31100,'AB32',34583,'2014-02-13');
insert into Habilitado values (27900,'AB32',34591,'2014-02-22');
insert into Habilitado values (27900,'AB34',34591,'2014-02-27');

insert into Aviao values ('CS-ABG','D. Afonso Henriques','2015-02-28','AB32');
insert into Aviao values ('CS-PDC','D. Fernando','2015-02-28','FK10');
insert into Aviao values ('CS-LFV','D. Filipe','2015-02-28','AB34');

insert into Aeroporto values ('LIS','Lisboa-Portela','Portugal');
insert into Aeroporto values ('OPO','Oporto-FrSCarneiro','Portugal');
insert into Aeroporto values ('MAD','Madrid-Barajas','Spain');
insert into Aeroporto values ('HND','Tokyo-Haneda','Japan');
insert into Aeroporto values ('FRA','Frankfurt','Germany');
insert into Aeroporto values ('BKK','Bangkok','Thailand');


insert into Rota values (12345,'LIS','MAD');
insert into Rota values (12346,'LIS','HND');
insert into Rota values (12347,'HND','LIS');
insert into Rota values (12348,'MAD','LIS');
insert into Rota values (12349,'LIS','OPO');
insert into Rota values (12350,'OPO','LIS');
insert into Rota values (12351,'OPO','MAD');
insert into Rota values (12352,'LIS','BKK');
insert into Rota values (12353,'BKK','LIS');


insert into Escala values (12346,'FRA',1);
insert into Escala values (12347,'FRA',1);
insert into Escala values (12352,'MAD',1);
insert into Escala values (12352,'FRA',2);
insert into Escala values (12353,'FRA',1);
insert into Escala values (12353,'MAD',2);


insert into Voo values (755,'2015-10-12 05:30:32',
 '2015-10-13 11:32:23',12346,25100,18200,'CS-ABG');

insert into VooPcabine values (755, 23200);

-- EXTRA
INSERT INTO TipoAviao VALUES ('CESS', 'Cessna', '18', 250);
INSERT INTO Aeroporto VALUES ('CDG', 'Paris', 'France');
INSERT INTO Rota VALUES (12354,'LIS','CDG');
INSERT INTO Rota VALUES (12355,'LIS','BKK');
INSERT INTO Rota VALUES (12356,'OPO','HND');
INSERT INTO Rota VALUES (12357,'OPO','HND');
INSERT INTO Escala VALUES (12355, 'CDG', 1);
INSERT INTO Escala VALUES (12356, 'LIS', 1);
INSERT INTO Escala VALUES (12356, 'CDG', 2);
INSERT INTO Escala VALUES (12357, 'LIS', 1);
INSERT INTO Voo VALUES (756, '2015-10-12 05:30:32', '2015-10-13 11:32:23', 12354, 27900, 31100, 'CS-PDC');
INSERT INTO Voo VALUES (757, '2015-10-12 05:30:32', '2015-10-13 11:32:23', 12355, 27900, 31100, 'CS-PDC');
INSERT INTO Voo VALUES (758, '2015-10-12 05:30:32', '2015-10-13 11:32:23', 12356, 27900, 31100, 'CS-ABG');
INSERT INTO Voo VALUES (759, '2015-10-12 05:30:32', '2015-10-13 11:32:23', 12357, 27900, 31100, 'CS-ABG');
INSERT INTO Voo VALUES (741, '2014-12-01 08:21:59', '2014-12-01 17:21:36', 12346, 25100, 18200, 'CS-LFV');
INSERT INTO Voo VALUES (700, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12345, 25100, 31100, 'CS-LFV');
INSERT INTO Voo VALUES (701, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12345, 27900, 31100, 'CS-ABG');
INSERT INTO Voo VALUES (702, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12347, 25100, 18200, 'CS-ABG');
INSERT INTO Voo VALUES (703, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12348, 25100, 18200, 'CS-ABG');
INSERT INTO Voo VALUES (704, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12349, 27900, 31100, 'CS-ABG');
INSERT INTO Voo VALUES (705, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12350, 25100, 31100, 'CS-ABG');
INSERT INTO Voo VALUES (706, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12351, 25100, 18200, 'CS-ABG');
INSERT INTO Voo VALUES (707, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12352, 27900, 31100, 'CS-ABG');
INSERT INTO Voo VALUES (708, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12353, 25100, 31100, 'CS-ABG');
INSERT INTO Voo VALUES (709, '2015-10-31 22:55:12', '2015-11-01 02:21:36', 12355, 27900, 18200, 'CS-ABG');
INSERT INTO VooPcabine VALUES (756, 30300);
INSERT INTO VooPcabine VALUES (757, 25600);