-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Nov 08, 2021 at 06:58 PM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pokedex`
--

-- --------------------------------------------------------

--
-- Table structure for table `pokemon`
--

CREATE TABLE `pokemon` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL,
  `tipo` varchar(60) DEFAULT NULL,
  `age` int(11) NOT NULL,
  `birthdate` varchar(15) NOT NULL,
  `principalattack` varchar(50) NOT NULL,
  `picture` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pokemon`
--

INSERT INTO `pokemon` (`id`, `name`, `tipo`, `age`, `birthdate`, `principalattack`, `picture`) VALUES
(1, 'Pikachu', 'Electrico', 10, '15/06/2011', 'Electrobola', 'https://static.wikia.nocookie.net/doblaje/images/a/aa/Pikachu_XY.png/revision/latest?cb=20161002184039&path-prefix=es'),
(3, 'Squirtle', 'Agua', 16, '14/06/2005', 'HidroTornado', 'https://assets.pokemon.com/assets/cms2/img/pokedex/full/007.png');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pokemon`
--
ALTER TABLE `pokemon`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pokemon`
--
ALTER TABLE `pokemon`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
