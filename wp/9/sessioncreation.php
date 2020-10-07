<?php
$myname= "xyz";
$mypass="hello";


if(isset($_POST["login"]))
{
$a=$_POST["username"];
$b=$_POST["password"];
if($myname==$a and $mypass==$b )
{
if(isset($_POST["Rememberme"]))
{
$cookie_exp = time()+60*60*24*30;
setcookie("username", $a, $cookie_exp);
}
session_start();
$_SESSION["username"]=$a;
header("location:welcome.php");
}
else
{
echo "Entered wrong username or password.. Try again";
echo "<a href='login.html'>ttt<>";
}
}
else
{
header("location:login.html");
}

?>