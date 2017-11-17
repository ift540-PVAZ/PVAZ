

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';
-- -----------------------------------------------------
-- Schema PVAZ
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `PVAZ` DEFAULT CHARACTER SET utf8 ;
USE `PVAZ` ;

-- -----------------------------------------------------
-- Table `PVAZ`.`Manufacturer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PVAZ`.`Manufacturer` (
  `ManufacturerID` INT NOT NULL AUTO_INCREMENT,
  `ManufacturerName` VARCHAR(45) NULL,
  `AuthorityName` VARCHAR(45) NULL,
  `Phone` VARCHAR(45) NULL,
  `Email` VARCHAR(45) NULL,
  `Fax` VARCHAR(45) NULL,
  `ApplicantName` VARCHAR(45) NULL,
  `Location` VARCHAR(45) NULL,
  PRIMARY KEY (`ManufacturerID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PVAZ`.`PerformanceParameters`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PVAZ`.`PerformanceParameters` (
  `PerformanceID` INT NOT NULL AUTO_INCREMENT,
  `Power` DOUBLE NULL,
  `Voltage` DOUBLE NULL,
  `Current` DOUBLE NULL,
  `TemperatureCoefficient` DOUBLE NULL,
  PRIMARY KEY (`PerformanceID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PVAZ`.`SolarPanel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PVAZ`.`SolarPanel` (
  `ModelID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `ModelNumber` INT NULL,
  `DesignSpecificationID` VARCHAR(45) NULL,
  `Manufacturer_ManufacturerID` INT NOT NULL,
  `PerformanceParameters_PerformanceID` INT NOT NULL,
  PRIMARY KEY (`ModelID`, `Manufacturer_ManufacturerID`, `PerformanceParameters_PerformanceID`),
  INDEX `fk_SolarPanel_Manufacturer1_idx` (`Manufacturer_ManufacturerID` ASC),
  INDEX `fk_SolarPanel_PerformanceParameters1_idx` (`PerformanceParameters_PerformanceID` ASC),
  CONSTRAINT `fk_SolarPanel_Manufacturer1`
    FOREIGN KEY (`Manufacturer_ManufacturerID`)
    REFERENCES `PVAZ`.`Manufacturer` (`ManufacturerID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SolarPanel_PerformanceParameters1`
    FOREIGN KEY (`PerformanceParameters_PerformanceID`)
    REFERENCES `PVAZ`.`PerformanceParameters` (`PerformanceID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PVAZ`.`TestCondition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PVAZ`.`TestCondition` (
  `Name` VARCHAR(45) NOT NULL,
  `Irradiance` DOUBLE NULL,
  `AmbientTemperature` DOUBLE NULL,
  `AirMass` DOUBLE NULL,
  `WindSpeed` DOUBLE NULL,
  PRIMARY KEY (`Name`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PVAZ`.`DesignSpecifications`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PVAZ`.`DesignSpecifications` (
  `DesignSpecificationID` INT NOT NULL AUTO_INCREMENT,
  `SolarPanel_ModelID` INT NOT NULL,
  `ModelNumber` INT NULL,
  `Manufacturer` VARCHAR(45) NULL,
  `Size` DOUBLE NULL,
  `Material` VARCHAR(45) NULL,
  `TotalNoOfCells` INT NULL,
  `Encapsulant` VARCHAR(45) NULL,
  `FrontDesign` VARCHAR(45) NULL,
  `BackDesign` VARCHAR(45) NULL,
  `TypeModelDesignation` VARCHAR(45) NULL,
  `ModelManufacturingDate` DATETIME NULL,
  `ModuleTotalArea` DOUBLE NULL,
  `ModuleWeight` DOUBLE NULL,
  `IndividualCellArea` DOUBLE NULL,
  `CellTechnology` VARCHAR(45) NULL,
  `CellManufacturerAndPartNo` VARCHAR(45) NULL,
  `CellManufacturingLocation` VARCHAR(45) NULL,
  `NoOfCellsInSeries` INT NULL,
  `NoOfCellsInParallel` INT NULL,
  `NoOfBypassDiodes` INT NULL,
  `BypassDiodeRating` DOUBLE NULL,
  `BypassDiodeMaxJunctionTemp` DOUBLE NULL,
  `SeriesFuseRating` DOUBLE NULL,
  `InterconnectMaterialAndSupplierModelNo` VARCHAR(45) NULL,
  `SuperstrateType` VARCHAR(45) NULL,
  `SuperstrateManufacturerAndPartNo` VARCHAR(45) NULL,
  `SubstrateType` VARCHAR(45) NULL,
  `SubstrateManufacturerAndPartNo` VARCHAR(45) NULL,
  `FrameTypeMaterial` VARCHAR(45) NULL,
  `FrameAdhesive` VARCHAR(45) NULL,
  `EncapsulantType` VARCHAR(45) NULL,
  `EncapsulantManufacturerAndPartNo` VARCHAR(45) NULL,
  `JunctionBoxType` VARCHAR(45) NULL,
  `JunctionBoxManufacturerAndPartNo` VARCHAR(45) NULL,
  `JunctionBoxPlottingMaterial` VARCHAR(45) NULL,
  `JunctionBoxAdhesive` VARCHAR(45) NULL,
  `CableAndConnectorType` VARCHAR(45) NULL,
  `MaximumSystemVoltage` DOUBLE NULL,
  PRIMARY KEY (`DesignSpecificationID`, `SolarPanel_ModelID`),
  INDEX `fk_DesignSpecifications_SolarPanel_idx` (`SolarPanel_ModelID` ASC),
  CONSTRAINT `fk_DesignSpecifications_SolarPanel`
    FOREIGN KEY (`SolarPanel_ModelID`)
    REFERENCES `PVAZ`.`SolarPanel` (`ModelID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `PVAZ`.`SolarPanel_has_TestCondition`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `PVAZ`.`SolarPanel_has_TestCondition` (
  `SolarPanel_ModelID` INT NOT NULL,
  `TestCondition_Name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`SolarPanel_ModelID`, `TestCondition_Name`),
  INDEX `fk_SolarPanel_has_TestCondition_TestCondition1_idx` (`TestCondition_Name` ASC),
  INDEX `fk_SolarPanel_has_TestCondition_SolarPanel1_idx` (`SolarPanel_ModelID` ASC),
  CONSTRAINT `fk_SolarPanel_has_TestCondition_SolarPanel1`
    FOREIGN KEY (`SolarPanel_ModelID`)
    REFERENCES `PVAZ`.`SolarPanel` (`ModelID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_SolarPanel_has_TestCondition_TestCondition1`
    FOREIGN KEY (`TestCondition_Name`)
    REFERENCES `PVAZ`.`TestCondition` (`Name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;  
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;