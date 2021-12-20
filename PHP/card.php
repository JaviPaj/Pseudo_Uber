<?php

require_once("payment.php");
class Card extends Payment {
    
    $this->numbercard;
    $this->enddate;
    $this->cvv;

    public function __construct($id, $numbercard, $enndate, $cvv){
        parent::__construct($id);
        $this->numbercard = $numbercard;
        $this->enddate = $enddate;
        $this->cvv = $cvv;
    }
}
?>