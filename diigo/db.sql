/*
SQLyog Community Edition- MySQL GUI v7.01 
MySQL - 5.0.27-community-nt : Database - peertopeerride
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

CREATE DATABASE /*!32312 IF NOT EXISTS*/`peertopeerride` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `peertopeerride`;

/*Table structure for table `currentlocationider` */

DROP TABLE IF EXISTS `currentlocationider`;

CREATE TABLE `currentlocationider` (
  `id` int(50) NOT NULL auto_increment,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `markerimage` varchar(50) NOT NULL,
  `riderlatitude` double default NULL,
  `riderlongitude` double default NULL,
  `dname` varchar(50) default NULL,
  `rname` varchar(50) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `currentlocationider` */

insert  into `currentlocationider`(`id`,`latitude`,`longitude`,`markerimage`,`riderlatitude`,`riderlongitude`,`dname`,`rname`) values (1,19.0728,72.8826,'static/icons/cloudysunny.png',19.4553059,72.811816,'yash','r'),(2,19.0728,72.8826,'static/icons/cloudysunny.png',19.4553059,72.811816,'m','r'),(3,19.0728,72.8826,'static/icons/cloudysunny.png',19.4553059,72.811816,'d','r');

/*Table structure for table `location` */

DROP TABLE IF EXISTS `location`;

CREATE TABLE `location` (
  `id` int(50) NOT NULL auto_increment,
  `location_name` varchar(50) default '',
  `location_address` varchar(50) default NULL,
  `latitude` double default NULL,
  `longitude` double default NULL,
  `drivername` varchar(50) default NULL,
  `images` varchar(50) default NULL,
  `narker` varchar(50) default NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `location` */

insert  into `location`(`id`,`location_name`,`location_address`,`latitude`,`longitude`,`drivername`,`images`,`narker`) values (1,'Andheri','Military Rd, Raje Shivaji Nagar, Marol, Andheri Ea',19.113646,72.869736,'d','static/images/a.jpg','static/icons/cloudysunny.png'),(2,'Borivli','Ganesh Nagar, Tata Power House, Off Western Expres',19.23378,72.856941,'a','static/images/b.jpg','static/icons/cloudysunny.png'),(3,'juhu','Filmcity House, Raut Road, Juhu, Mumbai, Maharasht',-2.68751,115.640671,'yash','static/images/b.jpg','static/icons/cloudysunny.png'),(4,'Nalasopara','Gorai Pada, Mahan, Nalasopara East, Bilalpada, Mah',19.419863,72.811661,'n','static/images/a.jpg','static/icons/cloudysunny.png'),(5,'vikhroli','Vikhroli Park Site Uppar Depo Pada Sagar Nagar Ved',19.091183,72.92086,'m','static/images/a.jpg','static/icons/cloudysunny.png');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
