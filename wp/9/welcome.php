<?php
session_start();
echo "Welcome ".$_SESSION["username"];

$_SESSION["mynum"]=rand(1, 10);
// $_SESSION["mynum"]=3;
$_SESSION["count"]--;
$c=$_SESSION["count"];
echo "<h2>Number Game</h2>";
echo "You have total 3 attempts to guess the number [Between 1 & 10].<br><br>";
echo "Attempts left: $c";
echo '<form name="myGame" action="http://localhost/Lab8_Task_2.php" method="post">';
echo "Enter the number: ";
echo "<input type='number' name='num' id='num' autofocus required /><br>";
echo "<input type='submit' name='check'><br>";
echo "</form>";
?>