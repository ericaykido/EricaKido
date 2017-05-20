CREATE DATABASE 'cloud';

CREATE TABLE 'complains' (
  'idComplain' int(100) NOT NULL AUTO_INCREMENT,
  'idImovel' int(100) NOT NULL,
  'typeComplain' varchar(100) NOT NULL,
  'characteristics' varchar(500) NOT NULL,
  PRIMARY KEY ('idComplain'),
  KEY 'fk_idImovelComplain' ('idImovel'),
  CONSTRAINT 'fk_idImovelComplain' FOREIGN KEY ('idImovel') REFERENCES 'imovel' ('idImovel')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'imobiliaria' (
  'idImobialiaria' int(100) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY ('idImobialiaria')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'imovel' (
  'idImovel' int(100) NOT NULL AUTO_INCREMENT,
  'characteristics' varchar(500) NOT NULL,
  'image' varchar(500),
  'idUserInquilino' int(100),
  'idUserOwner' int(100)
  CONSTRAINT 'fk_idUserInquilino' FOREIGN KEY ('idUserInquilino') REFERENCES 'inquilino' ('idInquilino'),
  CONSTRAINT 'fk_idUserOwner' FOREIGN KEY ('idUserInquilino') REFERENCES 'owner' ('idOwner')
  PRIMARY KEY ('idImovel')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'inquilino' (
  'idInquilino' int(100) NOT NULL AUTO_INCREMENT,
  'idUserInquilino' int(100) NOT NULL,
  'cpf' varchar(20) NOT NULL,
  'name' varchar(100) NOT NULL,
  'lastName' varchar(100) NOT NULL,
  'boleto' boolean NOT NULL,
  PRIMARY KEY ('idInquilino'),
  UNIQUE KEY 'idUserInquilino' ('idUserInquilino'),
  UNIQUE KEY 'cpf' ('cpf'),
  CONSTRAINT 'fk_idUserInquilino' FOREIGN KEY ('idUserInquilino') REFERENCES 'users' ('userID')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'owner' (
  'idOwner' int(100) NOT NULL AUTO_INCREMENT,
  'idUserOwner' int(10) NOT NULL,
  'name' varchar(100) NOT NULL,
  'lastName' varchar(100) NOT NULL,
  'cpf' varchar(20) NOT NULL,
  'idHouseOwner'
  PRIMARY KEY ('idOwner'),
  UNIQUE KEY 'idUserOwner' ('idUserOwner'),
  UNIQUE KEY 'cpf' ('cpf'),
  CONSTRAINT 'fk_idUserOwner' FOREIGN KEY ('idUserOwner') REFERENCES 'users' ('userID'),
  CONSTRAINT 'fk_idHouseOwner' FOREIGN KEY ('idHouseOwner') REFERENCES 'house' ('idHouse')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'house'(
  'idHouse' int(100) NOT NULL AUTO_INCREMENT,
  'street' varchar(100) NOT NULL,
  'cep' varchar(10) NOT NULL,
  'neighborhood' varchar(100) NOT NULL,
  'city' varchar(50) NOT NULL,
  'state' varchar(50) NOT NULL,
  'complemento' varchar(20) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'repair' (
  'idRepair' int(100) NOT NULL AUTO_INCREMENT,
  'typeRepair' varchar(100) NOT NULL,
  'characteristics' varchar(500) NOT NULL,
  'idImovelRepair' int(100) NOT NULL,
  PRIMARY KEY ('idRepair'),
  KEY 'fk_idImovel' ('idImovelRepair'),
  CONSTRAINT 'fk_idImovel' FOREIGN KEY ('idImovelRepair') REFERENCES 'imovel' ('idImovel')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE 'users' (
  'userID' int(100) NOT NULL AUTO_INCREMENT,
  'name' varchar(100) NOT NULL,
  'email' varchar(100) NOT NULL,
  'lastName' varchar(100) NOT NULL,
  'password' varchar(100) NOT NULL,
  'typeUser' int(10) NOT NULL,
  'status' boolean NOT NULL,
  PRIMARY KEY ('userID'),
  KEY 'id' ('userID'),
  KEY 'idx_users_id' ('userID')
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
