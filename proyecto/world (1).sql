-- phpMyAdmin SQL Dump
-- version 3.4.9
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 29-11-2023 a las 15:11:45
-- Versión del servidor: 5.5.20
-- Versión de PHP: 5.3.9

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `world`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `city`
--

CREATE TABLE IF NOT EXISTS `city` (
  `ID` int(20) NOT NULL,
  `Name` varchar(35) NOT NULL,
  `CountryCode` varchar(3) NOT NULL,
  `District` varchar(20) NOT NULL,
  `Population` int(10) NOT NULL,
  `PostalCode` int(10) NOT NULL,
  `Neighborhoods` int(10) NOT NULL
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `country`
--

CREATE TABLE IF NOT EXISTS `country` (
  `Code` varchar(3) NOT NULL,
  `Name` varchar(52) NOT NULL,
  `Continent` varchar(15) NOT NULL,
  `Region` varchar(26) NOT NULL,
  `SurfaceArea` int(10) NOT NULL,
  `IndepYear` int(10) NOT NULL,
  `Population` int(10) NOT NULL,
  `LifeExpentancy` int(3) NOT NULL,
  `GNP` int(10) NOT NULL,
  `GNPOld` int(10) NOT NULL,
  `LocalName` varchar(45) NOT NULL,
  `GovernmentForm` varchar(45) NOT NULL,
  `HeadOfState` varchar(60) NOT NULL,
  `Capital` varchar(20) NOT NULL,
  `Code2` varchar(2) NOT NULL,
  `NumberCities` int(20) NOT NULL,
  `MayorsNumber` int(10) NOT NULL,
  PRIMARY KEY (`Code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `countrylanguage`
--

CREATE TABLE IF NOT EXISTS `countrylanguage` (
  `CountryCode` varchar(3) NOT NULL,
  `Language` varchar(30) NOT NULL,
  `IsOfficial` int(5) NOT NULL,
  `Percentage` int(4) NOT NULL,
  `SecondLanguage` varchar(20) NOT NULL,
  `RankingPosition` int(5) NOT NULL,
  PRIMARY KEY (`Language`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
