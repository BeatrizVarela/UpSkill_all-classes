-- @Ana Paula Afonso - Bases de Dados - DIFCUL - 2015
-- Para apagar as tabelas é necessário apagar as foreign keys primeiro porque existem várias circulares

ALTER TABLE VooPcabine DROP FOREIGN KEY fk_VooPcabine_id_pcabine;
ALTER TABLE VooPcabine DROP FOREIGN KEY fk_VooPcabine_n_voo;
ALTER TABLE Voo DROP FOREIGN KEY fk_Voo_cod_rota;
ALTER TABLE Voo DROP FOREIGN KEY  fk_Voo_id_comandante;
ALTER TABLE Voo DROP FOREIGN KEY  fk_Voo_copiloto;
ALTER TABLE Voo DROP FOREIGN KEY  fk_Voo_matricula;
ALTER TABLE Escala DROP FOREIGN KEY fk_Escala_cod_aeroporto;
ALTER TABLE Escala DROP FOREIGN KEY fk_Escala_cod_rota;
ALTER TABLE Rota DROP FOREIGN KEY fk_Rota_cod_aeroporto_ini;
ALTER TABLE Rota DROP FOREIGN KEY  fk_Rota_cod_aeroporto_fim;
ALTER TABLE Habilitado DROP FOREIGN KEY  fk_Habilitado_id;
ALTER TABLE Habilitado DROP FOREIGN KEY  fk_Habilitado_cod_tipo;
ALTER TABLE Piloto DROP FOREIGN KEY fk_Piloto_id;
ALTER TABLE Aviao DROP FOREIGN KEY fk_Aviao_cod_tipo;
DROP TABLE IF EXISTS TipoAviao;
DROP TABLE IF EXISTS Aviao;
DROP TABLE IF EXISTS Piloto;
DROP TABLE IF EXISTS Tripulante;
DROP TABLE IF EXISTS Habilitado;
DROP TABLE IF EXISTS Rota;
DROP TABLE IF EXISTS Escala;
DROP TABLE IF EXISTS Voo;
DROP TABLE IF EXISTS VooPcabine;
DROP TABLE IF EXISTS Aeroporto;

-- TipoAviao (cod_tipo, marca, modelo, autonomia)

CREATE TABLE TipoAviao (
cod_tipo VARCHAR(4),
marca	VARCHAR(20) NOT NULL,
modelo	VARCHAR(20) NOT NULL,
autonomia NUMERIC(4)NOT NULL,
CONSTRAINT pk_TipoAviao PRIMARY KEY (cod_tipo));

-- Aviao (matricula, nome, data_aquisicao, TipoAviao.cod_tipo)

CREATE TABLE Aviao (
matricula 	VARCHAR(6),
nome		VARCHAR(20) NOT NULL,
data_aquisicao	DATE NOT NULL,
cod_tipo	VARCHAR(4),
CONSTRAINT pk_Aviao_matricula PRIMARY KEY (matricula),
CONSTRAINT fk_Aviao_cod_tipo FOREIGN KEY (cod_tipo) REFERENCES TipoAviao (cod_tipo));

-- Tripulante(id, nome, apelido, tipo)

CREATE TABLE Tripulante (
id	NUMERIC(5),
nome	VARCHAR(20) NOT NULL,
apelido	VARCHAR(20) NOT NULL,
tipo	VARCHAR(20),
CONSTRAINT pk_Tripulante_id PRIMARY KEY (id),
CONSTRAINT chk_Tripulante_tipo CHECK (tipo IN ('pessoal_cabine','piloto')));

-- Piloto (Tripulante.id, n_aterragens, n_descolagens, n_horas_voo, tipo)

CREATE TABLE Piloto (
id		NUMERIC(5),	
n_aterragens	NUMERIC(6) NOT NULL,
n_descolagens	NUMERIC(6) NOT NULL,
n_horas_voo	NUMERIC(8) NOT NULL,
tipo	VARCHAR(20),
CONSTRAINT pk_Piloto_id PRIMARY KEY (id),
CONSTRAINT fk_Piloto_id FOREIGN KEY (id) REFERENCES Tripulante(id),
CONSTRAINT chk_Piloto_tipo CHECK (tipo IN ('copiloto','comandante'))
 );

-- Habilitado ( Piloto.id, TipoAviao.cod_tipo, n_licenca, data_licenca)

CREATE TABLE Habilitado (
id	NUMERIC(5),	
cod_tipo	VARCHAR(4),
n_licenca	NUMERIC(6) NOT NULL,
data_licenca	DATE NOT NULL,
CONSTRAINT pk_Habilitado PRIMARY KEY (id,cod_tipo),
CONSTRAINT fk_Habilitado_id FOREIGN KEY (id) REFERENCES Piloto(id),
CONSTRAINT fk_Habilitado_cod_tipo FOREIGN KEY (cod_tipo) REFERENCES TipoAviao(cod_tipo));

-- Aeroporto ( cod_aeroporto, local, pais)

CREATE TABLE Aeroporto (
cod_aeroporto	VARCHAR(3),	
local	VARCHAR(20) NOT NULL,
pais	VARCHAR(20) NOT NULL,
CONSTRAINT pk_cod_aeroporto PRIMARY KEY (cod_aeroporto));

-- Rota ( cod_rota, Aeroporto.cod_aeroporto_ini, Aeroporto.cod_aeroporto_fim) 

CREATE TABLE Rota (
cod_rota	NUMERIC(5),
cod_aeroporto_ini	VARCHAR(3),
cod_aeroporto_fim	VARCHAR(3),
CONSTRAINT pk_Rota PRIMARY KEY (cod_rota),
CONSTRAINT fk_Rota_cod_aeroporto_ini FOREIGN KEY (cod_aeroporto_ini) REFERENCES Aeroporto(cod_aeroporto),
CONSTRAINT fk_Rota_cod_aeroporto_fim FOREIGN KEY (cod_aeroporto_fim) REFERENCES Aeroporto(cod_aeroporto));

-- Escala ( Rota.cod_rota, Aeroporto.cod_aeroporto, n_ordem)

CREATE TABLE Escala (
cod_rota	NUMERIC(5),
cod_aeroporto	VARCHAR(3),
n_ordem	NUMERIC(1) NOT NULL,
CONSTRAINT pk_Escala PRIMARY KEY (cod_rota,cod_aeroporto), 
CONSTRAINT fk_Escala_cod_aeroporto FOREIGN KEY (cod_aeroporto) REFERENCES Aeroporto(cod_aeroporto),
CONSTRAINT fk_Escala_cod_rota FOREIGN KEY (cod_rota) REFERENCES Rota(cod_rota));

-- Voo ( n_voo, data_partida, data_chegada, Rota.cod_rota, Piloto.id_comandante ,
--	 Piloto.id_copiloto, Aviao.matricula) 

CREATE TABLE Voo (
n_voo	NUMERIC(3),
data_partida	TIMESTAMP NOT NULL,
data_chegada	TIMESTAMP NOT NULL,
cod_rota	NUMERIC(5),	
id_comandante	NUMERIC(5),
id_copiloto	NUMERIC(5),
matricula	VARCHAR(6),
CONSTRAINT pk_Voo_n_voo PRIMARY KEY (n_voo),
CONSTRAINT fk_Voo_cod_rota FOREIGN KEY (cod_rota) REFERENCES Rota(cod_rota),	
CONSTRAINT fk_Voo_id_comandante FOREIGN KEY  (id_comandante) REFERENCES Piloto(id),
CONSTRAINT fk_Voo_copiloto FOREIGN KEY (id_copiloto) REFERENCES Piloto(id),
CONSTRAINT fk_Voo_matricula FOREIGN KEY (matricula) REFERENCES Aviao(matricula));

-- VooPcabine ( Voo.n_voo, Tripulante.id_pcabine )

CREATE TABLE VooPcabine (
n_voo	NUMERIC(4),
id_pcabine	NUMERIC(5),
CONSTRAINT pk_VooPcabine PRIMARY KEY (n_voo,id_pcabine),
CONSTRAINT fk_VooPcabine_n_voo FOREIGN KEY (n_voo) REFERENCES Voo(n_voo),
CONSTRAINT fk_VooPcabine_id_pcabine FOREIGN KEY (id_pcabine) REFERENCES Tripulante(id));


-- Regras de Integridade (as essenciais para representar em SQL  )
-- RIA-1: O atributo tipo de Tripulante toma valores no dominio (pessoal_cabine, piloto  )
-- RIA-2: O atributo tipo de Piloto toma valores no dominio (copiloto, comandante)