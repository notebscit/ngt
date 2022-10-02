<?php
$m=new MongoCLient();
$db=$m->krish2;
$collection=$db->details;

$cur=$collection->find();

foreach($cur as $document){
echo $document["name"]." ".$document["lname"]." ".$document["age"]." ".$document["country"]."<br>";
}
?>