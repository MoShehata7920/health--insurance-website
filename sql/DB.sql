CREATE SCHEMA IF NOT EXISTS `healthInsurance` ;
USE `healthInsurance` ;


DROP TABLE IF EXISTS `healthInsurance`.`plane` ;

CREATE TABLE IF NOT EXISTS `healthInsurance`.`plane` (
  `P_id` INT NOT NULL AUTO_INCREMENT,
  `P_name` VARCHAR(45) NULL,
  `Price` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`P_id`)
  );



DROP TABLE IF EXISTS `healthInsurance`.`Customers` ;

CREATE TABLE IF NOT EXISTS `healthInsurance`.`Customers` (
  `C_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NULL,
  `birth_date` DATE NULL,
  `gender` VARCHAR(1) NULL,
  `income` INT NULL,
  `address` VARCHAR(50) NULL,
  `phone` VARCHAR(14) NULL,
  `has_chronic_dis` TINYINT NULL,
  `tall` INT NULL,
  `weight` INT NULL,
  `email` VARCHAR(60) NULL,
  `plane` INT NOT NULL,
  PRIMARY KEY (`C_id`),
    FOREIGN KEY (`plane`)
    REFERENCES `healthInsurance`.`plane` (`P_id`)
    )


DROP TABLE IF EXISTS `healthInsurance`.`hospital` ;

CREATE TABLE IF NOT EXISTS `healthInsurance`.`hospital` (
  `H_id` INT NOT NULL AUTO_INCREMENT,
  `H_name` VARCHAR(40) NOT NULL,
  `phone` VARCHAR(14) NULL,
  `address` VARCHAR(60) NULL,
  `email` VARCHAR(60) NULL,
  `website` VARCHAR(150) NULL,
  PRIMARY KEY (`H_id`));


DROP TABLE IF EXISTS `healthInsurance`.`dependant` ;

CREATE TABLE IF NOT EXISTS `healthInsurance`.`dependant` (
  `D_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(60) NULL,
  `birth_date` DATE NULL,
  `plane` INT NOT NULL,
  `belongs_to` INT NOT NULL,
  PRIMARY KEY (`D_id`),
    FOREIGN KEY (`plane`)
    REFERENCES `healthInsurance`.`plane` (`P_id`),
    FOREIGN KEY (`belongs_to`)
    REFERENCES `healthInsurance`.`Customers` (`C_id`)
);
 

DROP TABLE IF EXISTS `healthInsurance`.`insurance_claim` ;

CREATE TABLE IF NOT EXISTS `healthInsurance`.`insurance_claim` (
  `IC_claim` INT NOT NULL AUTO_INCREMENT,
  `amount` INT NOT NULL,
  `date` DATE NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `status` VARCHAR(45) NULL,
  `mainly_for` INT NOT NULL,
  `dependant` INT ,
  `hospital` INT NOT NULL,
  PRIMARY KEY (`IC_claim`),
    FOREIGN KEY (`mainly_for`)
    REFERENCES `healthInsurance`.`Customers` (`C_id`),
    FOREIGN KEY (`dependant`)
    REFERENCES `healthInsurance`.`dependant` (`D_id`),
    FOREIGN KEY (`hospital`)
    REFERENCES `healthInsurance`.`hospital` (`H_id`));


DROP TABLE IF EXISTS `healthInsurance`.`hospital_planes` ;

CREATE TABLE IF NOT EXISTS `healthInsurance`.`hospital_planes` (
  `hospital` INT NOT NULL,
  `plane` INT NOT NULL,
    FOREIGN KEY (`hospital`)
    REFERENCES `healthInsurance`.`hospital` (`H_id`),
    FOREIGN KEY (`plane`)
    REFERENCES `healthInsurance`.`plane` (`P_id`));



DROP TABLE IF EXISTS `healthInsurance`.`Expenses` ;

CREATE TABLE IF NOT EXISTS `healthInsurance`.`Expenses` (
  `E_id` INT NOT NULL,
  `amount` INT NOT NULL,
  `date` DATE ,
  `Customer` INT NOT NULL,
  PRIMARY KEY (`E_id`),
  FOREIGN KEY (`Customer`)
    REFERENCES `healthInsurance`.`Customers` (`C_id`))

