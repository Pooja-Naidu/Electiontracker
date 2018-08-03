<?php
header("Content-Type: application/json; charset=UTF-8");
$conn=new mysqli('localhost','root','','electiontracker');
$sql="SELECT updatedate,total from updatetable where SNo='ST-005'";
$res=$conn->query($sql);
$outp = array();
$outp = $res->fetch_all(MYSQLI_ASSOC);
echo json_encode($outp);

?>