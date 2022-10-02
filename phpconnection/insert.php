<?php

$m=new MongoCLient();
//echo"Connected Successfully \n";

$db=$m->krish2;
//echo"Db created Successfully \n";

$collection=$db->details;
//echo"Collection created Successfully\n";

$document=array(
"name"=>"Divesh",
"lname"=>"Chauhan",
"age"=>21,
"country"=>"India"
);


$collection->insert($document);
echo"Inserted Successfully";


?>

