<?php
class Payment{
    public $id;

    public function __comstruct(id){
        $this->id = $id;
    }

    public function printDataPayment(){
        echo "ID Payment: ".$this->id."<br>";
    }
}

?>