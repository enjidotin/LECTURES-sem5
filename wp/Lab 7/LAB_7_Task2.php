<?php

$username = trim($_POST['username']);
$password = trim($_POST['password']);
$email = trim($_POST['email']);


if(empty($username)){
    echo "Username is Empty!!";
}
else{
    echo "Username entered is: " . $username;
}

if(empty($password)){
    echo "<br>Password is Empty!!";
}
else{
    $a = preg_match("/^(?=.{8,})(?=.*[a-z])(?=.*[A-Z])(?=.*[^\w\d]).*$/",$_POST["password"]);
    if(!$a)
    {
    	echo "<br>Invalid password";
    }
    else {
    	echo "<br>Valid password";
    }
}

if(empty($email)){
    echo "<br>Email is Empty!!";
}
else{
    if(filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo("<br>Valid email address: " . $email);
    }
    else{
        echo("<br>Invalid Email");
    }
}


if(!empty($_POST['checkbox'])){
	echo "<br>Checked values: ";

	foreach($_POST['checkbox'] as $selected){
		echo $selected." ";
	}
}
else{
	echo "<br>No Checkbox Selected!!";
}

echo "<br>Radio button picked: " . $_POST['radio']

?>