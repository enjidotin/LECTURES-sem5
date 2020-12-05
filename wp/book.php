<?php

session_start();
$bkid = $_SESSION["BookId"];
$auth = $_SESSION["author"];
echo "Your Book Id is - $bkid and author is - $auth";
?>