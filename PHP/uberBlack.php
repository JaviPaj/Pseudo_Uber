<?php

require_once("car.php");
class UberBlack extends Car {
    public $typecaraccepted;
    public $seatsmaterial;

    public function __construct($license, $driver, $typecaraccepted, $seatsmaterial){
        parent:: __construct($license, $driver);
        $this->typecaraccepted = $typecaraccepted;
        $this->seatmateria = $seatsmaterial
    }
}

?>
