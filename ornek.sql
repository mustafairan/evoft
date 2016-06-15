-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: fakedb
-- ------------------------------------------------------
-- Server version	5.6.28-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Product` (
  `productID` int(11) DEFAULT NULL,
  `quality` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (20,0.692727),(13,0.300165),(15,0.595383),(5,0.512593),(14,0.8),(6,0.370882),(1,0.59118),(17,0.661941),(11,0.727689),(19,0.349106),(16,0.598568),(8,0.598026),(18,0.597898),(12,0.434504),(9,0.84017),(7,0.6),(3,0.8);
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ratings`
--

DROP TABLE IF EXISTS `Ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Ratings` (
  `userID` int(11) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  `categoryID` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ratings`
--

LOCK TABLES `Ratings` WRITE;
/*!40000 ALTER TABLE `Ratings` DISABLE KEYS */;
INSERT INTO `Ratings` VALUES (1,20,4,3),(2,20,4,3),(7,13,3,2),(1,15,3,1),(7,5,1,2),(3,14,3,4),(3,20,4,5),(5,6,1,3),(7,1,1,5),(9,17,3,3),(5,20,4,1),(1,11,3,4),(4,19,4,1),(9,16,3,4),(9,8,2,1),(6,15,3,3),(3,11,3,3),(2,18,4,1),(4,1,1,3),(10,18,4,4),(3,1,1,1),(6,13,3,1),(5,12,3,1),(9,15,3,4),(8,9,2,3),(9,20,4,4),(4,12,3,3),(3,17,3,3),(5,7,2,3),(3,19,4,1),(1,3,1,4),(6,9,2,5),(7,9,2,4),(5,15,3,5),(7,14,3,4),(4,11,3,4),(5,18,4,4),(1,19,4,3),(2,3,1,4),(1,9,2,5),(4,16,3,2),(10,20,4,4),(3,6,1,2),(2,6,1,1),(7,8,2,5),(9,9,2,4),(1,17,3,4),(4,5,1,3),(7,20,4,4),(2,15,3,2);
/*!40000 ALTER TABLE `Ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Trust`
--

DROP TABLE IF EXISTS `Trust`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Trust` (
  `trusting` int(11) DEFAULT NULL,
  `trusted` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Trust`
--

LOCK TABLES `Trust` WRITE;
/*!40000 ALTER TABLE `Trust` DISABLE KEYS */;
/*!40000 ALTER TABLE `Trust` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `expertise` float DEFAULT NULL,
  `credibility` float DEFAULT NULL,
  `userID` int(11) DEFAULT NULL,
  `categoryID` int(11) DEFAULT NULL
) ENGINE=MEMORY DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserPreference`
--

DROP TABLE IF EXISTS `UserPreference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserPreference` (
  `userID` int(11) NOT NULL,
  `categoryID` int(11) DEFAULT NULL,
  `value` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserPreference`
--

LOCK TABLES `UserPreference` WRITE;
/*!40000 ALTER TABLE `UserPreference` DISABLE KEYS */;
INSERT INTO `UserPreference` VALUES (1,1,0.121212),(1,1,0.142857),(1,2,0.142857),(1,3,0.428571),(1,4,0.285714),(2,1,0.4),(2,3,0.2),(2,4,0.4),(3,1,0.285714),(3,3,0.428571),(3,4,0.285714),(4,1,0.333333),(4,3,0.5),(4,4,0.166667),(5,1,0.166667),(5,2,0.166667),(5,3,0.333333),(5,4,0.333333),(6,2,0.333333),(6,3,0.666667),(7,1,0.285714),(7,2,0.285714),(7,3,0.285714),(7,4,0.142857),(8,2,1),(9,2,0.333333),(9,3,0.5),(9,4,0.166667),(10,4,1);
/*!40000 ALTER TABLE `UserPreference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoryAssociation`
--

DROP TABLE IF EXISTS `categoryAssociation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categoryAssociation` (
  `category1` int(11) DEFAULT NULL,
  `category2` int(11) DEFAULT NULL,
  `value` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoryAssociation`
--

LOCK TABLES `categoryAssociation` WRITE;
/*!40000 ALTER TABLE `categoryAssociation` DISABLE KEYS */;
INSERT INTO `categoryAssociation` VALUES (4,4,1),(4,3,0.875),(4,1,0.75),(4,2,0.5),(3,4,0.875),(3,3,1),(3,1,0.75),(3,2,0.625),(1,4,1),(1,3,1),(1,1,1),(1,2,0.5),(2,4,0.666667),(2,3,0.833333),(2,1,0.5),(2,2,1);
/*!40000 ALTER TABLE `categoryAssociation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-16  0:57:36
-- MySQL dump 10.13  Distrib 5.6.28, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: fakedb
-- ------------------------------------------------------
-- Server version	5.6.28-1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Product`
--

DROP TABLE IF EXISTS `Product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Product` (
  `productID` int(11) DEFAULT NULL,
  `quality` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Product`
--

LOCK TABLES `Product` WRITE;
/*!40000 ALTER TABLE `Product` DISABLE KEYS */;
INSERT INTO `Product` VALUES (20,0.692727),(13,0.300165),(15,0.595383),(5,0.512593),(14,0.8),(6,0.370882),(1,0.59118),(17,0.661941),(11,0.727689),(19,0.349106),(16,0.598568),(8,0.598026),(18,0.597898),(12,0.434504),(9,0.84017),(7,0.6),(3,0.8);
/*!40000 ALTER TABLE `Product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Ratings`
--

DROP TABLE IF EXISTS `Ratings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Ratings` (
  `userID` int(11) DEFAULT NULL,
  `productID` int(11) DEFAULT NULL,
  `categoryID` int(11) DEFAULT NULL,
  `rating` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Ratings`
--

LOCK TABLES `Ratings` WRITE;
/*!40000 ALTER TABLE `Ratings` DISABLE KEYS */;
INSERT INTO `Ratings` VALUES (1,20,4,3),(2,20,4,3),(7,13,3,2),(1,15,3,1),(7,5,1,2),(3,14,3,4),(3,20,4,5),(5,6,1,3),(7,1,1,5),(9,17,3,3),(5,20,4,1),(1,11,3,4),(4,19,4,1),(9,16,3,4),(9,8,2,1),(6,15,3,3),(3,11,3,3),(2,18,4,1),(4,1,1,3),(10,18,4,4),(3,1,1,1),(6,13,3,1),(5,12,3,1),(9,15,3,4),(8,9,2,3),(9,20,4,4),(4,12,3,3),(3,17,3,3),(5,7,2,3),(3,19,4,1),(1,3,1,4),(6,9,2,5),(7,9,2,4),(5,15,3,5),(7,14,3,4),(4,11,3,4),(5,18,4,4),(1,19,4,3),(2,3,1,4),(1,9,2,5),(4,16,3,2),(10,20,4,4),(3,6,1,2),(2,6,1,1),(7,8,2,5),(9,9,2,4),(1,17,3,4),(4,5,1,3),(7,20,4,4),(2,15,3,2);
/*!40000 ALTER TABLE `Ratings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Trust`
--

DROP TABLE IF EXISTS `Trust`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Trust` (
  `trusting` int(11) DEFAULT NULL,
  `trusted` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Trust`
--

LOCK TABLES `Trust` WRITE;
/*!40000 ALTER TABLE `Trust` DISABLE KEYS */;
/*!40000 ALTER TABLE `Trust` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `User`
--

DROP TABLE IF EXISTS `User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `User` (
  `expertise` float DEFAULT NULL,
  `credibility` float DEFAULT NULL,
  `userID` int(11) DEFAULT NULL,
  `categoryID` int(11) DEFAULT NULL
) ENGINE=MEMORY DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `User`
--

LOCK TABLES `User` WRITE;
/*!40000 ALTER TABLE `User` DISABLE KEYS */;
INSERT INTO `User` VALUES (0.4,0.5,1,1),(0.420085,0.418018,1,2),(0.496253,0.59893,1,3),(0.347278,0.555199,1,4),(0.390294,0.608754,2,1),(0.297691,0.402865,2,3),(0.430208,0.505793,2,4),(0.320687,0.528422,3,1),(0.547408,0.702503,3,3),(0.347278,0.511468,3,4),(0.367924,0.633699,4,1),(0.44019,0.641562,4,3),(0.174553,0.422743,4,4),(0.185441,0.386869,5,1),(0.3,0.5,5,2),(0.343296,0.452767,5,3),(0.430208,0.434929,5,4),(0.420085,0.418018,6,2),(0.298516,0.631335,6,3),(0.367924,0.49195,7,1),(0.479399,0.518748,7,2),(0.366722,0.633422,7,3),(0.346364,0.444459,7,4),(0.420085,0.381981,8,2),(0.479399,0.523894,9,2),(0.463973,0.632443,9,3),(0.346364,0.444459,9,4),(0.430208,0.560873,10,4);
/*!40000 ALTER TABLE `User` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `UserPreference`
--

DROP TABLE IF EXISTS `UserPreference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `UserPreference` (
  `userID` int(11) NOT NULL,
  `categoryID` int(11) DEFAULT NULL,
  `value` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `UserPreference`
--

LOCK TABLES `UserPreference` WRITE;
/*!40000 ALTER TABLE `UserPreference` DISABLE KEYS */;
INSERT INTO `UserPreference` VALUES (1,1,0.142857),(1,2,0.142857),(1,3,0.428571),(1,4,0.285714),(2,1,0.4),(2,3,0.2),(2,4,0.4),(3,1,0.285714),(3,3,0.428571),(3,4,0.285714),(4,1,0.333333),(4,3,0.5),(4,4,0.166667),(5,1,0.166667),(5,2,0.166667),(5,3,0.333333),(5,4,0.333333),(6,2,0.333333),(6,3,0.666667),(7,1,0.285714),(7,2,0.285714),(7,3,0.285714),(7,4,0.142857),(8,2,1),(9,2,0.333333),(9,3,0.5),(9,4,0.166667),(10,4,1);
/*!40000 ALTER TABLE `UserPreference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categoryAssociation`
--

DROP TABLE IF EXISTS `categoryAssociation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `categoryAssociation` (
  `category1` int(11) DEFAULT NULL,
  `category2` int(11) DEFAULT NULL,
  `value` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categoryAssociation`
--

LOCK TABLES `categoryAssociation` WRITE;
/*!40000 ALTER TABLE `categoryAssociation` DISABLE KEYS */;
INSERT INTO `categoryAssociation` VALUES (4,4,1),(4,3,0.875),(4,1,0.75),(4,2,0.5),(3,4,0.875),(3,3,1),(3,1,0.75),(3,2,0.625),(1,4,1),(1,3,1),(1,1,1),(1,2,0.5),(2,4,0.666667),(2,3,0.833333),(2,1,0.5),(2,2,1);
/*!40000 ALTER TABLE `categoryAssociation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-06-16  1:03:20
