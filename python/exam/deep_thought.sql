-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema deep_thoughts
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema deep_thoughts
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `deep_thoughts` DEFAULT CHARACTER SET utf8 ;
USE `deep_thoughts` ;

-- -----------------------------------------------------
-- Table `deep_thoughts`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `deep_thoughts`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(110) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `modified_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `deep_thoughts`.`thoughts`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `deep_thoughts`.`thoughts` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `owner_id` INT NOT NULL,
  `description` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `modified_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`, `owner_id`),
  INDEX `fk_thoughts_users_idx` (`owner_id` ASC) VISIBLE,
  CONSTRAINT `fk_thoughts_users`
    FOREIGN KEY (`owner_id`)
    REFERENCES `deep_thoughts`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `deep_thoughts`.`likes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `deep_thoughts`.`likes` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `thought_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `modified_at` DATETIME NULL DEFAULT NOW() ON UPDATE NOW(),
  PRIMARY KEY (`id`),
  INDEX `fk_likes_thoughts1_idx` (`thought_id` ASC) VISIBLE,
  INDEX `fk_likes_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_likes_thoughts1`
    FOREIGN KEY (`thought_id`)
    REFERENCES `deep_thoughts`.`thoughts` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `deep_thoughts`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
