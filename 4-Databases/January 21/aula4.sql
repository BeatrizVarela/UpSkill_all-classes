/* Comandos SQL da aula */

-- 1. Comando simples de criação de uma tabela
CREATE TABLE Students (sid integer, 
	name char(30),
	login char(30), 
	age integer, 
	gpa real);
	
-- 2. Inserção de uma entrada na tabela Students
INSERT 
INTO Students (sid, name, login, age, gpa)
VALUES (53688, 'Smith', 'smith@ee', 18, 3.2);

-- 3. Inserção de múltiplas entradas na tabela Students
INSERT 
INTO Students (sid, name, login, age, gpa)
VALUES 
(53831, 'Madayan', 'madayan@music', 11, 3.2),
(53832, 'Guldu', 'guldu@music', 12, 3.2),
(53650, 'Smith', 'smith@math', 19, 3.2),
(53666, 'Jones', 'jones@cs', 18, 3.2),
(50000, 'Dave', 'dave@cs', 19, 3.2);

-- 4. Simples atualização do valor de uma linha
UPDATE Students S
SET S.age = S.age + 1, S.gpa = S.gpa + 1
WHERE S.sid = 53688;

-- 5. Simples atualização do valor de várias linhas
UPDATE Students S
SET S.gpa = S.gpa - 0.1
WHERE S.gpa >= 3.3;

-- 6. Simples remoção de dados
DELETE
FROM Student S
WHERE S.name = 'Smith';

-- 7. Definição de restrições de domínio e de coluna
CREATE TABLE Empregado( 
	numero INTEGER(4) CHECK (numero > 0),
	vencimento DECIMAL (8,2) CHECK (vencimento > 0.0), 
	PRIMARY KEY (numero)
);

-- 8. Comando que permite apagar a tabela Empregado
DROP TABLE Empregado;

-- 9. Restrições de chave ou restrições de entidade
CREATE TABLE Empregado(
	nid INTEGER(4) PRIMARY KEY, 
    nif INTEGER(9) UNIQUE NOT NULL
);

-- 10. Criação de tabela com chave composta
CREATE TABLE Emp_HDIA(
	nid INTEGER(4),
	dia DATE,
	horas DECIMAL(3,1),
	CONSTRAINT pk_horas_dia PRIMARY KEY (nid, dia)
);

-- 11. Adição de chave primária a uma tabela
ALTER TABLE Students ADD PRIMARY KEY(sid);

-- 12. Restrições de chave estrangeira ou de integridade referencial
CREATE TABLE Enrolled ( 
	studid INTEGER, 
	cid CHAR(20), 
	grade CHAR(10), 
	PRIMARY KEY (studid, cid), 
	FOREIGN KEY (studid) REFERENCES Students(sid) 
);

-- 13. Violação da restrição de restrição primária
INSERT INTO Students (sid, name, login, age, gpa) 
VALUES (null, 'Mike', 'mike@ee', 17,3.4);

-- 14. Violação da restrição de restrição primária repetição
INSERT INTO Students (sid, name, login, age, gpa) 
VALUES (53688, 'Mike', 'mike@ee', 17,3.4);

-- 15.Violação da restrição de chave primária - repetição por update
UPDATE Students S SET S.sid = 50000
WHERE S.sid = 53688;

-- 16. Violação da restrição de chave estrangeira - cid não refere nada
INSERT INTO Enrolled (cid, grade, studid) 
VALUES ('Hindi101', 'B', 51111);

-- 17. Impressão de informação sobre o esquema de determinada tabela
SELECT COLUMN_NAME, CONSTRAINT_NAME, REFERENCED_COLUMN_NAME, REFERENCED_TABLE_NAME 
FROM information_schema.KEY_COLUMN_USAGE
WHERE TABLE_NAME = 'Enrolled';

-- 18. Alteração da restrição de chave estrangeira para adicionar estratégias de violação
-- Para alterar restrição deve-se apagar a restrição e adicionar outra
ALTER TABLE Enrolled DROP CONSTRAINT Enrolled_ibfk_1; -- troque Enrolled_ibfk_1 pela constraint retornada pelo comando anterior

ALTER TABLE Enrolled 
ADD CONSTRAINT 
Enrolled_fk_1 FOREIGN KEY(studid) REFERENCES Students(sid) 
ON DELETE CASCADE 
ON UPDATE NO ACTION;

-- 19. Criação de tabela com estratégias de violação de chave estrangeira
-- antes de criar tabela enrolled deve deitar abaixo a tabela já existente
DROP TABLE Enrolled;

CREATE TABLE Enrolled ( 
	studid INTEGER, 
	cid CHAR(20), 
	grade CHAR(10), 
	PRIMARY KEY (studid, cid), 
	FOREIGN KEY (studid) REFERENCES Students(sid) 
		ON DELETE CASCADE 
		ON UPDATE NO ACTION 
);

-- Estratégia de tratamento de violação de chave estrangeira através de valor por defeito
/* NÂO È SUPORTADO, SIMPLESMENTE ESTÀ DEFINIDO NO STANDARD SQL */
-- DROP TABLE Enrolled;
-- DROP TABLE Students;
-- 
-- CREATE TABLE Students (sid INTEGER PRIMARY KEY DEFAULT 53666, 
-- 					   name CHAR(30),
-- 					   login CHAR(30), 
-- 					   age INTEGER, 
-- 					   gpa REAL
-- );
-- 
-- CREATE TABLE Enrolled ( 
-- 	studid INTEGER, 
-- 	cid CHAR(20), 
-- 	grade CHAR(10), 
-- 	PRIMARY KEY (studid, cid), 
-- 	FOREIGN KEY (studid) REFERENCES Students(sid) 
-- 		ON DELETE SET DEFAULT 
-- 		ON UPDATE NO ACTION 
-- );




