<?php
if(isset($_POST['submit'])) {
  $user = $_POST["username"];
  $pass = $_POST["password"];
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
$sqlauth = "SELECT password FROM user where username='$user'";
$result = $conn->query($sqlauth);
if($result)
{
if ($result->num_rows >0) {
    $row = $result->fetch_assoc();
    if ($row['password'] == $pass){
    session_start();
    $_SESSION["username"] = $user;
    header('location:welcome.php');
    }
    else{
        echo "invalid password";
    }
} else {
  echo "USER NOT FOUND";
}
}
else
{
    echo "ERROR".$sqlauth."<br><br><br>".$conn->error;
}
 
CloseCon($conn);
}
else{echo "failed";}

?>