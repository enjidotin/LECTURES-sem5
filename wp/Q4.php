<?php

if(isset($_POST["submit"])) {

    $strUser = $_POST["strUser"];

    $count1 = 65;
    $count2 = 97;

    $key_latin = "NBAJYFOWLZMPXIKUVCDEGRQSTH";

    for($i=0; $i<strlen($strUser); $i++){

        if(ctype_upper($strUser[$i])){

            $temp = ord($strUser[$i]);

            $temp = $temp - $count1;

            echo $key_latin[$temp];
        }

        else{

            $temp = ord($strUser[$i]);

            $temp = $temp - $count2;

            echo $key_latin[$temp];
        }
    }
}

else
    echo "Error please try again";

?>