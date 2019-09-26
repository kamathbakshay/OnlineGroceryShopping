
-- MySQL dump 10.13  Distrib 5.7.24, for Win64 (x86_64)
--
-- Host: localhost    Database: onlineshopping
-- ------------------------------------------------------
-- Server version	5.7.24-log

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
-- Table structure for table `administrators`
--

DROP TABLE IF EXISTS `administrators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `administrators` (
  `adminname` varchar(45) NOT NULL,
  `password` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `administrators`
--

LOCK TABLES `administrators` WRITE;
/*!40000 ALTER TABLE `administrators` DISABLE KEYS */;
INSERT INTO `administrators` VALUES ('aashish','eigenvalue'),('akshay','guywithamanbun'),('rahul','rahul123'),('a','a');
/*!40000 ALTER TABLE `administrators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cart`
--

DROP TABLE IF EXISTS `cart`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cart` (
  `cid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `quantity` varchar(45) NOT NULL,
  `amount` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cart`
--

LOCK TABLES `cart` WRITE;
/*!40000 ALTER TABLE `cart` DISABLE KEYS */;
INSERT INTO `cart` VALUES (812,9,'2',54),(816,11,'2',96),(816,14,'3',195),(817,11,'2',96),(817,12,'1',140),(817,14,'2',130),(817,9,'10',270),(817,13,'12',576),(819,15,'2',62),(819,9,'13',351);
/*!40000 ALTER TABLE `cart` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `category`
--

DROP TABLE IF EXISTS `category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `category` (
  `catid` int(11) NOT NULL AUTO_INCREMENT,
  `categoryname` varchar(45) NOT NULL,
  PRIMARY KEY (`catid`)
) ENGINE=InnoDB AUTO_INCREMENT=68 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `category`
--

LOCK TABLES `category` WRITE;
/*!40000 ALTER TABLE `category` DISABLE KEYS */;
INSERT INTO `category` VALUES (57,'dairyproducts'),(58,'vegetables'),(63,'beverages'),(67,'Frozen Products');
/*!40000 ALTER TABLE `category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `cid` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(45) NOT NULL,
  `email` varchar(45) NOT NULL,
  `phone` varchar(45) NOT NULL,
  `password` varchar(500) NOT NULL,
  PRIMARY KEY (`cid`)
) ENGINE=InnoDB AUTO_INCREMENT=823 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (817,'amruth','amruth@gmail.com','9339339383','$5$rounds=535000$5t7Sgj5QYFwY1nbB$beIhs8EK35eFu761R/kKU01Uo21XT4507zOP05Lj/O0'),(819,'akshay','kamathbakshay@gmail.com','8277251970','$5$rounds=535000$8X.5oTdVCBKr.s3B$GEtkBcPhWLiL8JUo1GZ6bIXU1MzrB0f349GBa2hfzj.'),(820,'aashish','aashishMukund@gmail.com','9449339393','$5$rounds=535000$x.DbpTh0lwwx7jAq$p49OX8PAQB6zcHT7EyD/qqjjIHiFDs8JVaIZAy83nP7'),(822,'b','test@gmail.com','8277251970','$5$rounds=535000$5aWYw2RKjcLVzbel$oVjQo6kWUDmdjZqXozfjXT62MMYxvH41Z0BoQusYMQ9');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `livedelivery`
--

DROP TABLE IF EXISTS `livedelivery`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `livedelivery` (
  `oid` int(11) NOT NULL,
  `sid` int(11) NOT NULL,
  `deliveryboyname` varchar(45) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `deliveryboyphoneno` int(11) DEFAULT NULL,
  `totalamount` float DEFAULT NULL,
  `status` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `livedelivery`
--

LOCK TABLES `livedelivery` WRITE;
/*!40000 ALTER TABLE `livedelivery` DISABLE KEYS */;
/*!40000 ALTER TABLE `livedelivery` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `cid` int(11) NOT NULL,
  `oid` int(11) NOT NULL AUTO_INCREMENT,
  `productidlist` varchar(1000) NOT NULL,
  `quantitylist` varchar(1000) NOT NULL,
  `orderdate` date NOT NULL,
  `deleveryTime` varchar(45) NOT NULL,
  PRIMARY KEY (`oid`)
) ENGINE=InnoDB AUTO_INCREMENT=184 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (812,172,'[9]','[\'2\']','2018-11-30','Morning(7-12)'),(816,173,'[11, 14]','[\'2\', \'3\']','2018-11-30','Afternoon(1-4)'),(816,174,'[11, 14]','[\'2\', \'3\']','2018-11-30','Morning(7-12)'),(814,175,'[10]','[\'3\']','2018-11-30','Evening(4-7)'),(817,176,'[11, 10]','[\'2\', \'20\']','2018-12-04','Morning(7-12)'),(817,177,'[11, 12, 14]','[\'2\', \'1\', \'2\']','2018-12-04','Morning(7-12)'),(817,178,'[11, 12, 14, 9, 13]','[\'2\', \'1\', \'2\', \'10\', \'12\']','2018-12-04','Morning(7-12)'),(817,179,'[11, 12, 14, 9, 13]','[\'2\', \'1\', \'2\', \'10\', \'12\']','2018-12-04','Morning(7-12)'),(817,180,'[11, 12, 14, 9, 13]','[\'2\', \'1\', \'2\', \'10\', \'12\']','2018-12-04','Morning(7-12)'),(817,181,'[11, 12, 14, 9, 13]','[\'2\', \'1\', \'2\', \'10\', \'12\']','2018-12-04','Morning(7-12)'),(817,182,'[11, 12, 14, 9, 13]','[\'2\', \'1\', \'2\', \'10\', \'12\']','2018-12-04','Morning(7-12)'),(819,183,'[15, 9]','[\'2\', \'13\']','2018-12-06','Evening(4-7)');
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pendingorder`
--

DROP TABLE IF EXISTS `pendingorder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pendingorder` (
  `cid` int(11) NOT NULL,
  `pidlist` varchar(100) NOT NULL,
  `quantitylist` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pendingorder`
--

LOCK TABLES `pendingorder` WRITE;
/*!40000 ALTER TABLE `pendingorder` DISABLE KEYS */;
INSERT INTO `pendingorder` VALUES (1,'23','3'),(812,'[2, 5, 4]','[\'5\', \'1\', \'3\']'),(812,'[2, 5, 4]','[\'5\', \'1\', \'3\']'),(812,'[2, 5, 4, 4, 5, 2]','[\'5\', \'1\', \'3\', \'1\', \'4\', \'1\']'),(812,'[]','[]'),(812,'[]','[]'),(812,'[]','[]'),(812,'[2]','[\'1\']'),(813,'[5]','[\'12\']'),(812,'[4]','[\'23\']'),(812,'[4, 4, 4]','[\'23\', \'1\', \'1\']'),(812,'[3, 4, 4, 4, 4]','[\'2\', \'23\', \'1\', \'1\', \'1\']'),(812,'[5]','[\'2\']'),(812,'[]','[]'),(812,'[]','[]'),(812,'[9]','[\'3\']'),(812,'[9]','[\'3\']'),(812,'[9]','[\'3\']'),(812,'[]','[]'),(812,'[]','[]'),(812,'[]','[]'),(812,'[9]','[\'3\']'),(812,'[]','[]'),(812,'[]','[]'),(812,'[]','[]'),(812,'[9]','[\'3\']'),(812,'[9]','[\'3\']'),(812,'[5, 9]','[\'2\', \'3\']'),(812,'[5, 9]','[\'2\', \'3\']'),(812,'[5, 9]','[\'2\', \'3\']'),(812,'[5, 9]','[\'2\', \'3\']'),(812,'[]','[]'),(812,'[]','[]'),(812,'[3]','[\'10\']'),(812,'[]','[]'),(812,'[3]','[\'10\']'),(812,'[3]','[\'10\']'),(812,'[9, 3]','[\'3\', \'10\']'),(812,'[]','[]'),(812,'[]','[]'),(812,'[3]','[\'10\']'),(812,'[3]','[\'10\']'),(812,'[3]','[\'10\']'),(812,'[3]','[\'10\']'),(812,'[9, 3]','[\'3\', \'10\']'),(812,'[9, 3]','[\'3\', \'10\']'),(812,'[9, 3]','[\'3\', \'10\']'),(812,'[9, 3]','[\'3\', \'10\']'),(812,'[9, 3]','[\'3\', \'10\']'),(812,'[5, 9, 3]','[\'2\', \'3\', \'10\']'),(812,'[]','[]'),(812,'[]','[]'),(812,'[3]','[\'1\']'),(812,'[4]','[\'2\']'),(812,'[3, 4]','[\'1\', \'2\']'),(812,'[]','[]'),(812,'[3]','[\'1\']'),(812,'[4]','[\'2\']'),(812,'[]','[]'),(816,'[]','[]'),(816,'[11]','[\'2\']'),(814,'[]','[]'),(817,'[11, 10]','[\'2\', \'20\']'),(817,'[11]','[\'2\']'),(817,'[11]','[\'2\']'),(817,'[]','[]'),(817,'[]','[]'),(817,'[]','[]'),(819,'[]','[]');
/*!40000 ALTER TABLE `pendingorder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phistory`
--

DROP TABLE IF EXISTS `phistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phistory` (
  `pid` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phistory`
--

LOCK TABLES `phistory` WRITE;
/*!40000 ALTER TABLE `phistory` DISABLE KEYS */;
INSERT INTO `phistory` VALUES (11,2),(12,1),(14,2),(9,10),(13,12),(11,2),(12,1),(14,2),(9,10),(13,12),(15,2),(9,13);
/*!40000 ALTER TABLE `phistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `catid` int(11) DEFAULT NULL,
  `priceperunit` float DEFAULT NULL,
  `pname` varchar(45) NOT NULL,
  `stockleft` int(11) DEFAULT '0',
  `productdesc` varchar(200) DEFAULT NULL,
  `imagesrc` longtext,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (3,57,98,'curd',10,'Milky Mist Natural Set Curd, 1 kg Cup','https://www.bigbasket.com/media/uploads/p/l/40003156_3-milky-mist-natural-set-curd.jpg'),(4,58,26,'potato',10,'Grown through organic methods, this variety is best for french fries','https://4.imimg.com/data4/AY/BI/ANDROID-23561387/product-500x500.jpeg'),(5,58,23,'carrot',130,'Freshly grown carrots, this is the favourite food of Bugs Bunny','http://befreshcorp.net/wp-content/uploads/2017/06/product-packshot-Carrot-558x600.jpg'),(9,58,27,'Tomato',67,'Fresho Tomato - Hybrid, Organically Grown, 1 kg ','https://www.bigbasket.com/media/uploads/p/l/50000557_5-fresho-tomato-hybrid-organically-grown.jpg'),(10,57,24,'SKIMMED MILK',100,'Nandini GoodLife Skimmed Milk, 500 ml Pouch','https://www.bigbasket.com/media/uploads/p/l/242673_4-nandini-goodlife-skimmed-milk.jpg'),(11,57,48,'Amul Buttery',94,'Amul Buttery Spread - Garlic & Herbs, 100 gm Carton','https://www.bigbasket.com/media/uploads/p/l/40018687_1-amul-buttery-spread-garlic-herbs.jpg'),(12,57,140,'Cheese',25,'Britannia Pizza Block, 200 gm Carton','https://www.bigbasket.com/media/uploads/p/l/124871_6-britannia-pizza-block.jpg'),(13,58,48,'Chilli',52,'Fresho Chilli - Green Long, Medium, 1 kg ','https://www.bigbasket.com/media/uploads/p/l/10000333_14-fresho-chilli-green-long-medium.jpg'),(14,58,65,'Mushroom',0,'Fresho Mushrooms - Button, 200 gm ','https://www.bigbasket.com/media/uploads/p/l/10000273_13-fresho-mushrooms-button.jpg'),(15,63,31,'Coca Cola',8,'Coca Cola Soft Drink, 300 ml Can','https://www.bigbasket.com/media/uploads/p/l/100401160_3-coca-cola-soft-drink.jpg'),(16,63,30,'Mirinda',100,'Mirinda Soft Drink - Orange Flavour, Mini Can, 150 ml','https://images.all-free-download.com/images/graphiclarge/mirinda_can_6827261.jpg'),(17,63,32,'Thums up',100,'Thums Up Charged, 300 ml ','https://4.imimg.com/data4/TO/HM/MY-1850306/thums-up-500x500.jpg'),(18,63,20,'7 up',100,'7 Up Soft Drink, 150 ml ','https://images-cdn.azureedge.net/azure/lulu-resources/947f11bb-f157-4c65-b7fb-df009c3c9ec9/Images/ProductImages/Source/8210-01.jpg'),(19,63,30,'Pepsi',100,'Pepsi Soft Drink, 250ml MultiPack','https://www.bigbasket.com/media/uploads/p/l/263333_8-pepsi-soft-drink-diet.jpg');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supplier` (
  `sid` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1111,'wilson supers','kormangala');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-15 11:20:07
