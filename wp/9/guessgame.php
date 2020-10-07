<?php
session_start();
if (!isset($_SESSION["guesscount"])){
$_SESSION["guesscount"] = 0;}

if($_SESSION["guesscount"]==0){
	$_SESSION["guess"] = rand(1,10);
}
if(isset($_POST['submit'])) {

		$cookie_exp = time() + 60*60*24*60;
		setcookie("guess", $_SESSION["guess"], $cookie_exp);
		
		if($_SESSION["guesscount"] == 3){
			echo "no tries remaining";
			session_destroy();
		}
		else{
		$_SESSION["guesscount"] += 1;
		if ($_POST["number"] == $_SESSION["guess"]){
			echo "correct!";
			session_destroy();
		}

		else{echo "incorrect!";
			
		}
		}
		

		echo "<a href = 'guessgame.html'>back</a>";
}

?>