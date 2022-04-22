-- 1. Comando simples de criação da tabela Students
CREATE TABLE Students (
	sid integer PRIMARY KEY, 
	name char(30),
	login char(30), 
	age integer, 
	gpa real
);

-- 2. Comando simples de criação de tabela Enrolled
CREATE TABLE Enrolled ( 
	cid VARCHAR(30) PRIMARY KEY, 
	grade VARCHAR(30), 
	studid INTEGER, 
	CONSTRAINT Enrolled_fk_1 FOREIGN KEY(studid) REFERENCES Students(sid) 
);

-- 3. Inserção de múltiplas entradas na tabela Students
INSERT 
INTO Students (sid, name, login, age, gpa)
VALUES 
(53831, 'Madayan', 'madayan@music', 11, 3.3),
(53832, 'Guldu', 'guldu@music', 12, 3.4),
(53688, 'Smith', 'smith@ee', 18, 3.2),
(53650, 'Smith', 'smith@math', 19, 3.8),
(53666, 'Jones', 'jones@cs', 18, 1.8),
(50000, 'Dave', 'dave@cs', 19, 2.0);

-- 5. Inserção de múltiplas entradas na tabela Enrolled
INSERT 
INTO Enrolled (cid, grade, studid)
VALUES 
('Carnatic101','C',53831),
('Reggae203','B',53832),
('Topology112','A',53650),
('History105','B',53666);

-- 6. Adição de coluna
ALTER TABLE Students 
ADD COLUMN maiden_name CHAR(10);

-- 7. Alteração de coluna
ALTER TABLE Students 
MODIFY COLUMN maiden_name CHAR(20);

-- 8. Remoção de coluna
ALTER TABLE Students 
DROP COLUMN maiden_name;

-- 9. Adição de restrições de coluna
ALTER TABLE Enrolled 
ADD CONSTRAINT nn_enrolled_grade CHECK (grade IS NOT NULL);

-- 10. Remoção de restrições
ALTER TABLE Enrolled 
DROP CONSTRAINT nn_enrolled_grade;

-- 11. Pesquisa de dados simples numa única tabela
SELECT * FROM Students;

-- 12. Pesquisa de dados com multiplas colunas numa única tabela
SELECT name, login 
FROM Students 
WHERE age >= 18;

-- 13. Pesquisa de dados em multiplas tabelas
SELECT S.name, E.cid
FROM Students S, Enrolled E 
WHERE S.sid = E.studid AND grade = 'A';

-- 14. Criação de vista dos alunos mais velhos
CREATE VIEW Old_students (name, login, age) AS 
	SELECT name, login, age
	FROM Students
	WHERE age >= 18;
	
-- 15. Pesquisa dos dados de uma vista
SELECT * FROM Old_students;

-- 16.Vista dos alunos com 'B'
CREATE VIEW B_Students (name, sid, course) AS 
	SELECT S.name, S.sid, E.cid
	FROM Students S, Enrolled E
	WHERE S.sid = E.studid AND E.grade = 'B';
	
-- 17. Vista dos bons alunos
CREATE VIEW good_student (sid, gpa) AS 
	SELECT sid, gpa 
	FROM Students
	WHERE gpa >=3;

-- 17.1., 19.1 Inserção de entradas na vista que cumprem com restrições
INSERT INTO good_student VALUES(10000, 3);

-- 17.2., 19.2 Inserção de entradas na vista que não cumprem com restrições
INSERT INTO good_student VALUES(11000, 1.8)

-- 18. Apagar vista good_student
DROP VIEW good_student

-- 19. Vista dos bons alunos com verificação de condição
CREATE VIEW good_student (sid, gpa) AS
	SELECT sid, gpa 
	FROM Students 
	WHERE gpa >=3 
	WITH CHECK OPTION
	
-- atualização de linhas na view com violação de restrição
UPDATE good_student SET gpa = 2.0;


