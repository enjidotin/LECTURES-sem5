<?php
$myname="myname";
$mypass="mypass";
if(isset($_POST["login"]))
{
 	$user=$_POST["username"];
 	$pass=$_POST["password"];
	if($myname==$user and $mypass==$pass)
	{
 		if(isset($_POST["rememberme"]))
		{
			$cookie_exp = time()+60*60*24*30;
			setcookie("username", $user, $cookie_exp);
		}
		session_start();
		$_SESSION["username"]=$user;
		$_SESSION["count"]=4;
		header("location:welcome.php");
	}
	else
	{
		echo "INVALID CREDENTIALS<br>";
		echo "<a href='Lab8_Task_1.html'>Login</a>";
	}
}
else
{
	header("location:Lab8_Task_1.html");
}
?>