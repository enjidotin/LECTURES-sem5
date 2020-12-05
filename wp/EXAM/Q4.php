<?php

if(isset($_POST["submit"])) {

    $usrVAL = $_POST["val"];

    $count1 = 65;
    $count2 = 97;

    $encryptKEY = "";

    for($i=0; $i < 26; $i++){
        $temp = rand(65, 90);
        $encryptKEY .= chr($temp);
    }

    for($i=0; $i < strlen($usrVAL); $i++){

        if(ctype_upper($usrVAL[$i])){

            $temp = ord($usrVAL[$i]);

            $temp = $temp - $count1;

            echo $encryptKEY[$temp];
        }

        else{

            $temp = ord($usrVAL[$i]);

            $temp = $temp - $count2;

            echo $encryptKEY[$temp];
        }
    }
    echo "  is the encrypted for ";
    echo $usrVAL;
}

else
    echo "Error";

?>