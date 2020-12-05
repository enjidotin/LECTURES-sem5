<?php

if(isset($_POST["submit"])) {

    $val = $_POST["val"];

    $ctr1 = 65;
    $ctr2 = 97;

    $plain = "";

    for($i=0; $i < 26; $i++){
        $temp = rand(65, 90);
        $plain .= chr($temp);
    }

    for($i=0; $i < strlen($val); $i++){

        if(ctype_upper($val[$i])){

            $temp = ord($val[$i]);

            $temp = $temp - $ctr1;

            echo $plain[$temp];
        }

        else{

            $temp = ord($val[$i]);

            $temp = $temp - $ctr2;

            echo $plain[$temp];
        }
    }
}

else
    echo "Error";

?>