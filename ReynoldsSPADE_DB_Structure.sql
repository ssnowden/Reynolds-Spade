SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci ;
CREATE SCHEMA IF NOT EXISTS `ReynoldsSPADE` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;
USE `ReynoldsSPADE` ;

-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Users`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Users` (
  `UserID` INT NOT NULL AUTO_INCREMENT ,
  `FirstName` VARCHAR(45) NULL ,
  `SecondName` VARCHAR(45) NULL ,
  `Password` VARCHAR(45) NULL ,
  `AccessLevel` VARCHAR(10) NULL ,
  `DateTimeCreated` DATETIME NOT NULL ,
  `DateTimeModified` DATETIME NOT NULL ,
  PRIMARY KEY (`UserID`) ,
  UNIQUE INDEX `UserID_UNIQUE` (`UserID` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Region`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Region` (
  `RegionID` INT NOT NULL AUTO_INCREMENT ,
  `NumberOfSites` INT NULL ,
  PRIMARY KEY (`RegionID`) ,
  UNIQUE INDEX `RegionID_UNIQUE` (`RegionID` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`DistributionTypePattern`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`DistributionTypePattern` (
  `PatternID` INT NOT NULL AUTO_INCREMENT ,
  `PatternName` VARCHAR(45) NULL ,
  `PatternDescription` VARCHAR(45) NULL ,
  `Region_RegionID` INT NOT NULL ,
  PRIMARY KEY (`PatternID`) ,
  UNIQUE INDEX `PatternID_UNIQUE` (`PatternID` ASC) ,
  INDEX `fk_DistributionTypePattern_Region1_idx` (`Region_RegionID` ASC) ,
  CONSTRAINT `fk_DistributionTypePattern_Region1`
    FOREIGN KEY (`Region_RegionID` )
    REFERENCES `ReynoldsSPADE`.`Region` (`RegionID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`DistributionType`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`DistributionType` (
  `DistributionTypeID` INT NOT NULL AUTO_INCREMENT ,
  `NumberOfRegions` INT NULL ,
  `DistributionTypePattern_PatternID` INT NOT NULL ,
  PRIMARY KEY (`DistributionTypeID`) ,
  UNIQUE INDEX `DistributionTypeID_UNIQUE` (`DistributionTypeID` ASC) ,
  INDEX `fk_DistributionType_DistributionTypePattern1_idx` (`DistributionTypePattern_PatternID` ASC) ,
  CONSTRAINT `fk_DistributionType_DistributionTypePattern1`
    FOREIGN KEY (`DistributionTypePattern_PatternID` )
    REFERENCES `ReynoldsSPADE`.`DistributionTypePattern` (`PatternID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`OilDistribution`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`OilDistribution` (
  `OilDistributionID` INT NOT NULL AUTO_INCREMENT ,
  `CreatedDateTime` DATETIME NOT NULL ,
  `DistributionType_DistributionTypeID` INT NOT NULL ,
  PRIMARY KEY (`OilDistributionID`) ,
  UNIQUE INDEX `OilDistributionID_UNIQUE` (`OilDistributionID` ASC) ,
  INDEX `fk_OilDistribution_DistributionType1_idx` (`DistributionType_DistributionTypeID` ASC) ,
  CONSTRAINT `fk_OilDistribution_DistributionType1`
    FOREIGN KEY (`DistributionType_DistributionTypeID` )
    REFERENCES `ReynoldsSPADE`.`DistributionType` (`DistributionTypeID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Scenario`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Scenario` (
  `ScenarioID` INT NOT NULL AUTO_INCREMENT ,
  `DateTimeCreated` DATETIME NOT NULL ,
  `OilDistribution_OilDistributionID` INT NOT NULL ,
  PRIMARY KEY (`ScenarioID`) ,
  UNIQUE INDEX `ScenarioID_UNIQUE` (`ScenarioID` ASC) ,
  INDEX `fk_Scenario_OilDistribution1_idx` (`OilDistribution_OilDistributionID` ASC) ,
  CONSTRAINT `fk_Scenario_OilDistribution1`
    FOREIGN KEY (`OilDistribution_OilDistributionID` )
    REFERENCES `ReynoldsSPADE`.`OilDistribution` (`OilDistributionID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Experiment`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Experiment` (
  `ExperimentID` INT NOT NULL AUTO_INCREMENT ,
  `Description` VARCHAR(140) NULL ,
  `NumberOfRuns` INT NOT NULL ,
  `DateTimeCreated` DATETIME NOT NULL ,
  `Users_UserID` INT NOT NULL ,
  `Scenario_ScenarioID` INT NOT NULL ,
  PRIMARY KEY (`ExperimentID`) ,
  UNIQUE INDEX `ExperimentID_UNIQUE` (`ExperimentID` ASC) ,
  INDEX `fk_Experiment_Users_idx` (`Users_UserID` ASC) ,
  INDEX `fk_Experiment_Scenario1_idx` (`Scenario_ScenarioID` ASC) ,
  CONSTRAINT `fk_Experiment_Users`
    FOREIGN KEY (`Users_UserID` )
    REFERENCES `ReynoldsSPADE`.`Users` (`UserID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Experiment_Scenario1`
    FOREIGN KEY (`Scenario_ScenarioID` )
    REFERENCES `ReynoldsSPADE`.`Scenario` (`ScenarioID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Run`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Run` (
  `RunID` INT NOT NULL AUTO_INCREMENT ,
  `DateTimeCreated` VARCHAR(45) NOT NULL ,
  `Experiment_ExperimentID` INT NOT NULL ,
  PRIMARY KEY (`RunID`) ,
  UNIQUE INDEX `RunID_UNIQUE` (`RunID` ASC) ,
  INDEX `fk_Run_Experiment1_idx` (`Experiment_ExperimentID` ASC) ,
  CONSTRAINT `fk_Run_Experiment1`
    FOREIGN KEY (`Experiment_ExperimentID` )
    REFERENCES `ReynoldsSPADE`.`Experiment` (`ExperimentID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`AgentType`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`AgentType` (
  `AgentTypeID` INT NOT NULL AUTO_INCREMENT ,
  `Algorithm` VARCHAR(45) NOT NULL ,
  `Description` VARCHAR(140) NULL ,
  `CreatedDateTime` VARCHAR(45) NOT NULL ,
  PRIMARY KEY (`AgentTypeID`) ,
  UNIQUE INDEX `AgentTypeID_UNIQUE` (`AgentTypeID` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Agent`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Agent` (
  `AgentID` INT NOT NULL AUTO_INCREMENT ,
  `Name` VARCHAR(45) NULL ,
  `DateTimeCreated` DATETIME NOT NULL ,
  `AgentType_AgentTypeID` INT NOT NULL ,
  PRIMARY KEY (`AgentID`) ,
  UNIQUE INDEX `AgentID_UNIQUE` (`AgentID` ASC) ,
  INDEX `fk_Agent_AgentType1_idx` (`AgentType_AgentTypeID` ASC) ,
  CONSTRAINT `fk_Agent_AgentType1`
    FOREIGN KEY (`AgentType_AgentTypeID` )
    REFERENCES `ReynoldsSPADE`.`AgentType` (`AgentTypeID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Agents`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Agents` (
  `Agent_AgentID` INT NOT NULL ,
  `Experiment_ExperimentID` INT NOT NULL ,
  INDEX `fk_Agents_Agent1_idx` (`Agent_AgentID` ASC) ,
  INDEX `fk_Agents_Experiment1_idx` (`Experiment_ExperimentID` ASC) ,
  CONSTRAINT `fk_Agents_Agent1`
    FOREIGN KEY (`Agent_AgentID` )
    REFERENCES `ReynoldsSPADE`.`Agent` (`AgentID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Agents_Experiment1`
    FOREIGN KEY (`Experiment_ExperimentID` )
    REFERENCES `ReynoldsSPADE`.`Experiment` (`ExperimentID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Parameter`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Parameter` (
  `ParameterID` INT NOT NULL AUTO_INCREMENT ,
  `ParameterName` VARCHAR(45) NULL ,
  `ParameterDescription` VARCHAR(140) NULL ,
  `DateTimeCreated` DATETIME NOT NULL ,
  PRIMARY KEY (`ParameterID`) ,
  UNIQUE INDEX `ParameterID_UNIQUE` (`ParameterID` ASC) )
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`AgentParameters`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`AgentParameters` (
  `ParameterValue` INT NOT NULL ,
  `DateTimeCreated` VARCHAR(45) NOT NULL ,
  `Agent_AgentID` INT NOT NULL ,
  `Parameter_ParameterID` INT NOT NULL ,
  INDEX `fk_AgentParameters_Agent1_idx` (`Agent_AgentID` ASC) ,
  INDEX `fk_AgentParameters_Parameter1_idx` (`Parameter_ParameterID` ASC) ,
  CONSTRAINT `fk_AgentParameters_Agent1`
    FOREIGN KEY (`Agent_AgentID` )
    REFERENCES `ReynoldsSPADE`.`Agent` (`AgentID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_AgentParameters_Parameter1`
    FOREIGN KEY (`Parameter_ParameterID` )
    REFERENCES `ReynoldsSPADE`.`Parameter` (`ParameterID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Expectation`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Expectation` (
  `ExpectationID` INT NOT NULL AUTO_INCREMENT ,
  `ExpectationValue` INT NULL ,
  `DateTimeCreated` DATETIME NOT NULL ,
  `Region_RegionID` INT NOT NULL ,
  PRIMARY KEY (`ExpectationID`) ,
  UNIQUE INDEX `ExpectationID_UNIQUE` (`ExpectationID` ASC) ,
  INDEX `fk_Expectation_Region1_idx` (`Region_RegionID` ASC) ,
  CONSTRAINT `fk_Expectation_Region1`
    FOREIGN KEY (`Region_RegionID` )
    REFERENCES `ReynoldsSPADE`.`Region` (`RegionID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Expectations`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Expectations` (
  `CreatedDateTime` DATETIME NOT NULL ,
  `Agent_AgentID` INT NOT NULL ,
  `Expectation_ExpectationID` INT NOT NULL ,
  INDEX `fk_Expectations_Agent1_idx` (`Agent_AgentID` ASC) ,
  INDEX `fk_Expectations_Expectation1_idx` (`Expectation_ExpectationID` ASC) ,
  CONSTRAINT `fk_Expectations_Agent1`
    FOREIGN KEY (`Agent_AgentID` )
    REFERENCES `ReynoldsSPADE`.`Agent` (`AgentID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Expectations_Expectation1`
    FOREIGN KEY (`Expectation_ExpectationID` )
    REFERENCES `ReynoldsSPADE`.`Expectation` (`ExpectationID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`DistributionRegions`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`DistributionRegions` (
  `OilDistribution_OilDistributionID` INT NOT NULL ,
  `Region_RegionID` INT NOT NULL ,
  INDEX `fk_DistributionRegions_OilDistribution1_idx` (`OilDistribution_OilDistributionID` ASC) ,
  INDEX `fk_DistributionRegions_Region1_idx` (`Region_RegionID` ASC) ,
  CONSTRAINT `fk_DistributionRegions_OilDistribution1`
    FOREIGN KEY (`OilDistribution_OilDistributionID` )
    REFERENCES `ReynoldsSPADE`.`OilDistribution` (`OilDistributionID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_DistributionRegions_Region1`
    FOREIGN KEY (`Region_RegionID` )
    REFERENCES `ReynoldsSPADE`.`Region` (`RegionID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `ReynoldsSPADE`.`Site`
-- -----------------------------------------------------
CREATE  TABLE IF NOT EXISTS `ReynoldsSPADE`.`Site` (
  `SiteID` INT NOT NULL AUTO_INCREMENT ,
  `AmountOfOil` INT NULL ,
  `IsExplored` TINYINT(1) NOT NULL ,
  `DateTimeExplored` DATETIME NOT NULL ,
  `DateTimeCreated` DATETIME NOT NULL ,
  `Region_RegionID` INT NOT NULL ,
  `Agent_AgentID` INT NOT NULL ,
  PRIMARY KEY (`SiteID`) ,
  UNIQUE INDEX `SiteID_UNIQUE` (`SiteID` ASC) ,
  INDEX `fk_Site_Region1_idx` (`Region_RegionID` ASC) ,
  INDEX `fk_Site_Agent1_idx` (`Agent_AgentID` ASC) ,
  CONSTRAINT `fk_Site_Region1`
    FOREIGN KEY (`Region_RegionID` )
    REFERENCES `ReynoldsSPADE`.`Region` (`RegionID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Site_Agent1`
    FOREIGN KEY (`Agent_AgentID` )
    REFERENCES `ReynoldsSPADE`.`Agent` (`AgentID` )
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
