<?php
$m=new MongoClient();
$db=$m->krish2;
$collection=$db->details;

$collection->remove(array('country'=>'India'));
echo"Remove Successfully";

$cur=$collection->find();

foreach($cur as $document){
echo"<br>".$document['name']."<br>";

}








?>