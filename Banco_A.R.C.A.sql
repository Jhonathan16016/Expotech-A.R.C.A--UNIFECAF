CREATE DATABASE  IF NOT EXISTS `arca` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `arca`;
-- MySQL dump 10.13  Distrib 8.0.46, for Win64 (x86_64)
--
-- Host: localhost    Database: arca
-- ------------------------------------------------------
-- Server version	8.0.46

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `controle_dispositivo`
--

DROP TABLE IF EXISTS `controle_dispositivo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `controle_dispositivo` (
  `controle_id` int NOT NULL AUTO_INCREMENT,
  `usuario_iid` int DEFAULT NULL,
  `disp_iid` int DEFAULT NULL,
  PRIMARY KEY (`controle_id`),
  KEY `usuario_iid` (`usuario_iid`),
  KEY `disp_iid` (`disp_iid`),
  CONSTRAINT `controle_dispositivo_ibfk_1` FOREIGN KEY (`usuario_iid`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE,
  CONSTRAINT `controle_dispositivo_ibfk_2` FOREIGN KEY (`disp_iid`) REFERENCES `dispositivo_smart` (`disp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `controle_dispositivo`
--

LOCK TABLES `controle_dispositivo` WRITE;
/*!40000 ALTER TABLE `controle_dispositivo` DISABLE KEYS */;
/*!40000 ALTER TABLE `controle_dispositivo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dispositivo_smart`
--

DROP TABLE IF EXISTS `dispositivo_smart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dispositivo_smart` (
  `disp_id` int NOT NULL AUTO_INCREMENT,
  `disp_nome` varchar(100) NOT NULL,
  `disp_tipo` varchar(100) NOT NULL,
  `disp_status` varchar(100) NOT NULL,
  `disp_comodo` varchar(100) NOT NULL,
  `disp_temperatura` float DEFAULT NULL,
  PRIMARY KEY (`disp_id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dispositivo_smart`
--

LOCK TABLES `dispositivo_smart` WRITE;
/*!40000 ALTER TABLE `dispositivo_smart` DISABLE KEYS */;
INSERT INTO `dispositivo_smart` VALUES (1,'Porta da sala','porta','Fechada','Sala',NULL),(2,'Janela da sala','janela','Aberta','Sala',NULL),(3,'Cortinha da sala','cortina','Fechada','Sala',NULL),(4,'Luz da sala','luz','Desligada','Sala',NULL),(5,'Ar-Condicionado da sala','arcondicionado','Ligado - modo Frio','Sala',18),(6,'Televisão da sala','tv','Ligada','Sala',NULL),(7,'Luz da cozinha','luz','Desligada','Cozinha',NULL),(8,'Fogão da cozinha','fogao','Desligado','Cozinha',25),(9,'Janela da cozinha','janela','Fechada','Cozinha',NULL),(10,'Porta do quarto','porta','Fechada','Quarto das Crianças',NULL),(11,'Janela do quarto','janela','Fechada','Quarto das Crianças',NULL),(12,'Cortina do quarto','cortina','Fechada','Quarto das Crianças',NULL),(13,'Luz do quarto','luz','Ligada','Quarto das Crianças',NULL),(14,'Ar-Condicionado do quarto','arcondicionado','Ligado - modo Frio','Quarto das Crianças',18),(15,'Televisão do quarto','tv','Desligada','Quarto das Crianças',NULL),(16,'Porta do quarto','porta','Fechada','Quarto dos Adultos',NULL),(17,'Janela do quarto','janela','Fechada','Quarto dos Adultos',NULL),(18,'Cortina do quarto','cortina','Fechada','Quarto dos Adultos',NULL),(19,'Luz do quarto','luz','Desligada','Quarto dos Adultos',NULL),(20,'Ar-Condicionado do quarto','arcondicionado','Ligado - modo Quente','Quarto dos Adultos',30),(21,'Televisão do quarto','tv','Desligada','Quarto dos Adultos',NULL),(22,'Porta do banheiro','porta','Fechada','Banheiro',NULL),(23,'Janela do banheiro','janela','Fechada','Banheiro',NULL),(24,'Luz do banheiro','luz','Desligada','Banheiro',NULL),(25,'Privada Inteligente','privada','Desligado','Banheiro',17),(26,'Porta da lavanderia','porta','Fechada','Lavanderia',NULL),(27,'Janela da lavanderia','janela','Fechada','Lavanderia',NULL),(28,'Luz da lavanderia','luz','Desligada','Lavanderia',NULL),(29,'Maquina de Lavar','maquina','Desligado','Lavanderia',NULL);
/*!40000 ALTER TABLE `dispositivo_smart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico_jogo`
--

DROP TABLE IF EXISTS `historico_jogo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico_jogo` (
  `historico_id` int NOT NULL AUTO_INCREMENT,
  `usuario_iid` int DEFAULT NULL,
  `jogo_iid` int DEFAULT NULL,
  `score` int DEFAULT NULL,
  PRIMARY KEY (`historico_id`),
  KEY `usuario_iid` (`usuario_iid`),
  KEY `jogo_iid` (`jogo_iid`),
  CONSTRAINT `historico_jogo_ibfk_1` FOREIGN KEY (`usuario_iid`) REFERENCES `usuario` (`usuario_id`) ON DELETE CASCADE,
  CONSTRAINT `historico_jogo_ibfk_2` FOREIGN KEY (`jogo_iid`) REFERENCES `jogo_arcade` (`jogo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico_jogo`
--

LOCK TABLES `historico_jogo` WRITE;
/*!40000 ALTER TABLE `historico_jogo` DISABLE KEYS */;
INSERT INTO `historico_jogo` VALUES (1,2,1,1300),(2,4,2,560),(3,1,4,2200),(4,3,5,3000);
/*!40000 ALTER TABLE `historico_jogo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jogo_arcade`
--

DROP TABLE IF EXISTS `jogo_arcade`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jogo_arcade` (
  `jogo_id` int NOT NULL AUTO_INCREMENT,
  `jogo_nome` varchar(100) NOT NULL,
  `jogo_sistema_emulador` varchar(100) NOT NULL,
  `jogo_tempo_jogado_minutos` int DEFAULT '0',
  PRIMARY KEY (`jogo_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jogo_arcade`
--

LOCK TABLES `jogo_arcade` WRITE;
/*!40000 ALTER TABLE `jogo_arcade` DISABLE KEYS */;
INSERT INTO `jogo_arcade` VALUES (1,'Cadillacs and Dinosaurs','MAME',0),(2,'Super Mario World','SNES',0),(3,'Ultimate Mortal Kombat 3 ','SNES',0),(4,'Pac-Man','MAME',0),(5,'Metal Slug X','MAME',0);
/*!40000 ALTER TABLE `jogo_arcade` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuario` (
  `usuario_id` int NOT NULL AUTO_INCREMENT,
  `usuario_nome` varchar(255) NOT NULL,
  `usuario_login` varchar(255) NOT NULL,
  `usuario_senha` varchar(255) NOT NULL,
  `usuario_posicao` varchar(255) NOT NULL,
  PRIMARY KEY (`usuario_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuario`
--

LOCK TABLES `usuario` WRITE;
/*!40000 ALTER TABLE `usuario` DISABLE KEYS */;
INSERT INTO `usuario` VALUES (1,'Samantha Souza','Samantha.So','scrypt:32768:8:1$ccraA8nP35GCYrhe$e3f3a9b18fb1c0cf882f9e166d6e3c5b7d0f3c76a44ab121c06745b431b44f2adbf5a06ef626bacb04d48eaa17db5ee457302f2615244db4ccd7059ec3adbfc0','ADMINISTRADOR'),(2,'Fernando Kaxinawa','Fernando.Ka','scrypt:32768:8:1$q6GZLnFku6OVIXGN$0c6aec79d93f16db26ca228f739ef6e45de389b765c52a28468ab2eda41eda489337ccd4a8b85ae3ce931b1d623548549e344f1281c275a1e5f9a8c93fa75a63','ADMINISTRADOR'),(3,'Raoni Souza Kaxinawa','Raoni.So','scrypt:32768:8:1$FUTHnnbXpPoMgXdL$69f46c407db30a2acb9f30f387575677c314a5d710873c58b26db473abd98ad34d9a9c988cb7c172a473f7b32893b67f3f743ac9f410f19709bd4d8cb8c789d0','MORADOR'),(4,'Moara Souza Kaxinawa','Moara.So','scrypt:32768:8:1$aUtWjXxdvRGVQ2J1$0d2bfc706c7873de5d0b93758f5769ea5a695990a9d0bcee8a53387da9d3aa5146e2b4f154f1408207e4d55c524fc7e32f1e50fd2c06833a6df5b969b54b6310','MORADOR');
/*!40000 ALTER TABLE `usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'arca'
--

--
-- Dumping routines for database 'arca'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-11-08 14:54:33
