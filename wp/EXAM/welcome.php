<?php
session_start();
if(isset($_SESSION["username"]))
{
  $user = $_SESSION["username"];

function OpenCon()
{
    $dbhost = "localhost";
    $dbuser = "root";
    $dbpass = "123456";
    $db = "PHPLecture";
    $conn = new mysqli($dbhost, $dbuser, $dbpass, $db);
    
    return $conn;
} 
 
function CloseCon($conn)
{
    $conn -> close();
}
 
 $conn = OpenCon();
 if($conn === false){
    die("ERROR: Could not connect." . $conn->connect_error);
    echo "<br>";
}

$sql = "SELECT visits FROM user where username='$user'";
$sqlupdate = "UPDATE user SET visits = visits+1 WHERE username='$user'";
$result = $conn->query($sql);
if($result)
{
if ($result->num_rows >0) {
    $conn->query($sqlupdate);
    $row = $result->fetch_assoc();
    echo "HELLO ". $user;
    echo "<br>";
    $viscount = $row['visits']+1;
    echo "this is your ". $viscount . " visit";
    
} else {
  echo "Not Found";
}
}
else
{
    echo "Error in ".$sql."<br>".$conn->error;
}
 
CloseCon($conn);
}
else{echo "failed";}
session_destroy();
?>