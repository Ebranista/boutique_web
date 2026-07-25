-- MySQL dump 10.13  Distrib 8.0.44, for Win64 (x86_64)
--
-- Host: localhost    Database: boutique_db
-- ------------------------------------------------------
-- Server version	8.0.44

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('76626e286293');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `audit_logs`
--

DROP TABLE IF EXISTS `audit_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audit_logs` (
  `user_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `action` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `entity_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `entity_id` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `old_value` text COLLATE utf8mb4_unicode_ci,
  `new_value` text COLLATE utf8mb4_unicode_ci,
  `ip_address` varchar(45) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_agent` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `request_method` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `request_path` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `error_message` text COLLATE utf8mb4_unicode_ci,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `audit_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audit_logs`
--

LOCK TABLES `audit_logs` WRITE;
/*!40000 ALTER TABLE `audit_logs` DISABLE KEYS */;
/*!40000 ALTER TABLE `audit_logs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `brands`
--

DROP TABLE IF EXISTS `brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `brands` (
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_brands_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `brands`
--

LOCK TABLES `brands` WRITE;
/*!40000 ALTER TABLE `brands` DISABLE KEYS */;
INSERT INTO `brands` VALUES ('Nike-7852 (Updated)','Nike Activewear - Updated Description','16f405b2-d310-4a08-bdf6-192134a53cb5','2026-07-10 13:21:50','2026-07-10 13:23:51',1,'2026-07-10 13:23:51'),('Nike','Nike Activewear','207c7e1a-3d9e-44e8-a00d-6950faded093','2026-07-09 11:18:31','2026-07-09 11:18:31',0,NULL),('Brand 17837161771760 Updated','Brand updated','23b4ffff-3cd3-4b44-8c00-5dd4d2152abb','2026-07-10 20:43:38','2026-07-10 20:45:09',1,'2026-07-10 20:45:09'),('Nike-1583 (Updated)','Nike Activewear - Updated Description','4f156fc6-d3be-4b29-8b8f-7c2405fca7d2','2026-07-10 13:41:13','2026-07-10 13:43:15',1,'2026-07-10 13:43:15'),('Brand 17837174432023 Updated','Brand updated','54e814bb-4a90-4a21-8461-4c4080fb456d','2026-07-10 21:04:44','2026-07-10 21:04:48',0,NULL),('Nike-3275 (Updated)','Nike Activewear - Updated Description','60f674aa-db58-4753-891f-aae9dee32137','2026-07-10 13:38:21','2026-07-10 13:40:23',1,'2026-07-10 13:40:23'),('Brand 17839721726790 B','Brand B','70080bac-5454-4eb1-89ed-50d0c4005364','2026-07-13 19:50:15','2026-07-13 19:50:19',1,'2026-07-13 19:50:19'),('Nike-6071 (Updated)','Nike Activewear - Updated Description','70b683f5-6e43-4bbb-aa3c-9d89158225ec','2026-07-09 13:34:35','2026-07-09 13:36:06',1,'2026-07-09 13:36:06'),('Nike (Updated)','Nike Activewear - Updated Description','80d84645-676e-4cb8-912d-dba55c1a01ba','2026-07-09 08:23:01','2026-07-09 08:56:39',0,NULL),('Nike-2069 (Updated)','Nike Activewear - Updated Description','964c3ac9-4e74-40a7-838d-f7f6d04196e4','2026-07-09 13:27:19','2026-07-09 13:28:42',1,'2026-07-09 13:28:42'),('Nike-4376 (Updated)','Nike Activewear - Updated Description','abeeaacb-30a8-42a8-a66d-4a9f961bc2d2','2026-07-10 11:46:13','2026-07-10 11:48:11',1,'2026-07-10 11:48:11'),('Nike-6287 (Updated)','Nike Activewear - Updated Description','c2aff1df-c638-4d7f-aa30-73ba76318c0a','2026-07-10 11:06:04','2026-07-10 11:07:37',1,'2026-07-10 11:07:37'),('puma','puma','c55cb019-6c13-49e5-b9a1-3dfe5df36dc9','2026-07-10 21:25:24','2026-07-10 21:25:24',0,NULL),('Brand 17837174432023 B','Brand B','c8c545d1-b5bf-4723-bbe5-3a32caf26704','2026-07-10 21:04:46','2026-07-10 21:04:50',1,'2026-07-10 21:04:50'),('Brand 17839721726790 Updated','Brand updated','d4623434-a928-4c2d-8c75-70ee8989ab47','2026-07-13 19:50:13','2026-07-13 19:50:17',0,NULL),('Nike-4341 (Updated)','Nike Activewear - Updated Description','dc63fe4b-1301-4456-b0d4-f28d8cb6dca0','2026-07-10 11:38:11','2026-07-10 11:40:06',1,'2026-07-10 11:40:06'),('Brand 17837161771760 B','Brand B','f032a7aa-f8f2-4935-a8cb-5db9bd1f9a70','2026-07-10 20:43:40','2026-07-10 20:43:45',1,'2026-07-10 20:43:45');
/*!40000 ALTER TABLE `brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `capital`
--

DROP TABLE IF EXISTS `capital`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `capital` (
  `beginning_capital` decimal(12,2) DEFAULT NULL,
  `current_capital` decimal(12,2) DEFAULT NULL,
  `total_invested` decimal(12,2) DEFAULT NULL,
  `total_withdrawn` decimal(12,2) DEFAULT NULL,
  `period_start` datetime NOT NULL,
  `period_end` datetime DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `capital`
--

LOCK TABLES `capital` WRITE;
/*!40000 ALTER TABLE `capital` DISABLE KEYS */;
INSERT INTO `capital` VALUES (0.00,600.00,2500.00,1900.00,'2026-07-09 08:17:27',NULL,1,'5ae2993a-1e4e-4919-a387-d0e2f84deddc','2026-07-09 08:17:27','2026-07-13 19:50:57',0,NULL);
/*!40000 ALTER TABLE `capital` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_categories_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES ('Category 17837161771760 B','Category B','23845fa1-0787-4956-8b4d-e5d6e99e1146','2026-07-10 20:43:32','2026-07-10 20:43:36',1,'2026-07-10 20:43:36'),('Category 17837161771760 Updated','Category updated','2dab9132-69c2-458d-a33a-84b83335fa00','2026-07-10 20:43:30','2026-07-10 20:45:07',1,'2026-07-10 20:45:07'),('T-Shirts-4376 (Updated)','Premium Cotton T-Shirts - Updated Description','36450278-b665-4bf0-b665-441e0308fe35','2026-07-10 11:46:11','2026-07-10 11:48:13',1,'2026-07-10 11:48:13'),('T-Shirts (Updated)','Premium Cotton T-Shirts - Updated Description','365708fd-1af5-4e5f-9741-5c36e7e75c10','2026-07-09 08:19:51','2026-07-09 08:56:35',0,NULL),('T-Shirts-6287 (Updated)','Premium Cotton T-Shirts - Updated Description','4590dd4c-764d-46ef-81b7-abcc9b0206a3','2026-07-10 11:06:02','2026-07-10 11:07:39',1,'2026-07-10 11:07:39'),('T-Shirts','Premium Cotton T-Shirts','4d0c310c-9de4-4528-8158-86eed7aa9840','2026-07-09 11:18:29','2026-07-09 11:18:29',0,NULL),('T-Shirts-1583 (Updated)','Premium Cotton T-Shirts - Updated Description','4eab6fdd-05b4-4950-a765-4b13a4e79af9','2026-07-10 13:41:11','2026-07-10 13:43:17',1,'2026-07-10 13:43:17'),('T-Shirts-6071 (Updated)','Premium Cotton T-Shirts - Updated Description','616dbe6c-03f4-4f39-95e2-6f75193d2bd7','2026-07-09 13:34:33','2026-07-09 13:36:08',1,'2026-07-09 13:36:08'),('Category 17839721726790 B','Category B','7794be93-be83-4341-99b8-947741f38503','2026-07-13 19:50:06','2026-07-13 19:50:11',1,'2026-07-13 19:50:11'),('T-Shirts-2069 (Updated)','Premium Cotton T-Shirts - Updated Description','80f3355c-7cc3-4bdb-b16b-5f35c63bc22c','2026-07-09 13:27:17','2026-07-09 13:28:44',1,'2026-07-09 13:28:44'),('Category 17837174432023 Updated','Category updated','8c1de5ab-bddf-4f8f-ac21-66fc6d490600','2026-07-10 21:04:36','2026-07-10 21:04:40',0,NULL),('Nike','Nike Shoes','992801b2-eb37-45da-81f5-45ab9049d0fe','2026-07-13 19:41:15','2026-07-13 19:41:15',0,NULL),('T-Shirts-3275 (Updated)','Premium Cotton T-Shirts - Updated Description','9be98334-4d39-4ec8-9b62-2034d935a7a3','2026-07-10 13:38:18','2026-07-10 13:40:26',1,'2026-07-10 13:40:26'),('Category 17839721726790 Updated','Category updated','afa03a87-8412-487d-9509-c9758829ccec','2026-07-13 19:50:04','2026-07-13 19:50:09',0,NULL),('Category 17837174432023 B','Category B','b954470b-25f1-4ff5-b9b6-deca6d1a169b','2026-07-10 21:04:38','2026-07-10 21:04:42',1,'2026-07-10 21:04:42'),('adidas','adidas','c8ea5f8e-854b-482f-a779-668a53644d10','2026-07-10 21:25:09','2026-07-10 21:25:09',0,NULL),('T-Shirts-4341 (Updated)','Premium Cotton T-Shirts - Updated Description','d60809af-cadd-43a4-88ba-2f4c2f4ec2ce','2026-07-10 11:38:09','2026-07-10 11:40:08',1,'2026-07-10 11:40:08'),('T-Shirts-7852 (Updated)','Premium Cotton T-Shirts - Updated Description','fedcc75a-fe53-4fdb-9a27-a826577892b9','2026-07-10 13:21:48','2026-07-10 13:23:53',1,'2026-07-10 13:23:53');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `gender` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `birthday` date DEFAULT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `loyalty_points` int NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_customers_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES ('Jane Smith-2069 (Updated)','+2519112071','jane.smith2069@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'1cc4b790-4edb-4668-a9eb-694979101782','2026-07-09 13:27:56','2026-07-09 13:28:36',1,'2026-07-09 13:28:36'),('Jane Smith (Updated)','+251911987654','jane.smith@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'438af568-8631-4deb-b7ac-eaa8a537373f','2026-07-09 08:56:54','2026-07-09 08:56:58',0,NULL),('Customer 17837174432023 B','+251911860880','customer17837174432023b@example.com','Bahir Dar',NULL,NULL,NULL,0,1,'621272ba-53fb-404c-a517-a80316082aed','2026-07-10 21:05:11','2026-07-10 21:05:16',1,'2026-07-10 21:05:16'),('Jane Smith-3275 (Updated)','+2519113277','jane.smith3275@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'819b18f7-15f5-4987-b09c-dddb45cd0a23','2026-07-10 13:38:59','2026-07-10 13:40:17',1,'2026-07-10 13:40:17'),('Customer 17837174432023 Updated','+251911906022','updated17837174432023@example.com','Addis Ababa',NULL,NULL,NULL,0,1,'838ab827-a033-4586-a8cd-17785cb137c6','2026-07-10 21:05:09','2026-07-10 21:05:13',0,NULL),('Jane Smith-6071 (Updated)','+2519116073','jane.smith6071@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'94938285-070b-4287-9ebf-ae6d8f457005','2026-07-09 13:35:12','2026-07-09 13:36:00',1,'2026-07-09 13:36:00'),('Customer 17839721726790 Updated','+251911299239','updated17839721726790@example.com','Addis Ababa',NULL,NULL,NULL,0,1,'9db622c8-1fd7-4991-96f8-f7685adef371','2026-07-13 19:50:38','2026-07-13 19:50:42',0,NULL),('Jane Smith-6287 (Updated)','+2519116289','jane.smith6287@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'9de8ece6-2a26-4002-a8e4-4102267f765c','2026-07-10 11:06:42','2026-07-10 11:07:30',1,'2026-07-10 11:07:30'),('Customer 17839721726790 B','+251911504601','customer17839721726790b@example.com','Bahir Dar',NULL,NULL,NULL,0,1,'aa5307aa-f116-4ad1-aac0-8ff81e2ee6c2','2026-07-13 19:50:40','2026-07-13 19:50:45',1,'2026-07-13 19:50:45'),('Customer 17837161771760 Updated','+251911783935','updated17837161771760@example.com','Addis Ababa',NULL,NULL,NULL,0,1,'b6628f4a-5092-44ef-ab86-ee1d5e6c4bab','2026-07-10 20:44:03','2026-07-10 20:45:15',1,'2026-07-10 20:45:15'),('Jane Smith-4341 (Updated)','+2519114343','jane.smith4341@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'bfc8636d-a8ec-49c3-81c8-538e195abc3c','2026-07-10 11:38:48','2026-07-10 11:39:59',1,'2026-07-10 11:39:59'),('Jane Smith-7852 (Updated)','+2519117854','jane.smith7852@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'d4528da7-3cee-4f92-bd29-ffe60fb514c5','2026-07-10 13:22:27','2026-07-10 13:23:43',1,'2026-07-10 13:23:43'),('Jane Smith-1583 (Updated)','+2519111585','jane.smith1583@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'e76f03b0-7033-4b8f-aabc-0746acef1d46','2026-07-10 13:41:51','2026-07-10 13:43:09',1,'2026-07-10 13:43:09'),('Customer 17837161771760 B','+251911909264','customer17837161771760b@example.com','Bahir Dar',NULL,NULL,NULL,0,1,'f15c7b82-deff-42df-9403-5cf4d0e6f5ee','2026-07-10 20:44:06','2026-07-10 20:44:10',1,'2026-07-10 20:44:10'),('Jane Smith-4376 (Updated)','+2519114378','jane.smith4376@example.com','Addis Ababa, Ethiopia',NULL,NULL,NULL,0,1,'f6f1c04c-6150-4026-8e7f-0afcacba2e1f','2026-07-10 11:46:50','2026-07-10 11:48:05',1,'2026-07-10 11:48:05');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expense_categories`
--

DROP TABLE IF EXISTS `expense_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expense_categories` (
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_recurring` tinyint(1) NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_expense_categories_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expense_categories`
--

LOCK TABLES `expense_categories` WRITE;
/*!40000 ALTER TABLE `expense_categories` DISABLE KEYS */;
INSERT INTO `expense_categories` VALUES ('ekk','ekk',0,'08e5b61f-ca0b-46a7-93b8-49a9ccd79fce','2026-07-10 21:27:05','2026-07-10 21:27:05',0,NULL),('Fuel','Fuel expenses',0,'0e1f273a-a27a-4e97-baec-dd7133da7f2a','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Utilities 17839721726790 Updated','Utility bills updated',0,'23853f37-4399-4064-b062-a716d7b2f105','2026-07-13 19:50:47','2026-07-13 19:50:51',0,NULL),('Transportation','Transportation costs',0,'2e140234-42cb-4cbe-8f10-50bd763a11ee','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Internet','Internet bills',1,'2fdff310-cf1b-4a3b-913c-aa8a4cfddac8','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Utilities-7852','Utility bills',0,'35cdb270-092e-4969-b79f-d6641ba58295','2026-07-10 13:22:40','2026-07-10 13:23:41',1,'2026-07-10 13:23:41'),('Water','Water bills',1,'48251e76-e92f-483f-b078-2e26b9560f82','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Lunch','Lunch expenses',0,'48827a88-47ea-4bf7-9915-8b39fd1211a9','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('House Rent','Monthly rent payment',1,'4e5bef6f-21aa-4b21-b21d-690ebfcdb414','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Utilities 17837161771760 B','Utility bills B',0,'52f3be7a-8abb-4b7d-8c44-7e3b0cdb1815','2026-07-10 20:44:14','2026-07-10 20:44:18',1,'2026-07-10 20:44:18'),('test cat','test cat d',0,'55d7ea91-e9fa-4190-b66c-394d376bdebd','2026-07-10 08:50:59','2026-07-10 08:50:59',0,NULL),('Salary','Employee salaries',1,'5981f628-29ea-4877-bf03-1e124052b9c6','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Utilities-6071','Utility bills',0,'83721136-f491-4073-86b0-d91d3b15f0fd','2026-07-09 13:35:25','2026-07-09 13:35:58',1,'2026-07-09 13:35:58'),('Electricity','Electricity bills',1,'8e3821a5-e9ae-4a5e-bdbe-e64845826f5a','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Miscellaneous','Other expenses',0,'9cc0eaa7-13ae-4b34-a0d0-b3b9fbcc8215','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Guard Salary','Security guard salary',1,'acb47cb8-ead2-4099-9b91-96189bd11ad8','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Utilities 17839721726790 B','Utility bills B',0,'af5c20e6-2b4a-424b-9366-a2ad3507e53d','2026-07-13 19:50:49','2026-07-13 19:50:53',1,'2026-07-13 19:50:53'),('Utilities 17837174432023 B','Utility bills B',0,'bf64376a-01b5-48e1-a237-0cd26c8b2af9','2026-07-10 21:05:20','2026-07-10 21:05:24',1,'2026-07-10 21:05:24'),('Utilities-6287','Utility bills',0,'bfd6c023-380f-45ee-8179-4d1ad982f3db','2026-07-10 11:06:55','2026-07-10 11:07:28',1,'2026-07-10 11:07:28'),('Breakfast','Breakfast expenses',0,'c923089c-6ef5-4412-ba27-98c0812c8f22','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Marketing','Marketing expenses',0,'ca03b78d-9564-4e92-b41b-6897d1378701','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Utilities-4341','Utility bills',0,'cc74507b-2a6f-4f23-a7c5-4da16e40ce0a','2026-07-10 11:39:01','2026-07-10 11:39:57',1,'2026-07-10 11:39:57'),('Ekub','Ekub Monthly',0,'d0b074a5-eee2-43c4-bdcf-e5c39e08a3c9','2026-07-10 08:51:12','2026-07-10 08:51:12',0,NULL),('Utilities-4376','Utility bills',0,'d59b2fbf-2cab-411c-8070-02ba3075802c','2026-07-10 11:47:03','2026-07-10 11:48:03',1,'2026-07-10 11:48:03'),('Utilities 17837161771760 A','Utility bills A',0,'dac27e70-22d9-45de-8663-1c0d9913cb68','2026-07-10 20:44:12','2026-07-10 20:45:17',1,'2026-07-10 20:45:17'),('Utilities-3275','Utility bills',0,'dd413ecc-757e-42f6-9a60-29c7a17c4a97','2026-07-10 13:39:14','2026-07-10 13:40:15',1,'2026-07-10 13:40:15'),('Utilities 17837174432023 Updated','Utility bills updated',0,'e4c8fd2c-5962-4937-8c43-2a94a2f5de33','2026-07-10 21:05:18','2026-07-10 21:05:22',0,NULL),('Utilities-1583','Utility bills',0,'eedf74d6-2fa1-4576-b8eb-172d0a764606','2026-07-10 13:42:05','2026-07-10 13:43:07',1,'2026-07-10 13:43:07');
/*!40000 ALTER TABLE `expense_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expenses`
--

DROP TABLE IF EXISTS `expenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `expenses` (
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `category_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `amount` decimal(10,2) NOT NULL,
  `expense_date` datetime NOT NULL,
  `is_recurring` tinyint(1) NOT NULL,
  `recurring_month` int DEFAULT NULL,
  `receipt_image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `notes` text COLLATE utf8mb4_unicode_ci,
  `created_by` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `created_by` (`created_by`),
  CONSTRAINT `expenses_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `expense_categories` (`id`),
  CONSTRAINT `expenses_ibfk_2` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses`
--

LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES ('Electricity 17839721726790 B','Electricity bill B','23853f37-4399-4064-b062-a716d7b2f105',200.00,'2026-07-10 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','13f3efe3-d949-4c73-890c-a9187339bb27','2026-07-13 19:50:57','2026-07-13 19:51:01',1,'2026-07-13 19:51:01'),('Electricity 17837161771760 B','Electricity bill B','dac27e70-22d9-45de-8663-1c0d9913cb68',200.00,'2026-07-10 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','2344838b-b27a-4c2d-9565-04da77aa370b','2026-07-10 20:44:22','2026-07-10 20:44:27',1,'2026-07-10 20:44:27'),('Electricity bill-4376 (Updated)','Electricity bill (Updated)','d59b2fbf-2cab-411c-8070-02ba3075802c',175.00,'2026-07-09 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','6221fd75-ce64-4e32-b04b-7814ae2bca66','2026-07-10 11:47:05','2026-07-10 11:48:01',1,'2026-07-10 11:48:01'),('Electricity 17837174432023 B','Electricity bill B','e4c8fd2c-5962-4937-8c43-2a94a2f5de33',200.00,'2026-07-10 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','71284138-1047-4636-a87e-38197ec85d20','2026-07-10 21:05:28','2026-07-10 21:05:32',1,'2026-07-10 21:05:32'),('Electricity bill-1583 (Updated)','Electricity bill (Updated)','eedf74d6-2fa1-4576-b8eb-172d0a764606',175.00,'2026-07-09 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','93509e43-1e03-4c34-85a8-8befbb4eb8c0','2026-07-10 13:42:07','2026-07-10 13:43:05',1,'2026-07-10 13:43:05'),('Electricity bill-7852 (Updated)','Electricity bill (Updated)','35cdb270-092e-4969-b79f-d6641ba58295',175.00,'2026-07-09 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','a6f6174f-079f-4b65-a9e6-88448bb2df26','2026-07-10 13:22:42','2026-07-10 13:23:39',1,'2026-07-10 13:23:39'),('Electricity bill-3275 (Updated)','Electricity bill (Updated)','dd413ecc-757e-42f6-9a60-29c7a17c4a97',175.00,'2026-07-09 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','ae37ea6b-50cf-4d7c-96f9-788fcfb7d66c','2026-07-10 13:39:16','2026-07-10 13:40:13',1,'2026-07-10 13:40:13'),('Electricity 17837174432023 Updated','Electricity bill updated','e4c8fd2c-5962-4937-8c43-2a94a2f5de33',175.00,'2026-07-10 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','b5745f48-da3b-40ec-9084-d732b0aff671','2026-07-10 21:05:26','2026-07-10 21:05:30',0,NULL),('Electricity 17837161771760 Updated','Electricity bill updated','dac27e70-22d9-45de-8663-1c0d9913cb68',175.00,'2026-07-10 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','d8abd82c-c7f7-4d5c-8517-25d12a768c20','2026-07-10 20:44:20','2026-07-10 20:45:19',1,'2026-07-10 20:45:19'),('Electricity 17839721726790 Updated','Electricity bill updated','23853f37-4399-4064-b062-a716d7b2f105',175.00,'2026-07-10 00:00:00',0,NULL,NULL,NULL,'f35da230-26a8-4696-b03a-c00e184d7826','e4e24cc2-40c0-4091-8508-33c1132d6031','2026-07-13 19:50:55','2026-07-13 19:50:59',0,NULL);
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `product_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantity` int NOT NULL,
  `reserved_quantity` int NOT NULL,
  `available_quantity` int NOT NULL,
  `average_cost` decimal(10,2) DEFAULT NULL,
  `total_value` decimal(10,2) DEFAULT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `product_id` (`product_id`),
  CONSTRAINT `inventory_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES ('e765067e-0a3d-4e66-9ae5-012a25200341',0,0,0,0.00,0.00,'00591061-1d7a-495d-a2d7-30d0efca4cb3','2026-07-10 20:43:49','2026-07-10 20:43:49',0,NULL),('0f4c7cbd-17f0-4e7e-80ee-86a7ec542753',20,0,20,11.09,221.80,'1c89b5bb-c7ad-4ad6-80bf-60a343cd144f','2026-07-10 20:43:47','2026-07-10 20:44:39',0,NULL),('12be64ff-18f3-42cf-a1e1-8a5dd2454b6a',1,0,1,1.14,1.14,'29ccd2d6-3db6-4b85-8da6-b9a9299cf014','2026-07-09 08:27:25','2026-07-14 11:58:42',0,NULL),('86aa3fd7-da71-4653-8b3a-86f50950ac30',120,0,120,2.29,275.16,'2c61448c-e094-42ee-97f3-e223470d2b78','2026-07-10 13:38:23','2026-07-10 16:45:29',0,NULL),('5c900a29-a111-434a-93d8-1f4b0fb9fd6e',0,0,0,0.00,0.00,'502eca1c-dd69-4d83-849d-14dad824fefc','2026-07-10 21:24:00','2026-07-10 21:24:00',0,NULL),('d40bfad1-2be4-4724-87cc-e2ec662d2573',120,0,120,2.08,250.00,'51d31d4b-d103-459b-8809-5a29c01cacaa','2026-07-10 11:46:15','2026-07-10 11:46:56',0,NULL),('b2315975-218b-42d5-8b4a-4675d7321a3c',20,0,20,11.09,221.80,'62331fd4-e1ee-4a2d-9b4f-1ee17aa8d966','2026-07-10 21:04:53','2026-07-10 21:05:45',0,NULL),('500c751e-b29c-4067-b52e-7426e708b1f9',17,0,17,2495.00,42415.00,'7db8f373-d233-42ce-aa05-bfcf8af34a06','2026-07-13 19:42:11','2026-07-13 20:48:36',0,NULL),('230e297a-772d-4d71-82c2-dac539b2a84a',120,0,120,2.08,250.00,'7e1b5608-8d93-4cb4-9fd5-8225772f336a','2026-07-09 13:34:37','2026-07-09 13:35:18',0,NULL),('36104e9a-06ef-4fc4-8a2f-358ea09115f8',120,0,120,2.08,250.00,'894041c2-be7c-4e1d-a854-a10d4768a5a4','2026-07-09 13:27:21','2026-07-09 13:28:03',0,NULL),('0019750d-56f9-41c9-9c74-a62180b7ec8e',120,0,120,2.08,250.00,'9c82aa5d-61ef-4a0a-9822-9b282e822a2d','2026-07-10 11:38:13','2026-07-10 11:38:55',0,NULL),('1627e0ae-34fc-4029-b997-59bb231dc61d',20,0,20,12.50,250.00,'a811c39e-ed1f-42ee-bd2c-55cba3e466b9','2026-07-09 11:18:33','2026-07-09 11:19:12',0,NULL),('e625b251-161d-432a-a956-831efdb5ab46',0,0,0,0.00,0.00,'ac36dc4b-4ca8-4182-a248-6bf88d6f10c4','2026-07-13 19:50:23','2026-07-13 19:50:23',0,NULL),('47941fba-e8f7-4638-85a2-c777260a1d1b',120,0,120,2.08,250.00,'ac5f3c5c-02d3-4ebb-9348-9f04dcbfb90b','2026-07-10 11:06:07','2026-07-10 11:06:48',0,NULL),('494e0824-e1d6-4cec-b733-cbbf23cc2855',120,0,120,2.08,250.00,'bbf0d557-4541-407e-8ae0-0257f041fb0c','2026-07-10 13:21:52','2026-07-10 13:22:34',0,NULL),('022f4aee-3b9e-43e8-9937-9c0f566bebcc',20,0,20,11.09,221.80,'c3b32557-d66f-497d-968f-2f1cf2ed79db','2026-07-13 19:50:21','2026-07-13 19:51:14',0,NULL),('df7224f0-83ad-42e7-8315-6aad33d1051c',0,0,0,0.00,0.00,'c514b92f-f570-49aa-aeb3-fe6703e10ab6','2026-07-09 08:46:45','2026-07-09 08:46:45',0,NULL),('6e58cc8f-c026-47c8-9c9b-04e179b699ef',118,0,118,2.12,250.00,'d3d01fa9-6554-459d-abe8-4be74e7078cb','2026-07-10 13:41:15','2026-07-10 13:41:57',0,NULL),('9adeacef-2392-43b2-af15-257334b30a3b',0,0,0,0.00,0.00,'dbaf81d6-1539-40ab-a6f8-7f9d3a40411b','2026-07-10 21:04:55','2026-07-10 21:04:55',0,NULL),('8631909c-d123-405c-b897-7d960284d401',20,0,20,12.50,250.00,'dc39ca6b-7805-42e8-86ff-f5a4823f2e36','2026-07-09 08:56:18','2026-07-09 08:57:00',0,NULL),('a3de90e2-acca-4832-a6c8-4fb999a0bcc1',0,0,0,0.00,0.00,'e5a108b6-7f03-49c9-ae91-12a2be3e3b0a','2026-07-10 21:24:45','2026-07-10 21:24:45',0,NULL);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `notifications`
--

DROP TABLE IF EXISTS `notifications`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `notifications` (
  `user_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `message` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `notification_type` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `reference_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reference_id` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_read` tinyint(1) NOT NULL,
  `read_at` datetime DEFAULT NULL,
  `push_sent` tinyint(1) NOT NULL,
  `push_sent_at` datetime DEFAULT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `notifications_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `notifications`
--

LOCK TABLES `notifications` WRITE;
/*!40000 ALTER TABLE `notifications` DISABLE KEYS */;
/*!40000 ALTER TABLE `notifications` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permissions`
--

DROP TABLE IF EXISTS `permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `permissions` (
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `module` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permissions`
--

LOCK TABLES `permissions` WRITE;
/*!40000 ALTER TABLE `permissions` DISABLE KEYS */;
INSERT INTO `permissions` VALUES ('manage_inventory_test_17839721726790_b','Temporary permission B','inventory','031144dc-978a-4380-a23a-1d9870e4c7ba','2026-07-13 19:49:41','2026-07-13 19:49:45',1,'2026-07-13 19:49:45'),('manage_inventory_test_3275','Temporary test permission for inventory management','inventory','07ae6653-cc77-4fd7-88b5-b7cd83059fcd','2026-07-10 13:39:22','2026-07-10 13:40:11',1,'2026-07-10 13:40:11'),('manage_inventory_test_4376','Temporary test permission for inventory management','inventory','45e3b272-c757-43ae-a54a-465a4eb520c4','2026-07-10 11:47:11','2026-07-10 11:47:59',1,'2026-07-10 11:47:59'),('manage_customers','Manage customers','customers','497eb0b7-c33a-4a4a-9f95-5b885c8f6e46','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_users','Manage users','users','507747cf-3aa0-4b11-bcda-f8a147475b15','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_inventory_test_17837174432023_b','Temporary permission B','inventory','52feb68a-5cb4-494d-8409-1dd9d4f71b79','2026-07-10 21:04:12','2026-07-10 21:04:16',1,'2026-07-10 21:04:16'),('manage_inventory_test_17839721726790_updated','Temporary permission updated','inventory','7213d4ee-e653-431c-bce4-40551eb3f94a','2026-07-13 19:49:39','2026-07-13 19:49:43',0,NULL),('manage_inventory_test_7852','Temporary test permission for inventory management','inventory','80efb2d0-cd5e-4ea0-b82c-f78e9933ebcc','2026-07-10 13:22:48','2026-07-10 13:23:37',1,'2026-07-10 13:23:37'),('manage_inventory_test_4341','Temporary test permission for inventory management','inventory','946d6879-7719-484e-807f-6e46d0ab33f7','2026-07-10 11:39:07','2026-07-10 11:39:55',1,'2026-07-10 11:39:55'),('manage_inventory_test_17837161771760_b','Temporary permission B','inventory','97613e41-2a0a-41d9-8cb1-7393e5a1927e','2026-07-10 20:43:06','2026-07-10 20:43:11',1,'2026-07-10 20:43:11'),('manage_sales','Process sales and refunds','sales','9aa369ff-25bc-4c8a-abf4-ef61ba792ac8','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_inventory_test_1583','Temporary test permission for inventory management','inventory','9c223844-ac36-47da-b3a0-8aabb5aaec2d','2026-07-10 13:42:14','2026-07-10 13:43:03',1,'2026-07-10 13:43:03'),('manage_suppliers','Manage suppliers','suppliers','9c7809bd-e195-466f-9b80-76fc0c6d6497','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_inventory','Adjust inventory','inventory','9da3026c-f8dd-4692-a795-83c2f0d5ad27','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_purchases','Create purchases','purchases','a10fbb42-722a-468a-8f48-78681d9d40c9','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_products','Create, update, delete products','products','a5d0fa20-0aaa-491f-a549-e3d0b34b53f5','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_inventory_test_17837174432023_updated','Temporary permission updated','inventory','b334960e-5b27-455d-9caf-13c7d54accef','2026-07-10 21:04:10','2026-07-10 21:04:14',0,NULL),('view_reports','View reports','reports','bcc10d37-2b9f-467f-898b-629bc6ee21cb','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_settings','Update settings','settings','d55da4be-8579-4281-8e1d-18a18b116191','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_expenses','Create expenses','expenses','d712ee0b-4ebf-4f18-953e-6719d9db6a99','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('manage_inventory_test_17837161771760_updated','Temporary permission updated','inventory','ddfc9969-8309-4024-b7d5-6849d455270a','2026-07-10 20:43:04','2026-07-10 20:45:00',1,'2026-07-10 20:45:00');
/*!40000 ALTER TABLE `permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `product_code` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `barcode` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `qr_code` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` text COLLATE utf8mb4_unicode_ci,
  `category_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `brand_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `gender` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL,
  `color` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `size` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `buying_price` decimal(10,2) NOT NULL,
  `selling_price` decimal(10,2) NOT NULL,
  `quantity` int NOT NULL,
  `minimum_stock` int NOT NULL,
  `supplier_id` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_by` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_products_product_code` (`product_code`),
  UNIQUE KEY `qr_code` (`qr_code`),
  UNIQUE KEY `ix_products_barcode` (`barcode`),
  KEY `category_id` (`category_id`),
  KEY `brand_id` (`brand_id`),
  KEY `supplier_id` (`supplier_id`),
  KEY `created_by` (`created_by`),
  KEY `ix_products_name` (`name`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `products_ibfk_2` FOREIGN KEY (`brand_id`) REFERENCES `brands` (`id`),
  CONSTRAINT `products_ibfk_3` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`),
  CONSTRAINT `products_ibfk_4` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES ('PRD-L8PUPQIG','PRD-L8PUPQIG',NULL,'Nike Dry-Fit Tee-4341 (Updated)','Athletic dry-fit sports t-shirt - Updated','d60809af-cadd-43a4-88ba-2f4c2f4ec2ce','dc63fe4b-1301-4456-b0d4-f28d8cb6dca0','unisex','Black','L',12.50,40.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','0019750d-56f9-41c9-9c74-a62180b7ec8e','2026-07-10 11:38:13','2026-07-10 11:40:03',1,'2026-07-10 11:40:03'),('PRD-B2606M1I','PRD-B2606M1I',NULL,'Product 17839721726790 Updated','Test product updated','afa03a87-8412-487d-9509-c9758829ccec','d4623434-a928-4c2d-8c75-70ee8989ab47','unisex','Black','L',10.00,30.00,20,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','022f4aee-3b9e-43e8-9937-9c0f566bebcc','2026-07-13 19:50:21','2026-07-13 19:51:14',0,NULL),('PRD-1TCNYLCS','PRD-1TCNYLCS',NULL,'Product 17837161771760 Updated','Test product updated','2dab9132-69c2-458d-a33a-84b83335fa00','23b4ffff-3cd3-4b44-8c00-5dd4d2152abb','unisex','Black','L',10.00,30.00,20,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753','2026-07-10 20:43:47','2026-07-10 20:45:11',1,'2026-07-10 20:45:11'),('PRD-3Q644S9I','PRD-3Q644S9I',NULL,'Nike Dry-Fit Tee','Athletic dry-fit sports t-shirt','365708fd-1af5-4e5f-9741-5c36e7e75c10','80d84645-676e-4cb8-912d-dba55c1a01ba','unisex','Black','L',12.50,35.00,1,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a','2026-07-09 08:27:24','2026-07-14 11:58:42',0,NULL),('PRD-YXIQXJR0','PRD-YXIQXJR0',NULL,'Nike Dry-Fit Tee (Updated)','Athletic dry-fit sports t-shirt - Updated','4d0c310c-9de4-4528-8158-86eed7aa9840','207c7e1a-3d9e-44e8-a00d-6950faded093','unisex','Black','L',12.50,40.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','1627e0ae-34fc-4029-b997-59bb231dc61d','2026-07-09 11:18:33','2026-07-09 11:19:00',0,NULL),('PRD-J2GZP8E9','PRD-J2GZP8E9',NULL,'Nike Dry-Fit Tee-6071 (Updated)','Athletic dry-fit sports t-shirt - Updated','616dbe6c-03f4-4f39-95e2-6f75193d2bd7','70b683f5-6e43-4bbb-aa3c-9d89158225ec','unisex','Black','L',12.50,40.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','230e297a-772d-4d71-82c2-dac539b2a84a','2026-07-09 13:34:37','2026-07-09 13:36:04',1,'2026-07-09 13:36:04'),('PRD-LMI9B21B','PRD-LMI9B21B',NULL,'Nike Dry-Fit Tee-2069 (Updated)','Athletic dry-fit sports t-shirt - Updated','80f3355c-7cc3-4bdb-b16b-5f35c63bc22c','964c3ac9-4e74-40a7-838d-f7f6d04196e4','unisex','Black','L',12.50,40.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','36104e9a-06ef-4fc4-8a2f-358ea09115f8','2026-07-09 13:27:21','2026-07-09 13:28:40',1,'2026-07-09 13:28:40'),('PRD-930F0ZQ3','PRD-930F0ZQ3',NULL,'Nike Dry-Fit Tee-6287 (Updated)','Athletic dry-fit sports t-shirt - Updated','4590dd4c-764d-46ef-81b7-abcc9b0206a3','c2aff1df-c638-4d7f-aa30-73ba76318c0a','unisex','Black','L',12.50,40.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','47941fba-e8f7-4638-85a2-c777260a1d1b','2026-07-10 11:06:06','2026-07-10 11:07:35',1,'2026-07-10 11:07:35'),('PRD-84ZH5U97','PRD-84ZH5U97',NULL,'Nike Dry-Fit Tee-7852 (Updated)','Athletic dry-fit sports t-shirt - Updated','fedcc75a-fe53-4fdb-9a27-a826577892b9','16f405b2-d310-4a08-bdf6-192134a53cb5','unisex','Black','L',12.50,40.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','494e0824-e1d6-4cec-b733-cbbf23cc2855','2026-07-10 13:21:52','2026-07-10 13:23:47',1,'2026-07-10 13:23:47'),('PRD-VP4OC67J','PRD-VP4OC67J',NULL,'Air Force','Air Force','992801b2-eb37-45da-81f5-45ab9049d0fe','207c7e1a-3d9e-44e8-a00d-6950faded093','unisex','white','42',4000.00,5000.00,17,3,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','500c751e-b29c-4067-b52e-7426e708b1f9','2026-07-13 19:42:11','2026-07-13 20:48:36',0,NULL),('PRD-WM7XK3L5','PRD-WM7XK3L5',NULL,'test','test','365708fd-1af5-4e5f-9741-5c36e7e75c10','207c7e1a-3d9e-44e8-a00d-6950faded093','unisex','red','large',30.00,50.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','5c900a29-a111-434a-93d8-1f4b0fb9fd6e','2026-07-10 21:24:00','2026-07-10 21:24:00',0,NULL),('PRD-WGBKHKUE','PRD-WGBKHKUE',NULL,'Nike Dry-Fit Tee-1583 (Updated)','Athletic dry-fit sports t-shirt - Updated','4eab6fdd-05b4-4950-a765-4b13a4e79af9','4f156fc6-d3be-4b29-8b8f-7c2405fca7d2','unisex','Black','L',12.50,40.00,118,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','6e58cc8f-c026-47c8-9c9b-04e179b699ef','2026-07-10 13:41:15','2026-07-10 13:43:13',1,'2026-07-10 13:43:13'),('PRD-RBG6WKC4','PRD-RBG6WKC4',NULL,'Nike Dry-Fit Tee (Updated)','Athletic dry-fit sports t-shirt - Updated','365708fd-1af5-4e5f-9741-5c36e7e75c10','80d84645-676e-4cb8-912d-dba55c1a01ba','unisex','Black','L',12.50,40.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','8631909c-d123-405c-b897-7d960284d401','2026-07-09 08:56:18','2026-07-09 08:56:45',0,NULL),('PRD-D2R7TMQT','PRD-D2R7TMQT',NULL,'Nike Dry-Fit Tee-3275 (Updated)','Athletic dry-fit sports t-shirt - Updated','9be98334-4d39-4ec8-9b62-2034d935a7a3','60f674aa-db58-4753-891f-aae9dee32137','unisex','Black','L',12.50,40.00,120,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','86aa3fd7-da71-4653-8b3a-86f50950ac30','2026-07-10 13:38:23','2026-07-10 16:45:29',1,'2026-07-10 13:40:21'),('PRD-BVEWQABO','PRD-BVEWQABO',NULL,'Product 17837174432023 B','Test product B','8c1de5ab-bddf-4f8f-ac21-66fc6d490600','54e814bb-4a90-4a21-8461-4c4080fb456d','unisex','Blue','M',12.00,24.00,0,4,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','9adeacef-2392-43b2-af15-257334b30a3b','2026-07-10 21:04:55','2026-07-10 21:04:59',1,'2026-07-10 21:04:59'),('PRD-CUIEWEX9','PRD-CUIEWEX9',NULL,'test2','test2','4d0c310c-9de4-4528-8158-86eed7aa9840','207c7e1a-3d9e-44e8-a00d-6950faded093','unisex','green','small',110.00,199.85,0,50,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','a3de90e2-acca-4832-a6c8-4fb999a0bcc1','2026-07-10 21:24:45','2026-07-10 21:24:45',0,NULL),('PRD-7AXOBCTK','PRD-7AXOBCTK',NULL,'Product 17837174432023 Updated','Test product updated','8c1de5ab-bddf-4f8f-ac21-66fc6d490600','54e814bb-4a90-4a21-8461-4c4080fb456d','unisex','Black','L',10.00,30.00,20,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','b2315975-218b-42d5-8b4a-4675d7321a3c','2026-07-10 21:04:52','2026-07-10 21:05:45',0,NULL),('PRD-LJ3DY62W','PRD-LJ3DY62W',NULL,'Nike Dry-Fit Tee-4376 (Updated)','Athletic dry-fit sports t-shirt - Updated','36450278-b665-4bf0-b665-441e0308fe35','abeeaacb-30a8-42a8-a66d-4a9f961bc2d2','unisex','Black','L',12.50,40.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','d40bfad1-2be4-4724-87cc-e2ec662d2573','2026-07-10 11:46:15','2026-07-10 11:48:09',1,'2026-07-10 11:48:09'),('PRD-5FSLMJ8O','PRD-5FSLMJ8O',NULL,'Nike Dry-Fit Tee','Athletic dry-fit sports t-shirt','365708fd-1af5-4e5f-9741-5c36e7e75c10','80d84645-676e-4cb8-912d-dba55c1a01ba','unisex','Black','L',12.50,35.00,0,5,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','df7224f0-83ad-42e7-8315-6aad33d1051c','2026-07-09 08:46:45','2026-07-09 08:46:45',0,NULL),('PRD-81BH0WEU','PRD-81BH0WEU',NULL,'Product 17839721726790 B','Test product B','afa03a87-8412-487d-9509-c9758829ccec','d4623434-a928-4c2d-8c75-70ee8989ab47','unisex','Blue','M',12.00,24.00,0,4,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','e625b251-161d-432a-a956-831efdb5ab46','2026-07-13 19:50:23','2026-07-13 19:50:28',1,'2026-07-13 19:50:28'),('PRD-TA53WCR5','PRD-TA53WCR5',NULL,'Product 17837161771760 B','Test product B','2dab9132-69c2-458d-a33a-84b83335fa00','23b4ffff-3cd3-4b44-8c00-5dd4d2152abb','unisex','Blue','M',12.00,24.00,0,4,NULL,NULL,'active','f35da230-26a8-4696-b03a-c00e184d7826','e765067e-0a3d-4e66-9ae5-012a25200341','2026-07-10 20:43:49','2026-07-10 20:43:53',1,'2026-07-10 20:43:53');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchase_items`
--

DROP TABLE IF EXISTS `purchase_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchase_items` (
  `purchase_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantity` int NOT NULL,
  `buying_price` decimal(10,2) NOT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `purchase_id` (`purchase_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `purchase_items_ibfk_1` FOREIGN KEY (`purchase_id`) REFERENCES `purchases` (`id`),
  CONSTRAINT `purchase_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchase_items`
--

LOCK TABLES `purchase_items` WRITE;
/*!40000 ALTER TABLE `purchase_items` DISABLE KEYS */;
INSERT INTO `purchase_items` VALUES ('919eded7-efeb-466d-a538-b55327c9de50','1627e0ae-34fc-4029-b997-59bb231dc61d',20,12.50,0.00,250.00,'0265e7fc-7b1a-4383-b0ed-f55e28b8c4e2','2026-07-09 11:19:12','2026-07-09 11:19:12',0,NULL),('e292aa28-611d-4705-a533-7d8e3b8f81bc','022f4aee-3b9e-43e8-9937-9c0f566bebcc',12,12.00,0.00,144.00,'0d92dee5-279f-467a-8c83-7c4d8f5fa7b7','2026-07-13 19:51:06','2026-07-13 19:51:06',0,NULL),('a0690caa-7e9a-476a-b3e4-c2cdeffb9c1f','022f4aee-3b9e-43e8-9937-9c0f566bebcc',10,10.00,0.00,100.00,'1106eb00-fa92-43f9-a0dc-3dec4d419b92','2026-07-13 19:51:03','2026-07-13 19:51:03',0,NULL),('cd4aae1e-cfc7-4d1a-9c43-14e05f119931','47941fba-e8f7-4638-85a2-c777260a1d1b',20,12.50,0.00,250.00,'3cc65e8c-cbce-42b8-ab74-8a24c78a6584','2026-07-10 11:06:48','2026-07-10 11:06:48',0,NULL),('e056fa5e-9181-438a-b54b-883233713776','500c751e-b29c-4067-b52e-7426e708b1f9',7,345.00,0.00,2415.00,'47023c92-789a-4fe5-9559-5628d68faf0a','2026-07-13 20:48:36','2026-07-13 20:48:36',0,NULL),('a6819b2c-79af-4703-ae97-75ee76e09e6b','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753',10,10.00,0.00,100.00,'5f9e6719-59d6-492d-9845-1c27b92e8b17','2026-07-10 20:44:29','2026-07-10 20:44:29',0,NULL),('51566935-8a36-4b15-a6aa-30bbb4da2f90','494e0824-e1d6-4cec-b733-cbbf23cc2855',20,12.50,0.00,250.00,'65c99a55-bc34-4bed-8a4f-bfcc25b5922b','2026-07-10 13:22:34','2026-07-10 13:22:34',0,NULL),('0c541f77-9a75-4c11-80c5-e602ab03dea2','86aa3fd7-da71-4653-8b3a-86f50950ac30',20,12.50,0.00,250.00,'7edb7c15-389f-4a25-adc8-47304824c504','2026-07-10 13:39:05','2026-07-10 13:39:05',0,NULL),('7330ba8d-bc2c-4e24-a946-36e9d166c058','36104e9a-06ef-4fc4-8a2f-358ea09115f8',20,12.50,0.00,250.00,'ab70f413-146e-4771-8d17-b578c8dcd4d7','2026-07-09 13:28:03','2026-07-09 13:28:03',0,NULL),('fd746cc1-0ba0-4840-8c4d-ff3f1c66cf2b','8631909c-d123-405c-b897-7d960284d401',20,12.50,0.00,250.00,'b77915da-fcb3-430d-84de-9ddb62a6ae75','2026-07-09 08:57:00','2026-07-09 08:57:00',0,NULL),('5db8ed96-b4d9-4359-9465-716f29a50fa3','b2315975-218b-42d5-8b4a-4675d7321a3c',12,12.00,0.00,144.00,'bbf21071-e6bb-484f-9242-47bf8f3dcb42','2026-07-10 21:05:37','2026-07-10 21:05:37',0,NULL),('8d454557-3895-4b8d-8296-9b1dba84c651','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753',12,12.00,0.00,144.00,'c49c35fe-6a47-4794-b833-82c9dc4ece01','2026-07-10 20:44:31','2026-07-10 20:44:31',0,NULL),('f4f8a9c0-f00a-44a7-9cab-0813676fb193','d40bfad1-2be4-4724-87cc-e2ec662d2573',20,12.50,0.00,250.00,'d0a7035a-683e-409f-92da-7bb77ac65f8f','2026-07-10 11:46:56','2026-07-10 11:46:56',0,NULL),('0d4d9e69-97af-4770-9640-55a5d21aa949','6e58cc8f-c026-47c8-9c9b-04e179b699ef',20,12.50,0.00,250.00,'d8a06db2-e144-4891-b03a-7ca0d8dfcf7a','2026-07-10 13:41:57','2026-07-10 13:41:57',0,NULL),('3f4d06a9-f38a-4968-9a27-00c1caf3d7e1','500c751e-b29c-4067-b52e-7426e708b1f9',11,4000.00,0.00,44000.00,'d8c086c6-7384-4535-b1b8-54ee16191842','2026-07-13 19:46:18','2026-07-13 19:46:18',0,NULL),('de44ec1a-07e1-4683-bff0-fa4fdf1b40f2','b2315975-218b-42d5-8b4a-4675d7321a3c',10,10.00,0.00,100.00,'e102267d-6dd7-41d3-89a8-9334db7ee18f','2026-07-10 21:05:34','2026-07-10 21:05:34',0,NULL),('43b78693-839e-4127-9982-14a74db53a45','230e297a-772d-4d71-82c2-dac539b2a84a',20,12.50,0.00,250.00,'e1be9d43-6971-4c0a-bb7a-27afbab6947c','2026-07-09 13:35:18','2026-07-09 13:35:18',0,NULL),('6a4dcb9f-5a57-4874-a2f9-1ce619f6c51e','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a',1,12.50,0.00,12.50,'e9e8bf73-8ecd-4796-9ed9-725f7c648676','2026-07-13 16:54:00','2026-07-13 16:54:00',0,NULL),('36f48ea5-d091-4fc8-aad7-c144164c6eff','0019750d-56f9-41c9-9c74-a62180b7ec8e',20,12.50,0.00,250.00,'ef0888fb-ce68-4dc2-b6b7-dbbb844725c2','2026-07-10 11:38:55','2026-07-10 11:38:55',0,NULL);
/*!40000 ALTER TABLE `purchase_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `purchases`
--

DROP TABLE IF EXISTS `purchases`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `purchases` (
  `purchase_number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `supplier_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  `tax` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `payment_method` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `paid_amount` decimal(10,2) DEFAULT NULL,
  `balance` decimal(10,2) DEFAULT NULL,
  `purchase_date` datetime NOT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `notes` text COLLATE utf8mb4_unicode_ci,
  `receipt_image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_by` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_purchases_purchase_number` (`purchase_number`),
  KEY `supplier_id` (`supplier_id`),
  KEY `created_by` (`created_by`),
  CONSTRAINT `purchases_ibfk_1` FOREIGN KEY (`supplier_id`) REFERENCES `suppliers` (`id`),
  CONSTRAINT `purchases_ibfk_2` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `purchases`
--

LOCK TABLES `purchases` WRITE;
/*!40000 ALTER TABLE `purchases` DISABLE KEYS */;
INSERT INTO `purchases` VALUES ('PUR-20260710-9469','cd74230e-cecc-4c16-a504-ffbf677cdfed',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-10 13:39:05','completed','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','0c541f77-9a75-4c11-80c5-e602ab03dea2','2026-07-10 13:39:05','2026-07-13 19:43:02',0,NULL),('PUR-20260710-3145','46c51315-758f-4fd3-b896-50e71a5b7fcf',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-10 13:41:57','completed','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','0d4d9e69-97af-4770-9640-55a5d21aa949','2026-07-10 13:41:57','2026-07-13 20:35:26',0,NULL),('PUR-20260710-9654','c5566765-2e46-4883-8079-fec88d10c48f',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-10 11:38:55','completed','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','36f48ea5-d091-4fc8-aad7-c144164c6eff','2026-07-10 11:38:55','2026-07-13 20:35:23',0,NULL),('PUR-20260713-1861','69a99807-ddf2-41b1-8199-920e894d63d7',44000.00,0.00,7920.00,51920.00,'cash',4000.00,47920.00,'2026-07-13 19:46:18','completed','check',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','3f4d06a9-f38a-4968-9a27-00c1caf3d7e1','2026-07-13 19:46:18','2026-07-13 20:35:29',0,NULL),('PUR-20260709-3267','7e0301a4-868a-4cda-a8bd-790701af0786',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-09 13:35:18','completed','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','43b78693-839e-4127-9982-14a74db53a45','2026-07-09 13:35:18','2026-07-13 20:50:01',0,NULL),('PUR-20260710-7777','32581434-8042-4dff-9d0a-9524a27b3803',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-10 13:22:34','completed','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','51566935-8a36-4b15-a6aa-30bbb4da2f90','2026-07-10 13:22:34','2026-07-13 20:50:03',0,NULL),('PUR-20260711-6508','5365382d-2db4-4c22-9d1c-e21a20474bf9',144.00,0.00,25.92,169.92,'cash',300.00,-130.08,'2026-07-10 21:05:37','pending','Test purchase B',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','5db8ed96-b4d9-4359-9465-716f29a50fa3','2026-07-10 21:05:37','2026-07-10 21:05:41',1,'2026-07-10 21:05:41'),('PUR-20260713-6099','5365382d-2db4-4c22-9d1c-e21a20474bf9',12.50,0.00,2.25,14.75,'cash',660.00,-645.25,'2026-07-13 16:54:00','pending','uu',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','6a4dcb9f-5a57-4874-a2f9-1ce619f6c51e','2026-07-13 16:54:00','2026-07-13 16:54:00',0,NULL),('PUR-20260709-7818','234e8cd0-b4b4-448a-9e42-7e6756f745e1',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-09 13:28:03','completed','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','7330ba8d-bc2c-4e24-a946-36e9d166c058','2026-07-09 13:28:03','2026-07-10 11:03:50',0,NULL),('PUR-20260710-5034','c7700d2d-e39f-4b25-8e4c-5fde4e67e1b9',144.00,0.00,25.92,169.92,'cash',300.00,-130.08,'2026-07-10 20:44:31','pending','Test purchase B',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','8d454557-3895-4b8d-8296-9b1dba84c651','2026-07-10 20:44:31','2026-07-10 20:44:31',0,NULL),('PUR-20260709-2998','69a99807-ddf2-41b1-8199-920e894d63d7',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-09 11:19:12','pending','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','919eded7-efeb-466d-a538-b55327c9de50','2026-07-09 11:19:12','2026-07-09 11:19:12',0,NULL),('PUR-20260713-6356','65fdce5b-44f6-47f9-b5e1-bc5bafca91a1',100.00,0.00,18.00,118.00,'cash',280.00,-162.00,'2026-07-13 19:51:03','pending','Updated purchase notes',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','a0690caa-7e9a-476a-b3e4-c2cdeffb9c1f','2026-07-13 19:51:03','2026-07-13 19:51:08',0,NULL),('PUR-20260710-6828','c7700d2d-e39f-4b25-8e4c-5fde4e67e1b9',100.00,0.00,18.00,118.00,'cash',250.00,-132.00,'2026-07-10 20:44:29','pending','Test purchase A',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','a6819b2c-79af-4703-ae97-75ee76e09e6b','2026-07-10 20:44:29','2026-07-10 20:44:29',0,NULL),('PUR-20260710-8690','9be70534-f1be-4b69-bfb0-271ad49700ca',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-10 11:06:48','pending','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','cd4aae1e-cfc7-4d1a-9c43-14e05f119931','2026-07-10 11:06:48','2026-07-10 11:06:48',0,NULL),('PUR-20260711-8815','5365382d-2db4-4c22-9d1c-e21a20474bf9',100.00,0.00,18.00,118.00,'cash',280.00,-162.00,'2026-07-10 21:05:34','pending','Updated purchase notes',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','de44ec1a-07e1-4683-bff0-fa4fdf1b40f2','2026-07-10 21:05:34','2026-07-10 21:05:39',0,NULL),('PUR-20260713-7945','5365382d-2db4-4c22-9d1c-e21a20474bf9',2415.00,0.00,434.70,2849.70,'cash',345.00,2504.70,'2026-07-13 20:48:36','pending','yy',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','e056fa5e-9181-438a-b54b-883233713776','2026-07-13 20:48:36','2026-07-13 20:48:36',0,NULL),('PUR-20260713-9083','65fdce5b-44f6-47f9-b5e1-bc5bafca91a1',144.00,0.00,25.92,169.92,'cash',300.00,-130.08,'2026-07-13 19:51:06','pending','Test purchase B',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','e292aa28-611d-4705-a533-7d8e3b8f81bc','2026-07-13 19:51:06','2026-07-13 19:51:10',1,'2026-07-13 19:51:10'),('PUR-20260710-4504','d666a83d-3ae7-4c85-877f-1607c4a2deb1',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-10 11:46:56','pending','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','f4f8a9c0-f00a-44a7-9cab-0813676fb193','2026-07-10 11:46:56','2026-07-10 11:46:56',0,NULL),('PUR-20260709-2228','f080a161-27eb-4fdc-8d72-63e9c97c8051',250.00,0.00,45.00,295.00,'cash',250.00,45.00,'2026-07-09 08:57:00','pending','Test purchase',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','fd746cc1-0ba0-4840-8c4d-ff3f1c66cf2b','2026-07-09 08:57:00','2026-07-09 08:57:00',0,NULL);
/*!40000 ALTER TABLE `purchases` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_permissions`
--

DROP TABLE IF EXISTS `role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `role_permissions` (
  `role_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `permission_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `unique_role_permission` (`role_id`,`permission_id`),
  KEY `permission_id` (`permission_id`),
  CONSTRAINT `role_permissions_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`),
  CONSTRAINT `role_permissions_ibfk_2` FOREIGN KEY (`permission_id`) REFERENCES `permissions` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_permissions`
--

LOCK TABLES `role_permissions` WRITE;
/*!40000 ALTER TABLE `role_permissions` DISABLE KEYS */;
INSERT INTO `role_permissions` VALUES ('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','9da3026c-f8dd-4692-a795-83c2f0d5ad27','118d3232-afb4-46b0-b05c-eb24555af69a','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','d712ee0b-4ebf-4f18-953e-6719d9db6a99','164fa3fc-553c-46e3-9a7d-3b85754bdd9a','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','9c7809bd-e195-466f-9b80-76fc0c6d6497','2834afeb-2c1d-47ea-a60d-a3714f4ed508','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('d579a1d7-3130-442c-82f3-f7cbee083bb3','80efb2d0-cd5e-4ea0-b82c-f78e9933ebcc','2859547b-b184-463b-8bc4-d8878d3de348','2026-07-10 13:22:50','2026-07-10 13:22:50',0,NULL),('98551a26-5006-41da-9c62-71cb40b11057','45e3b272-c757-43ae-a54a-465a4eb520c4','2c3e4195-9dd0-47ba-907c-2c899f36b3e0','2026-07-10 11:47:13','2026-07-10 11:47:13',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','d55da4be-8579-4281-8e1d-18a18b116191','32af3868-3786-4271-91ab-4a671d4ed516','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','a10fbb42-722a-468a-8f48-78681d9d40c9','3a9e080b-279a-4e4b-aea0-a61a7e8d559d','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('6084df53-e10b-41a1-91ee-8bdf0586e943','b334960e-5b27-455d-9caf-13c7d54accef','44f961b4-fd84-43de-ada8-f773f00a0ee1','2026-07-10 21:04:21','2026-07-10 21:04:21',0,NULL),('84682663-e8da-4fd8-be68-6eca3193b3ed','9c223844-ac36-47da-b3a0-8aabb5aaec2d','4705943e-1901-44d0-a6da-f25648dcc338','2026-07-10 13:42:16','2026-07-10 13:42:16',0,NULL),('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','497eb0b7-c33a-4a4a-9f95-5b885c8f6e46','4bd8b26d-f386-4f1b-a1fe-b16dd3d50f90','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('8f3a4d12-e57b-4960-a52b-de50314fc6fa','ddfc9969-8309-4024-b7d5-6849d455270a','5cb37970-2597-4cfa-8ef2-20a0898b0d22','2026-07-10 20:43:15','2026-07-10 20:43:15',0,NULL),('30df1882-f986-41a8-9b67-26e73c8782c5','946d6879-7719-484e-807f-6e46d0ab33f7','63bb1d94-9019-466e-92ba-c5506f45513b','2026-07-10 11:39:09','2026-07-10 11:39:09',0,NULL),('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','d55da4be-8579-4281-8e1d-18a18b116191','64e5fb1a-a9de-4e3f-93e7-a3375f5eb5b6','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('ddda7b03-e30e-4f40-ad9a-34efb8e390d7','7213d4ee-e653-431c-bce4-40551eb3f94a','6649904b-bcf0-4ec3-9374-abec4ce14ca7','2026-07-13 19:49:49','2026-07-13 19:49:49',0,NULL),('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','bcc10d37-2b9f-467f-898b-629bc6ee21cb','6c5ce7eb-8e4e-4b96-961f-84efee4c59f7','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','d712ee0b-4ebf-4f18-953e-6719d9db6a99','6cbb6dfd-f0d7-49e2-a4cf-0c5dc2c38a51','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','9c7809bd-e195-466f-9b80-76fc0c6d6497','6f21cffe-8901-4ec3-99a5-45a8b025c8d4','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','a10fbb42-722a-468a-8f48-78681d9d40c9','6ff8b0ca-5c95-428e-8fd2-3413f71fc63d','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','a5d0fa20-0aaa-491f-a549-e3d0b34b53f5','7894f83e-c712-4191-acbf-8ebad6014b79','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','a5d0fa20-0aaa-491f-a549-e3d0b34b53f5','9f5d7432-156c-4bdc-98e1-3b21dffd1412','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('68d4620b-dea7-4dce-88d1-f1954ed462a1','b334960e-5b27-455d-9caf-13c7d54accef','a0129501-6a29-4a17-8191-7b3d7bb3cf07','2026-07-10 21:04:23','2026-07-10 21:04:23',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','9aa369ff-25bc-4c8a-abf4-ef61ba792ac8','a09baf14-3d8e-48df-bd30-62e466454ca4','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','9aa369ff-25bc-4c8a-abf4-ef61ba792ac8','a16f89e2-8002-425d-b1b7-714f1fd9ee42','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('c941d940-be28-4670-890b-f5751033dafa','9aa369ff-25bc-4c8a-abf4-ef61ba792ac8','a8f7f2a3-1e0c-4e56-928c-254bedf86f85','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('ceba000e-bdfa-45ec-abe0-7bb44f42f3c8','7213d4ee-e653-431c-bce4-40551eb3f94a','af513a42-593e-4ebe-aa0e-c5ced5084424','2026-07-13 19:49:51','2026-07-13 19:49:51',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','507747cf-3aa0-4b11-bcda-f8a147475b15','b234ec27-5353-4788-b02f-caaf86fef45b','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('8c18e0bb-3fde-4ae3-b367-a060c02fd8c1','ddfc9969-8309-4024-b7d5-6849d455270a','cfd90b1c-0389-4766-8231-d8d72f1a95b2','2026-07-10 20:43:17','2026-07-10 20:43:17',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','497eb0b7-c33a-4a4a-9f95-5b885c8f6e46','de3e7351-76fa-4b50-a0a8-6e588cbfa15d','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','9da3026c-f8dd-4692-a795-83c2f0d5ad27','dfa17877-936a-49c1-b500-6d2006313c5b','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('97437851-0e6e-4c49-9c84-cc0d7ffd7914','bcc10d37-2b9f-467f-898b-629bc6ee21cb','e0be89f0-de0b-4dfe-8d16-0d93d3650ee5','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('c941d940-be28-4670-890b-f5751033dafa','9da3026c-f8dd-4692-a795-83c2f0d5ad27','e7180570-8def-4781-8831-7d5827e9792a','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('da2f859d-ff3b-4e98-94f5-0c5533a4bfee','07ae6653-cc77-4fd7-88b5-b7cd83059fcd','f4295c0b-2c0f-4c97-860a-c4cde3a31983','2026-07-10 13:39:24','2026-07-10 13:39:24',0,NULL);
/*!40000 ALTER TABLE `role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `description` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES ('Test Role 4341','Temporary role for integration testing','30df1882-f986-41a8-9b67-26e73c8782c5','2026-07-10 11:39:09','2026-07-10 11:39:53',1,'2026-07-10 11:39:53'),('Test Role 17837174432023 B','Temporary role B','6084df53-e10b-41a1-91ee-8bdf0586e943','2026-07-10 21:04:21','2026-07-10 21:04:25',1,'2026-07-10 21:04:25'),('Test Role 17837174432023 Updated','Temporary role updated','68d4620b-dea7-4dce-88d1-f1954ed462a1','2026-07-10 21:04:18','2026-07-10 21:04:23',0,NULL),('Test Role 1583','Temporary role for integration testing','84682663-e8da-4fd8-be68-6eca3193b3ed','2026-07-10 13:42:16','2026-07-10 13:43:00',1,'2026-07-10 13:43:00'),('Test Role 17837161771760 Updated','Temporary role updated','8c18e0bb-3fde-4ae3-b367-a060c02fd8c1','2026-07-10 20:43:13','2026-07-10 20:45:02',1,'2026-07-10 20:45:02'),('Test Role 17837161771760 B','Temporary role B','8f3a4d12-e57b-4960-a52b-de50314fc6fa','2026-07-10 20:43:15','2026-07-10 20:43:19',1,'2026-07-10 20:43:19'),('Administrator','Full system access','97437851-0e6e-4c49-9c84-cc0d7ffd7914','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Test Role 4376','Temporary role for integration testing','98551a26-5006-41da-9c62-71cb40b11057','2026-07-10 11:47:13','2026-07-10 11:47:57',1,'2026-07-10 11:47:57'),('Cashier','Process sales and view inventory','c941d940-be28-4670-890b-f5751033dafa','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL),('Test Role 17839721726790 Updated','Temporary role updated','ceba000e-bdfa-45ec-abe0-7bb44f42f3c8','2026-07-13 19:49:47','2026-07-13 19:49:51',0,NULL),('Test Role 7852','Temporary role for integration testing','d579a1d7-3130-442c-82f3-f7cbee083bb3','2026-07-10 13:22:50','2026-07-10 13:23:35',1,'2026-07-10 13:23:35'),('Test Role 3275','Temporary role for integration testing','da2f859d-ff3b-4e98-94f5-0c5533a4bfee','2026-07-10 13:39:24','2026-07-10 13:40:09',1,'2026-07-10 13:40:09'),('Test Role 17839721726790 B','Temporary role B','ddda7b03-e30e-4f40-ad9a-34efb8e390d7','2026-07-13 19:49:49','2026-07-13 19:49:54',1,'2026-07-13 19:49:54'),('Manager','Manage operations and view reports','e3bf73f1-f557-4d60-9f69-3f3d88bee8a3','2026-07-09 08:17:27','2026-07-09 08:17:27',0,NULL);
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale_items`
--

DROP TABLE IF EXISTS `sale_items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sale_items` (
  `sale_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantity` int NOT NULL,
  `unit_price` decimal(10,2) NOT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `unit_cost` decimal(10,2) NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `sale_id` (`sale_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `sale_items_ibfk_1` FOREIGN KEY (`sale_id`) REFERENCES `sales` (`id`),
  CONSTRAINT `sale_items_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale_items`
--

LOCK TABLES `sale_items` WRITE;
/*!40000 ALTER TABLE `sale_items` DISABLE KEYS */;
INSERT INTO `sale_items` VALUES ('04c90282-7e5c-4de3-82fc-3d57845c1d35','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a',7,35.00,0.00,245.00,12.50,'0eaf8b1a-212a-4e59-839d-8c53eacb2920','2026-07-14 11:58:42','2026-07-14 11:58:42',0,NULL),('3fa009d3-a7d0-4268-88f3-820534032c5a','022f4aee-3b9e-43e8-9937-9c0f566bebcc',1,24.00,0.00,24.00,10.00,'1e4fd2fd-479b-4b30-84c7-c84a427bb336','2026-07-13 19:51:14','2026-07-13 19:51:14',0,NULL),('6ce54f65-a221-44f7-ae90-0e35d6e6b412','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753',1,24.00,0.00,24.00,10.00,'38999ef8-d1c5-4c4e-9cb2-9d400718775d','2026-07-10 20:44:39','2026-07-10 20:44:39',0,NULL),('b126e285-1de3-44d7-aefd-df370df4757f','b2315975-218b-42d5-8b4a-4675d7321a3c',1,24.00,0.00,24.00,10.00,'4dc374c3-bd2f-4a52-82bb-47e0723bf4ae','2026-07-10 21:05:45','2026-07-10 21:05:45',0,NULL),('e4c560c3-5af2-4750-9f98-f5635944e8c5','b2315975-218b-42d5-8b4a-4675d7321a3c',1,20.00,0.00,20.00,10.00,'5644b87a-64c8-4e69-be2e-0d8b5e39ca29','2026-07-10 21:05:43','2026-07-10 21:05:43',0,NULL),('ae9d5b15-e543-45e9-b238-4b6ac6576cd6','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753',1,20.00,0.00,20.00,10.00,'a813a5c5-21ba-485b-881a-25d2f09d94fd','2026-07-10 20:44:37','2026-07-10 20:44:37',0,NULL),('d78df9fc-ee13-430d-b855-4117d726ad1c','6e58cc8f-c026-47c8-9c9b-04e179b699ef',2,35.00,0.00,70.00,12.50,'ba15dea1-bec3-4318-9208-c2f520d39256','2026-07-10 13:41:21','2026-07-10 13:41:21',0,NULL),('0866c4f8-06bd-4ca1-85f4-d178c670800f','500c751e-b29c-4067-b52e-7426e708b1f9',1,5000.00,0.00,5000.00,4000.00,'d232caef-642b-4393-a4b6-63bd130b7cf6','2026-07-13 19:47:19','2026-07-13 19:47:19',0,NULL),('8fdd7721-70d4-469f-8a49-e56723325cc9','86aa3fd7-da71-4653-8b3a-86f50950ac30',2,35.00,0.00,70.00,12.50,'e3c1e171-0e8e-459a-8d15-635ac60405a9','2026-07-10 13:38:29','2026-07-10 13:38:29',0,NULL),('9a545dc0-90a9-4b8d-844e-7f906441b0bd','022f4aee-3b9e-43e8-9937-9c0f566bebcc',1,20.00,0.00,20.00,10.00,'ef60c3fb-e785-47a6-adda-8b6c4c87a458','2026-07-13 19:51:12','2026-07-13 19:51:12',0,NULL),('d1e85e41-41ca-448d-a64e-a2e831a1189b','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a',1,35.00,0.00,35.00,12.50,'fd4db4aa-b002-4d1c-81fd-a8ac53c32789','2026-07-13 16:56:08','2026-07-13 16:56:08',0,NULL),('7cec51a4-dc06-48dc-a648-b5bd88416137','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a',2,35.00,0.00,70.00,12.50,'fdc81561-9709-4924-8aed-b3e2435f2e93','2026-07-13 20:10:13','2026-07-13 20:10:13',0,NULL);
/*!40000 ALTER TABLE `sale_items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sales`
--

DROP TABLE IF EXISTS `sales`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sales` (
  `invoice_number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `receipt_number` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `customer_id` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `subtotal` decimal(10,2) DEFAULT NULL,
  `discount` decimal(10,2) DEFAULT NULL,
  `tax` decimal(10,2) DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  `payment_method` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `cash_received` decimal(10,2) DEFAULT NULL,
  `change` decimal(10,2) DEFAULT NULL,
  `total_cost` decimal(10,2) DEFAULT NULL,
  `total_profit` decimal(10,2) DEFAULT NULL,
  `status` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `sale_date` datetime NOT NULL,
  `notes` text COLLATE utf8mb4_unicode_ci,
  `cashier_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `receipt_number` (`receipt_number`),
  UNIQUE KEY `ix_sales_invoice_number` (`invoice_number`),
  KEY `customer_id` (`customer_id`),
  KEY `cashier_id` (`cashier_id`),
  CONSTRAINT `sales_ibfk_1` FOREIGN KEY (`customer_id`) REFERENCES `customers` (`id`),
  CONSTRAINT `sales_ibfk_2` FOREIGN KEY (`cashier_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sales`
--

LOCK TABLES `sales` WRITE;
/*!40000 ALTER TABLE `sales` DISABLE KEYS */;
INSERT INTO `sales` VALUES ('INV-20260714-432106','RCP-20260714-304122',NULL,245.00,0.00,44.10,289.10,'cash',245.00,-44.10,87.50,201.60,'completed','2026-07-14 11:58:42','sale','f35da230-26a8-4696-b03a-c00e184d7826','04c90282-7e5c-4de3-82fc-3d57845c1d35','2026-07-14 11:58:42','2026-07-14 11:58:42',0,NULL),('INV-20260713-291590','RCP-20260713-117340',NULL,5000.00,0.00,900.00,5900.00,'cash',6000.00,100.00,4000.00,1900.00,'completed','2026-07-13 19:47:19','more 1000','f35da230-26a8-4696-b03a-c00e184d7826','0866c4f8-06bd-4ca1-85f4-d178c670800f','2026-07-13 19:47:19','2026-07-13 19:47:19',0,NULL),('INV-20260713-028316','RCP-20260713-194072',NULL,24.00,5.00,4.32,23.32,'cash',120.00,96.68,10.00,13.32,'completed','2026-07-13 19:51:14','Sale B','f35da230-26a8-4696-b03a-c00e184d7826','3fa009d3-a7d0-4268-88f3-820534032c5a','2026-07-13 19:51:14','2026-07-13 19:51:18',1,'2026-07-13 19:51:18'),('INV-20260710-728361','RCP-20260710-516336',NULL,24.00,5.00,4.32,23.32,'cash',120.00,96.68,10.00,13.32,'completed','2026-07-10 20:44:39','Sale B','f35da230-26a8-4696-b03a-c00e184d7826','6ce54f65-a221-44f7-ae90-0e35d6e6b412','2026-07-10 20:44:39','2026-07-10 20:44:39',0,NULL),('INV-20260713-055525','RCP-20260713-754017',NULL,70.00,0.00,12.60,82.60,'cash',69.99,-12.61,25.00,57.60,'completed','2026-07-13 20:10:13','k','f35da230-26a8-4696-b03a-c00e184d7826','7cec51a4-dc06-48dc-a648-b5bd88416137','2026-07-13 20:10:13','2026-07-13 20:10:13',0,NULL),('INV-20260710-298490','RCP-20260710-225562',NULL,70.00,5.00,12.60,77.60,'cash',100.00,22.40,25.00,52.60,'refunded','2026-07-10 13:38:29','Updated sale notes','f35da230-26a8-4696-b03a-c00e184d7826','8fdd7721-70d4-469f-8a49-e56723325cc9','2026-07-10 13:38:29','2026-07-10 16:45:29',0,NULL),('INV-20260713-146416','RCP-20260713-141392',NULL,20.00,10.00,3.60,13.60,'cash',100.00,86.40,10.00,3.60,'completed','2026-07-13 19:51:12','Updated sale notes','f35da230-26a8-4696-b03a-c00e184d7826','9a545dc0-90a9-4b8d-844e-7f906441b0bd','2026-07-13 19:51:12','2026-07-13 19:51:16',0,NULL),('INV-20260710-657289','RCP-20260710-233735',NULL,20.00,10.00,3.60,13.60,'cash',100.00,86.40,10.00,3.60,'completed','2026-07-10 20:44:37','Updated sale notes','f35da230-26a8-4696-b03a-c00e184d7826','ae9d5b15-e543-45e9-b238-4b6ac6576cd6','2026-07-10 20:44:37','2026-07-10 20:44:41',0,NULL),('INV-20260711-629262','RCP-20260711-564482',NULL,24.00,5.00,4.32,23.32,'cash',120.00,96.68,10.00,13.32,'completed','2026-07-10 21:05:45','Sale B','f35da230-26a8-4696-b03a-c00e184d7826','b126e285-1de3-44d7-aefd-df370df4757f','2026-07-10 21:05:45','2026-07-10 21:05:49',1,'2026-07-10 21:05:49'),('INV-20260713-365883','RCP-20260713-689230',NULL,35.00,0.00,6.30,41.30,'cash',500.00,458.70,12.50,28.80,'completed','2026-07-13 16:56:08','7','f35da230-26a8-4696-b03a-c00e184d7826','d1e85e41-41ca-448d-a64e-a2e831a1189b','2026-07-13 16:56:08','2026-07-13 16:56:08',0,NULL),('INV-20260710-858282','RCP-20260710-040107',NULL,70.00,5.00,12.60,77.60,'cash',100.00,22.40,25.00,52.60,'completed','2026-07-10 13:41:21','Testing customer sale','f35da230-26a8-4696-b03a-c00e184d7826','d78df9fc-ee13-430d-b855-4117d726ad1c','2026-07-10 13:41:21','2026-07-10 13:41:21',0,NULL),('INV-20260711-335984','RCP-20260711-594126',NULL,20.00,10.00,3.60,13.60,'cash',100.00,86.40,10.00,3.60,'completed','2026-07-10 21:05:43','Updated sale notes','f35da230-26a8-4696-b03a-c00e184d7826','e4c560c3-5af2-4750-9f98-f5635944e8c5','2026-07-10 21:05:43','2026-07-10 21:05:47',0,NULL);
/*!40000 ALTER TABLE `sales` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `settings` (
  `shop_name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `logo` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `currency` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL,
  `currency_symbol` varchar(5) COLLATE utf8mb4_unicode_ci NOT NULL,
  `tax_percentage` int NOT NULL,
  `receipt_footer` text COLLATE utf8mb4_unicode_ci,
  `receipt_header` text COLLATE utf8mb4_unicode_ci,
  `low_stock_limit` int NOT NULL,
  `dark_mode` tinyint(1) NOT NULL,
  `tin_number` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `settings`
--

LOCK TABLES `settings` WRITE;
/*!40000 ALTER TABLE `settings` DISABLE KEYS */;
INSERT INTO `settings` VALUES ('Boutique Shop-1583 (Updated)',NULL,'Burayyuu Keellaa',NULL,NULL,'ETB','$',15,'Thank you for shopping with us!','Anane Boutique Shop',10,0,NULL,'6f4fd3fa-0f47-4baa-beff-f33d56e86d24','2026-07-09 08:17:27','2026-07-10 13:42:37',0,NULL);
/*!40000 ALTER TABLE `settings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stock_movements`
--

DROP TABLE IF EXISTS `stock_movements`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stock_movements` (
  `inventory_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `product_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `movement_type` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `quantity` int NOT NULL,
  `previous_quantity` int NOT NULL,
  `new_quantity` int NOT NULL,
  `reference_type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reference_id` varchar(36) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `reason` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `notes` text COLLATE utf8mb4_unicode_ci,
  `performed_by` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `inventory_id` (`inventory_id`),
  KEY `product_id` (`product_id`),
  KEY `performed_by` (`performed_by`),
  CONSTRAINT `stock_movements_ibfk_1` FOREIGN KEY (`inventory_id`) REFERENCES `inventory` (`id`),
  CONSTRAINT `stock_movements_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `products` (`id`),
  CONSTRAINT `stock_movements_ibfk_3` FOREIGN KEY (`performed_by`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stock_movements`
--

LOCK TABLES `stock_movements` WRITE;
/*!40000 ALTER TABLE `stock_movements` DISABLE KEYS */;
INSERT INTO `stock_movements` VALUES ('62331fd4-e1ee-4a2d-9b4f-1ee17aa8d966','b2315975-218b-42d5-8b4a-4675d7321a3c','stock_in',10,0,10,'purchase','de44ec1a-07e1-4683-bff0-fa4fdf1b40f2','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','07883480-f6a8-4026-adaf-0e7e646b5a10','2026-07-10 21:05:34','2026-07-10 21:05:34',0,NULL),('29ccd2d6-3db6-4b85-8da6-b9a9299cf014','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a','stock_out',2,10,8,'sale','7cec51a4-dc06-48dc-a648-b5bd88416137','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','102f7d35-fec0-4e99-ae19-47a5b907e2a8','2026-07-13 20:10:13','2026-07-13 20:10:13',0,NULL),('ac5f3c5c-02d3-4ebb-9348-9f04dcbfb90b','47941fba-e8f7-4638-85a2-c777260a1d1b','stock_in',20,100,120,'purchase','cd4aae1e-cfc7-4d1a-9c43-14e05f119931','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','1f6e164c-ba58-4eb7-aea8-d5985a9fd43b','2026-07-10 11:06:48','2026-07-10 11:06:48',0,NULL),('2c61448c-e094-42ee-97f3-e223470d2b78','86aa3fd7-da71-4653-8b3a-86f50950ac30','stock_in',20,98,118,'purchase','0c541f77-9a75-4c11-80c5-e602ab03dea2','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','306bd139-072c-4717-a6eb-f26c1e33a31a','2026-07-10 13:39:05','2026-07-10 13:39:05',0,NULL),('9c82aa5d-61ef-4a0a-9822-9b282e822a2d','0019750d-56f9-41c9-9c74-a62180b7ec8e','stock_in',20,100,120,'purchase','36f48ea5-d091-4fc8-aad7-c144164c6eff','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','3ab3a148-df2c-4445-91b2-1716b2c52489','2026-07-10 11:38:55','2026-07-10 11:38:55',0,NULL),('62331fd4-e1ee-4a2d-9b4f-1ee17aa8d966','b2315975-218b-42d5-8b4a-4675d7321a3c','stock_out',1,22,21,'sale','e4c560c3-5af2-4750-9f98-f5635944e8c5','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','47f5d0d6-2fb6-4dbe-97bd-b3f2db3f83fb','2026-07-10 21:05:43','2026-07-10 21:05:43',0,NULL),('c3b32557-d66f-497d-968f-2f1cf2ed79db','022f4aee-3b9e-43e8-9937-9c0f566bebcc','stock_in',10,0,10,'purchase','a0690caa-7e9a-476a-b3e4-c2cdeffb9c1f','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','494ce594-ff42-42bc-9166-32b655f8b3b4','2026-07-13 19:51:04','2026-07-13 19:51:04',0,NULL),('2c61448c-e094-42ee-97f3-e223470d2b78','86aa3fd7-da71-4653-8b3a-86f50950ac30','stock_out',2,100,98,'sale','8fdd7721-70d4-469f-8a49-e56723325cc9','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','49da080f-d7c5-46c9-b9dc-0b1a8fda6f39','2026-07-10 13:38:29','2026-07-10 13:38:29',0,NULL),('1c89b5bb-c7ad-4ad6-80bf-60a343cd144f','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753','stock_in',12,10,22,'purchase','8d454557-3895-4b8d-8296-9b1dba84c651','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','4ccb7d2a-ed7f-4229-9b90-badb4a6a0908','2026-07-10 20:44:31','2026-07-10 20:44:31',0,NULL),('29ccd2d6-3db6-4b85-8da6-b9a9299cf014','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a','adjustment',10,0,10,'adjustment',NULL,'inv','inv','f35da230-26a8-4696-b03a-c00e184d7826','4dc230f3-79bf-4fe2-9d6f-b9abced6da0f','2026-07-10 21:25:47','2026-07-10 21:25:47',0,NULL),('d3d01fa9-6554-459d-abe8-4be74e7078cb','6e58cc8f-c026-47c8-9c9b-04e179b699ef','adjustment',100,0,100,'adjustment',NULL,'Initial stock intake','Testing automated script addition','f35da230-26a8-4696-b03a-c00e184d7826','53129f5a-b451-46fd-8f12-561738710d6f','2026-07-10 13:41:17','2026-07-10 13:41:17',0,NULL),('29ccd2d6-3db6-4b85-8da6-b9a9299cf014','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a','stock_out',7,8,1,'sale','04c90282-7e5c-4de3-82fc-3d57845c1d35','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','56f23271-6796-48ee-acbc-ce4e90406309','2026-07-14 11:58:42','2026-07-14 11:58:42',0,NULL),('51d31d4b-d103-459b-8809-5a29c01cacaa','d40bfad1-2be4-4724-87cc-e2ec662d2573','adjustment',100,0,100,'adjustment',NULL,'Initial stock intake','Testing automated script addition','f35da230-26a8-4696-b03a-c00e184d7826','5d959419-0c14-4cf8-a54e-d22ee3545fcc','2026-07-10 11:46:17','2026-07-10 11:46:17',0,NULL),('1c89b5bb-c7ad-4ad6-80bf-60a343cd144f','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753','stock_out',1,21,20,'sale','6ce54f65-a221-44f7-ae90-0e35d6e6b412','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','65453cce-75d6-4b07-8a11-117b016b0b22','2026-07-10 20:44:39','2026-07-10 20:44:39',0,NULL),('c3b32557-d66f-497d-968f-2f1cf2ed79db','022f4aee-3b9e-43e8-9937-9c0f566bebcc','stock_out',1,21,20,'sale','3fa009d3-a7d0-4268-88f3-820534032c5a','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','65cc6085-98d7-4e38-88d6-4387cd9760c3','2026-07-13 19:51:14','2026-07-13 19:51:14',0,NULL),('29ccd2d6-3db6-4b85-8da6-b9a9299cf014','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a','stock_in',1,10,11,'purchase','6a4dcb9f-5a57-4874-a2f9-1ce619f6c51e','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','660a2782-626c-48e8-80dd-b854bd0d6a4b','2026-07-13 16:54:00','2026-07-13 16:54:00',0,NULL),('62331fd4-e1ee-4a2d-9b4f-1ee17aa8d966','b2315975-218b-42d5-8b4a-4675d7321a3c','stock_out',1,21,20,'sale','b126e285-1de3-44d7-aefd-df370df4757f','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','6ba6c7a5-ba18-45ad-8cab-516698df55dc','2026-07-10 21:05:45','2026-07-10 21:05:45',0,NULL),('2c61448c-e094-42ee-97f3-e223470d2b78','86aa3fd7-da71-4653-8b3a-86f50950ac30','stock_in',2,118,120,'refund','8fdd7721-70d4-469f-8a49-e56723325cc9','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','6f2b216c-c8e7-4c90-95c8-95f786c7d1dc','2026-07-10 16:45:29','2026-07-10 16:45:29',0,NULL),('9c82aa5d-61ef-4a0a-9822-9b282e822a2d','0019750d-56f9-41c9-9c74-a62180b7ec8e','adjustment',100,0,100,'adjustment',NULL,'Initial stock intake','Testing automated script addition','f35da230-26a8-4696-b03a-c00e184d7826','7430e925-d015-45b8-bbef-ea6af98c733e','2026-07-10 11:38:15','2026-07-10 11:38:15',0,NULL),('a811c39e-ed1f-42ee-bd2c-55cba3e466b9','1627e0ae-34fc-4029-b997-59bb231dc61d','stock_in',20,0,20,'purchase','919eded7-efeb-466d-a538-b55327c9de50','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','7a9f3e7a-2e8e-4850-ad67-d4efc3dd6f9c','2026-07-09 11:19:12','2026-07-09 11:19:12',0,NULL),('62331fd4-e1ee-4a2d-9b4f-1ee17aa8d966','b2315975-218b-42d5-8b4a-4675d7321a3c','stock_in',12,10,22,'purchase','5db8ed96-b4d9-4359-9465-716f29a50fa3','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','88df849c-7d0f-43ad-9c2a-0852cd232948','2026-07-10 21:05:37','2026-07-10 21:05:37',0,NULL),('7db8f373-d233-42ce-aa05-bfcf8af34a06','500c751e-b29c-4067-b52e-7426e708b1f9','stock_in',7,10,17,'purchase','e056fa5e-9181-438a-b54b-883233713776','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','92b78d13-ddb4-47c4-9531-6920b827c99c','2026-07-13 20:48:36','2026-07-13 20:48:36',0,NULL),('1c89b5bb-c7ad-4ad6-80bf-60a343cd144f','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753','stock_out',1,22,21,'sale','ae9d5b15-e543-45e9-b238-4b6ac6576cd6','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','9b9fe94a-8b04-45a7-855c-66bea6c2f2dc','2026-07-10 20:44:37','2026-07-10 20:44:37',0,NULL),('894041c2-be7c-4e1d-a854-a10d4768a5a4','36104e9a-06ef-4fc4-8a2f-358ea09115f8','adjustment',100,0,100,'adjustment',NULL,'Initial stock intake','Testing automated script addition','f35da230-26a8-4696-b03a-c00e184d7826','9f5ba5fc-187b-47c9-8948-7ac946e30475','2026-07-09 13:27:23','2026-07-09 13:27:23',0,NULL),('7db8f373-d233-42ce-aa05-bfcf8af34a06','500c751e-b29c-4067-b52e-7426e708b1f9','stock_in',11,0,11,'purchase','3f4d06a9-f38a-4968-9a27-00c1caf3d7e1','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','a6afd175-baea-4f59-8ac5-2aaeb12b3015','2026-07-13 19:46:18','2026-07-13 19:46:18',0,NULL),('2c61448c-e094-42ee-97f3-e223470d2b78','86aa3fd7-da71-4653-8b3a-86f50950ac30','adjustment',100,0,100,'adjustment',NULL,'Initial stock intake','Testing automated script addition','f35da230-26a8-4696-b03a-c00e184d7826','a7373832-59c4-4f09-a742-aa2a2b61095e','2026-07-10 13:38:25','2026-07-10 13:38:25',0,NULL),('ac5f3c5c-02d3-4ebb-9348-9f04dcbfb90b','47941fba-e8f7-4638-85a2-c777260a1d1b','adjustment',100,0,100,'adjustment',NULL,'Initial stock intake','Testing automated script addition','f35da230-26a8-4696-b03a-c00e184d7826','a8a0d3a9-a488-4361-8a6a-41c20414bf76','2026-07-10 11:06:09','2026-07-10 11:06:09',0,NULL),('c3b32557-d66f-497d-968f-2f1cf2ed79db','022f4aee-3b9e-43e8-9937-9c0f566bebcc','stock_in',12,10,22,'purchase','e292aa28-611d-4705-a533-7d8e3b8f81bc','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','a9a902b8-262a-4dd7-a475-7ae7b59be5f3','2026-07-13 19:51:06','2026-07-13 19:51:06',0,NULL),('51d31d4b-d103-459b-8809-5a29c01cacaa','d40bfad1-2be4-4724-87cc-e2ec662d2573','stock_in',20,100,120,'purchase','f4f8a9c0-f00a-44a7-9cab-0813676fb193','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','b1d734ee-2f23-4050-bc6a-f12952e1cfa2','2026-07-10 11:46:56','2026-07-10 11:46:56',0,NULL),('c3b32557-d66f-497d-968f-2f1cf2ed79db','022f4aee-3b9e-43e8-9937-9c0f566bebcc','stock_out',1,22,21,'sale','9a545dc0-90a9-4b8d-844e-7f906441b0bd','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','bd48626b-0a88-459b-9790-a622b6021d75','2026-07-13 19:51:12','2026-07-13 19:51:12',0,NULL),('894041c2-be7c-4e1d-a854-a10d4768a5a4','36104e9a-06ef-4fc4-8a2f-358ea09115f8','stock_in',20,100,120,'purchase','7330ba8d-bc2c-4e24-a946-36e9d166c058','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','c25acbf6-acf0-4c42-b400-43ae90de37a8','2026-07-09 13:28:03','2026-07-09 13:28:03',0,NULL),('29ccd2d6-3db6-4b85-8da6-b9a9299cf014','12be64ff-18f3-42cf-a1e1-8a5dd2454b6a','stock_out',1,11,10,'sale','d1e85e41-41ca-448d-a64e-a2e831a1189b','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','d02fd020-1c98-4de1-a397-7d5601ec03ba','2026-07-13 16:56:08','2026-07-13 16:56:08',0,NULL),('d3d01fa9-6554-459d-abe8-4be74e7078cb','6e58cc8f-c026-47c8-9c9b-04e179b699ef','stock_out',2,100,98,'sale','d78df9fc-ee13-430d-b855-4117d726ad1c','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','d0a91b1a-c40a-41c4-baea-6f453759ab5e','2026-07-10 13:41:21','2026-07-10 13:41:21',0,NULL),('bbf0d557-4541-407e-8ae0-0257f041fb0c','494e0824-e1d6-4cec-b733-cbbf23cc2855','stock_in',20,100,120,'purchase','51566935-8a36-4b15-a6aa-30bbb4da2f90','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','d0b6d8f4-0836-475f-a660-bdc32792bebb','2026-07-10 13:22:34','2026-07-10 13:22:34',0,NULL),('7e1b5608-8d93-4cb4-9fd5-8225772f336a','230e297a-772d-4d71-82c2-dac539b2a84a','adjustment',100,0,100,'adjustment',NULL,'Initial stock intake','Testing automated script addition','f35da230-26a8-4696-b03a-c00e184d7826','d759a5af-b16c-4e05-9c1a-58267fc70d1a','2026-07-09 13:34:39','2026-07-09 13:34:39',0,NULL),('d3d01fa9-6554-459d-abe8-4be74e7078cb','6e58cc8f-c026-47c8-9c9b-04e179b699ef','stock_in',20,98,118,'purchase','0d4d9e69-97af-4770-9640-55a5d21aa949','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','e89221a4-a141-485a-9cbb-18d269013a95','2026-07-10 13:41:57','2026-07-10 13:41:57',0,NULL),('1c89b5bb-c7ad-4ad6-80bf-60a343cd144f','0f4c7cbd-17f0-4e7e-80ee-86a7ec542753','stock_in',10,0,10,'purchase','a6819b2c-79af-4703-ae97-75ee76e09e6b','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','e924057a-7b1e-4ed9-ab76-3b4593628aa3','2026-07-10 20:44:29','2026-07-10 20:44:29',0,NULL),('bbf0d557-4541-407e-8ae0-0257f041fb0c','494e0824-e1d6-4cec-b733-cbbf23cc2855','adjustment',100,0,100,'adjustment',NULL,'Initial stock intake','Testing automated script addition','f35da230-26a8-4696-b03a-c00e184d7826','e9781f1a-d471-4b39-842a-24ff5f239a93','2026-07-10 13:21:54','2026-07-10 13:21:54',0,NULL),('dc39ca6b-7805-42e8-86ff-f5a4823f2e36','8631909c-d123-405c-b897-7d960284d401','stock_in',20,0,20,'purchase','fd746cc1-0ba0-4840-8c4d-ff3f1c66cf2b','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','ea788e39-cc35-400d-b4c3-48c67dca6065','2026-07-09 08:57:00','2026-07-09 08:57:00',0,NULL),('7e1b5608-8d93-4cb4-9fd5-8225772f336a','230e297a-772d-4d71-82c2-dac539b2a84a','stock_in',20,100,120,'purchase','43b78693-839e-4127-9982-14a74db53a45','Stock in',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','f892dde8-736b-4180-a401-1807d77f937b','2026-07-09 13:35:18','2026-07-09 13:35:18',0,NULL),('7db8f373-d233-42ce-aa05-bfcf8af34a06','500c751e-b29c-4067-b52e-7426e708b1f9','stock_out',1,11,10,'sale','0866c4f8-06bd-4ca1-85f4-d178c670800f','Stock out',NULL,'f35da230-26a8-4696-b03a-c00e184d7826','fadd56e4-3214-4f36-963d-b45d2520bf52','2026-07-13 19:47:19','2026-07-13 19:47:19',0,NULL);
/*!40000 ALTER TABLE `stock_movements` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `suppliers`
--

DROP TABLE IF EXISTS `suppliers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `suppliers` (
  `name` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `contact_person` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tin_number` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `outstanding_balance` decimal(10,2) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `ix_suppliers_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `suppliers`
--

LOCK TABLES `suppliers` WRITE;
/*!40000 ALTER TABLE `suppliers` DISABLE KEYS */;
INSERT INTO `suppliers` VALUES ('Supplier 17837161771760 B','Jane Doe','+251911567004','supplier17837161771760b@example.com','Dire Dawa','TIN17837161771760B',0.00,1,'10d82d31-f557-4aab-8dd0-e060682c23e0','2026-07-10 20:43:57','2026-07-10 20:44:01',1,'2026-07-10 20:44:01'),('ABC Suppliers Ltd-2069 (Updated)','John Doe','+2519112070','john2069@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'234e8cd0-b4b4-448a-9e42-7e6756f745e1','2026-07-09 13:27:50','2026-07-09 13:28:38',1,'2026-07-09 13:28:38'),('ABC Suppliers Ltd-7852 (Updated)','John Doe','+2519117853','john7852@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'32581434-8042-4dff-9d0a-9524a27b3803','2026-07-10 13:22:21','2026-07-10 13:23:45',1,'2026-07-10 13:23:45'),('ABC Suppliers Ltd-1583 (Updated)','John Doe','+2519111584','john1583@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'46c51315-758f-4fd3-b896-50e71a5b7fcf','2026-07-10 13:41:44','2026-07-10 13:43:11',1,'2026-07-10 13:43:11'),('Supplier 17837174432023 Updated','John Doe','+251911117681','supplier17837174432023a@example.com','Addis Ababa','TIN17837174432023A',2504.70,1,'5365382d-2db4-4c22-9d1c-e21a20474bf9','2026-07-10 21:05:01','2026-07-13 20:48:36',0,NULL),('Supplier 17839721726790 Updated','John Doe','+251911674045','supplier17839721726790a@example.com','Addis Ababa','TIN17839721726790A',0.00,1,'65fdce5b-44f6-47f9-b5e1-bc5bafca91a1','2026-07-13 19:50:30','2026-07-13 19:50:34',0,NULL),('ABC Suppliers Ltd','John Doe','+251911234567','john@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',47965.00,1,'69a99807-ddf2-41b1-8199-920e894d63d7','2026-07-09 11:19:02','2026-07-13 19:46:18',0,NULL),('Supplier 17839721726790 B','Jane Doe','+251911176525','supplier17839721726790b@example.com','Dire Dawa','TIN17839721726790B',0.00,1,'71dec074-fb90-44d2-ac35-66ca726f50a3','2026-07-13 19:50:32','2026-07-13 19:50:36',1,'2026-07-13 19:50:36'),('ABC Suppliers Ltd-6071 (Updated)','John Doe','+2519116072','john6071@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'7e0301a4-868a-4cda-a8bd-790701af0786','2026-07-09 13:35:06','2026-07-09 13:36:02',1,'2026-07-09 13:36:02'),('Test Supplier','bayisa','0919774799','ebrahim19usman@gmail.com','Yabello','12341234',0.00,1,'958a5c0f-326d-46c2-9d85-a39bb935b77c','2026-07-10 08:48:58','2026-07-10 08:48:58',0,NULL),('ABC Suppliers Ltd-6287 (Updated)','John Doe','+2519116288','john6287@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'9be70534-f1be-4b69-bfb0-271ad49700ca','2026-07-10 11:06:36','2026-07-10 11:07:33',1,'2026-07-10 11:07:33'),('ABC Suppliers Ltd-4341 (Updated)','John Doe','+2519114342','john4341@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'c5566765-2e46-4883-8079-fec88d10c48f','2026-07-10 11:38:42','2026-07-10 11:40:01',1,'2026-07-10 11:40:01'),('Supplier 17837161771760 Updated','John Doe','+251911706412','supplier17837161771760a@example.com','Addis Ababa','TIN17837161771760A',0.00,1,'c7700d2d-e39f-4b25-8e4c-5fde4e67e1b9','2026-07-10 20:43:55','2026-07-10 20:45:13',1,'2026-07-10 20:45:13'),('ABC Suppliers Ltd-3275 (Updated)','John Doe','+2519113276','john3275@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'cd74230e-cecc-4c16-a504-ffbf677cdfed','2026-07-10 13:38:52','2026-07-10 13:40:19',1,'2026-07-10 13:40:19'),('ABC Suppliers Ltd-4376 (Updated)','John Doe','+2519114377','john4376@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'d666a83d-3ae7-4c85-877f-1607c4a2deb1','2026-07-10 11:46:44','2026-07-10 11:48:07',1,'2026-07-10 11:48:07'),('Supplier 17837174432023 B','Jane Doe','+251911387939','supplier17837174432023b@example.com','Dire Dawa','TIN17837174432023B',0.00,1,'d7f62d92-2d25-431f-a47f-04ae2b664ddb','2026-07-10 21:05:03','2026-07-10 21:05:07',1,'2026-07-10 21:05:07'),('ABC Suppliers Ltd (Updated)','John Doe','+251911765432','john@abcsuppliers.com','Addis Ababa, Ethiopia','1234567890',45.00,1,'f080a161-27eb-4fdc-8d72-63e9c97c8051','2026-07-09 08:56:47','2026-07-09 08:57:00',0,NULL);
/*!40000 ALTER TABLE `suppliers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_roles`
--

DROP TABLE IF EXISTS `user_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_roles` (
  `user_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role_id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  UNIQUE KEY `unique_user_role` (`user_id`,`role_id`),
  KEY `role_id` (`role_id`),
  CONSTRAINT `user_roles_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`),
  CONSTRAINT `user_roles_ibfk_2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_roles`
--

LOCK TABLES `user_roles` WRITE;
/*!40000 ALTER TABLE `user_roles` DISABLE KEYS */;
INSERT INTO `user_roles` VALUES ('44a1fd09-d755-4b29-b596-bce3533397e2','30df1882-f986-41a8-9b67-26e73c8782c5'),('1ba937c7-03ef-4652-97ab-30b9d2316bc7','68d4620b-dea7-4dce-88d1-f1954ed462a1'),('7ba1e1c1-51e9-45d2-9f2e-67bdb2bd1528','68d4620b-dea7-4dce-88d1-f1954ed462a1'),('3e4af0f3-49fd-485d-94fc-8aa0aae96a5d','84682663-e8da-4fd8-be68-6eca3193b3ed'),('53ecf9ae-e63e-419d-82f3-a68d43ff010b','8c18e0bb-3fde-4ae3-b367-a060c02fd8c1'),('94f18c49-a3e8-40e2-a8dd-31edce37a122','8c18e0bb-3fde-4ae3-b367-a060c02fd8c1'),('f35da230-26a8-4696-b03a-c00e184d7826','97437851-0e6e-4c49-9c84-cc0d7ffd7914'),('14c1c696-44e5-4488-9381-602c37b9cf6b','98551a26-5006-41da-9c62-71cb40b11057'),('58cb9915-049b-40b0-9d5c-ee810c655b4d','ceba000e-bdfa-45ec-abe0-7bb44f42f3c8'),('838c2961-75a6-4ce2-929e-dd72740eeafb','ceba000e-bdfa-45ec-abe0-7bb44f42f3c8'),('b3e205c8-9f68-4066-93b1-8fceac6c4d92','d579a1d7-3130-442c-82f3-f7cbee083bb3'),('8be0a5e8-7e69-409e-b83d-8d0afd20f8b3','da2f859d-ff3b-4e98-94f5-0c5533a4bfee');
/*!40000 ALTER TABLE `user_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `username` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `email` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password_hash` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `phone` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `address` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `profile_image` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `id` varchar(36) COLLATE utf8mb4_unicode_ci NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `is_deleted` tinyint(1) NOT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ix_users_email` (`email`),
  UNIQUE KEY `ix_users_username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('testuser4376','testuser4376@example.com','scrypt:32768:8:1$lRXhyb8IL1eMvIFA$1690db36e97aa42316a5ea79228678790108a3709925168e32879ab5b199ee72fb4b82851867ad8b3d9d0d47cb445eb042ed753fb96ac92ed7574a0d50438af5','Test-4376 (Updated)','User-4376 (Updated)','+2519114379',NULL,NULL,1,NULL,'14c1c696-44e5-4488-9381-602c37b9cf6b','2026-07-10 11:47:15','2026-07-10 11:47:55',1,'2026-07-10 11:47:55'),('testuser17837174432023a','updated17837174432023@example.com','scrypt:32768:8:1$DjibWN8671KvwzUh$3d41829c54bb863bf03a4dbf6c6a9aaae1bfec9e931c0e8feff66be9d2f55288f1ad9378d621445ae38edb31f8023dcca6a8337249e8d5c2552beae6ed460817','Test-17837174432023','User-17837174432023','+251911188576',NULL,NULL,1,NULL,'1ba937c7-03ef-4652-97ab-30b9d2316bc7','2026-07-10 21:04:27','2026-07-10 21:04:31',0,NULL),('testuser1583','testuser1583@example.com','scrypt:32768:8:1$E4vpRlsjNjXjnvTW$d0c9f8298b22b715795d560579b88263c4a5ada135737e32ccd681a6a4c75ffca34dec9ef6891aba4b9c7f43f70d5fb838c4d92cd21ab314ebe1cbf4e518e7b1','Test-1583 (Updated)','User-1583 (Updated)','+2519111586',NULL,NULL,1,NULL,'3e4af0f3-49fd-485d-94fc-8aa0aae96a5d','2026-07-10 13:42:18','2026-07-10 13:42:58',1,'2026-07-10 13:42:58'),('testuser4341','testuser4341@example.com','scrypt:32768:8:1$w8xk3mdTKH4AStEx$ae567e7cae15898db7f04f3a9645988993164c6f842744418390a71e7e061ceb56cb9b94c99acf791766f23681070237b10b21ab143e574c9c355d12c6a09092','Test-4341 (Updated)','User-4341 (Updated)','+2519114344',NULL,NULL,1,NULL,'44a1fd09-d755-4b29-b596-bce3533397e2','2026-07-10 11:39:11','2026-07-10 11:39:51',1,'2026-07-10 11:39:51'),('testuser6287','testuser6287@example.com','scrypt:32768:8:1$iQUExDXDDV9bl2L3$8cfa4719763daf3fe00ac39dfa431c254734234fb08238dc80d59d7115c27f9e52522e6767a393a1cc83dde4f9da22a5e630afe76e3bea7fc93f3e8578506aea','Test-6287 (Updated)','User-6287 (Updated)','+2519116290',NULL,NULL,1,NULL,'51728bea-8dea-43e7-ae1e-b563e4f791a3','2026-07-10 11:07:01','2026-07-10 11:07:26',1,'2026-07-10 11:07:26'),('testuser17837161771760b','testuser17837161771760b@example.com','scrypt:32768:8:1$aSykAlNa4eGRuMD5$0a437ae049a0fa62e2bc578312212c63750e3e569a4571e85eac15a25d9fc81594dfe1b818f68970f2caad585bde6b1595dc0ca04ef6dc1c4cf83dad004fa737','Test','User B','+251911865192',NULL,NULL,1,NULL,'53ecf9ae-e63e-419d-82f3-a68d43ff010b','2026-07-10 20:43:24','2026-07-10 20:43:28',1,'2026-07-10 20:43:28'),('testuser17839721726790b','testuser17839721726790b@example.com','scrypt:32768:8:1$SYCWR58ebckuAIZu$fc1ca79069307aaf4e44892ea347fcd9c82bb6b5640abd5a934e25e7ee3f22d7983f28a5720aa847883b09688259af3343a98d751ef32159b4c6f4a59391376c','Test','User B','+251911993474',NULL,NULL,1,NULL,'58cb9915-049b-40b0-9d5c-ee810c655b4d','2026-07-13 19:49:58','2026-07-13 19:50:02',1,'2026-07-13 19:50:02'),('testuser6071','testuser6071@example.com','scrypt:32768:8:1$Uu4MQlMecxYCfFbm$1f54fee36dbaa066566b475586d763f47492b7c5920e95b6ce1c2a2afd4ba52e462a21e9b4a65ae2db35391959ebcb20b52c5a2ba65c3f1201730834550daeaa','Test-6071 (Updated)','User-6071 (Updated)','+2519116074',NULL,NULL,1,NULL,'5c350a12-ba24-4575-b325-7997241a8133','2026-07-09 13:35:31','2026-07-09 13:35:56',1,'2026-07-09 13:35:56'),('testuser17837174432023b','testuser17837174432023b@example.com','scrypt:32768:8:1$D7Gh5SHaW65it7Ul$ab5019e029ab69f61784cabb37da6cc233292e49067d4fd56dfeaf05cf59f534e63d4cfa7f588400c4be3ddd32b2d666b9b42618dfff126581d418acfbe487ae','Test','User B','+251911374887',NULL,NULL,1,NULL,'7ba1e1c1-51e9-45d2-9f2e-67bdb2bd1528','2026-07-10 21:04:29','2026-07-10 21:04:33',1,'2026-07-10 21:04:33'),('testuser17839721726790a','updated17839721726790@example.com','scrypt:32768:8:1$xnMzebELVT2wIwN1$867814cafd981b8b7c913def15d7fa6524a84b101ab0bf2ff8c65ae0e5350b0d953f2e76f78b4cc9d6a0cc74505dd214d6e57d03101eb1903c507a14e0eeceac','Test-17839721726790','User-17839721726790','+251911677358',NULL,NULL,1,NULL,'838c2961-75a6-4ce2-929e-dd72740eeafb','2026-07-13 19:49:56','2026-07-13 19:50:00',0,NULL),('testuser3275','testuser3275@example.com','scrypt:32768:8:1$bA3rC6wJGDcu2aEC$0481773dc64e49b93912c49e9dcf76445e6c2ad96e5eb09037388f1b861fe3b1b7b81f2e9b3df01d893c7d328735cb4256e492dc8a78f4bef5c2105437ecbf82','Test-3275 (Updated)','User-3275 (Updated)','+2519113278',NULL,NULL,1,NULL,'8be0a5e8-7e69-409e-b83d-8d0afd20f8b3','2026-07-10 13:39:27','2026-07-10 13:40:07',1,'2026-07-10 13:40:07'),('testuser17837161771760a','updated17837161771760@example.com','scrypt:32768:8:1$LRtVIjm4Yrgd2aKc$c97705bf27ba56441365115c0eac3005036742f09bff36c22726d3d8f45837ed950206085ddc5f673dc6cce9e3e878dc85ed5411fd18baf410bb44476fab83f3','Test-17837161771760','User-17837161771760','+251911120367',NULL,NULL,1,NULL,'94f18c49-a3e8-40e2-a8dd-31edce37a122','2026-07-10 20:43:21','2026-07-10 20:45:04',1,'2026-07-10 20:45:04'),('testuser7852','testuser7852@example.com','scrypt:32768:8:1$rPyNreafXmu2M8GB$34ce9539e2bd93ede25db16fd514f4b117c789f92a3a8be1bc21077158d643595a0e8418430afe905e2cb34fb28ac0c92d52acd1b7c2cf92baada0689a3625f4','Test-7852 (Updated)','User-7852 (Updated)','+2519117855',NULL,NULL,1,NULL,'b3e205c8-9f68-4066-93b1-8fceac6c4d92','2026-07-10 13:22:53','2026-07-10 13:23:32',1,'2026-07-10 13:23:32'),('yero','yero@gmail.com','scrypt:32768:8:1$e0BxI9jnjpTx9NBG$f5da345f16fb07f2e597c795f907496508ebad76a502e994ef46fa2108b49abd466cefdccaf83f22f6a00cc6d9b97d58f97ac2a16151fffcdacbdb4eb69feccd','yeruman','guta','0919774799','keellla',NULL,1,'2026-07-13 16:52:05','db814df6-608a-494a-aedc-63a43c743fc9','2026-07-13 16:51:41','2026-07-13 16:52:05',0,NULL),('admin','admin@boutique.com','scrypt:32768:8:1$diAFefDH3pW4Sw67$9c36ed1250d15916ff0b93743343c022fa19a6dd6e434259fbb40107e3b85e46905dc75db218777eeda6efb35cc3633f8143db4b7e467b4273aa04d390a25549','System','Administrator','+1234567890',NULL,NULL,1,'2026-07-14 11:55:59','f35da230-26a8-4696-b03a-c00e184d7826','2026-07-09 08:17:27','2026-07-14 11:55:59',0,NULL);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-07-15 17:02:17
