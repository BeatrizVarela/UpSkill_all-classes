CREATE TABLE Sailors (
	sid INTEGER PRIMARY KEY,
	sname VARCHAR(30),
	rating INTEGER(4),
	age REAL(3,1)
);

INSERT 
INTO Sailors
VALUES
(22, 'Dustin', 7, 45.0),
(29, 'Brutus', 1, 33.0),
(31, 'Lubber', 8, 55.5),
(32, 'Andy', 8, 25.5),
(58, 'Rusty', 10, 35.0),
(61, 'Horatio', 7, 35.0), 
(71, 'Zorba', 10, 16.0), 
(74, 'Horatio', 9, 35.0),
(85, 'Art', 3, 25.5),
(95, 'Bob', 3, 63.5);

CREATE TABLE Boats (
	bid INTEGER PRIMARY KEY,
	bname VARCHAR(30),
	color VARCHAR(30),
);

INSERT 
INTO Boats
VALUES
(101, 'Interlake', 'blue'),
(102, 'Interlake', 'red'),
(103, 'Clipper', 'green'),
(104, 'Marine', 'red');

CREATE TABLE Reserves ( 
	sid INTEGER, 
	bid INTEGER, 
	`day` DATE, 
	CONSTRAINT Boats_pk_1 PRIMARY KEY(sid,bid,`day`), 
	CONSTRAINT Boats_fk_1 FOREIGN KEY(sid) REFERENCES Sailors(sid), 
	CONSTRAINT Boats_fk_2 FOREIGN KEY(bid) REFERENCES Boats(bid) 
);

INSERT 
INTO Reserves 
VALUES 
(22, 101, '1996/10/10'), 
(58, 103, '1996/12/11');