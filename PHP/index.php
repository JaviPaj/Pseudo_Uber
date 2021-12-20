<?php

require_once('Account.php');
require_once('Car.php');
require_once("uberX.php");
require_once("uberPool.php");
require_once("uberBlack.php");
require_once("uberVan.php");
require_once("payment.php");
require_once("card.php");
require_once("cash.ph");
require_once("payPal.php");

$car = new Car("AWD765", new Account("Anibal Smith", "USA29"))
$car->PrintDataCar();

$uberX = new UberX("CYJ784", new Account("Anibal Smith", "USA29"), "Daewoo", "Lanus")
$uberX->PrintDataCar();

$payment = new Payment("Payment");
$payment = printDataPayment();

$card = new Card("Card", "456346539547xxx", "1124", "345")
$card = printDataPayment();


?>
