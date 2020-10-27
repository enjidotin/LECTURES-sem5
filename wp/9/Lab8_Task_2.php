<?php
session_start();

if($_POST["num"]==$_SESSION["mynum"]){
	echo "Number was guessed correctly<br>";
}
else if($_SESSION["count"]<=1){
	echo "3 attempts over. Session destroyed.<br>" . $_SESSION["mynum"] . " Was the number";
	session_destroy();
	echo "<a href='Lab8_Task_1.html'>Login</a>";
}
else{
	echo "Wrong guess. <a href='welcome.php'>Try again</a>";
}
?>