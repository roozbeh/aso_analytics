-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema keywords
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema keywords
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `keywords` DEFAULT CHARACTER SET utf8 ;
USE `keywords` ;

-- -----------------------------------------------------
-- Table `keywords`.`app`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `keywords`.`app` ;

CREATE TABLE IF NOT EXISTS `keywords`.`app` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `url` VARCHAR(1024) NULL,
  `type` ENUM('ios', 'android') NULL,
  `app_id` INT NULL,
  `created` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `keywords`.`keyword`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `keywords`.`keyword` ;

CREATE TABLE IF NOT EXISTS `keywords`.`keyword` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `keyword` VARCHAR(128) NULL,
  `app_id` INT NOT NULL,
  `source` ENUM('name', 'description') NULL,
  `created` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `keyword_app_id_idx` (`app_id` ASC),
  CONSTRAINT `keyword_app_id`
    FOREIGN KEY (`app_id`)
    REFERENCES `keywords`.`app` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
