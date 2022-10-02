<?php
$m=new MongoClient();
$db=$m->krish2;
$collection=$db->details;


$collection->update(array('name'=>'Krishna'),array('$set'=>array('name'=>'KRSNAVc')));
echo"Updated Successfully";

$cur=$collection->find();
foreach ($cur as $document)
{
echo "<br>".$document['name']."<br>";
}

?>