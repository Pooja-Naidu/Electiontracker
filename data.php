
<?php
header("Content-Type: application/json; charset=UTF-8");
$conn=new mysqli('localhost','root','','electiontracker');
if($conn->connect_error){
    die("Connection failed:".$conn->connect_error);
}
$sql="SELECT updatedate,total from updatetable where SNo='ST-001'";
$res=$conn->query($sql);
$outp = array();
if ( $res->num_rows > 0){
 $outp = $res->fetch_all(MYSQLI_ASSOC);
echo json_encode($outp);
//while ($row = $res->fetch_assoc()) {
    //echo "SNo:".$row["updatedate"]."Status:".$row["total"]."<br>";
//}
}
else {
    echo "0 results";
}
$conn->close();

?>