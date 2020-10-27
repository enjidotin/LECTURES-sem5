<?php

$number = $_POST['num'];

echo "Fibonacci series for first $number numbers: ";
for ($counter = 0; $counter < $number; $counter++){
    echo Fibonacci($counter),' ';
}
echo "<br>";

$flag = Armstrong($number);
if ($flag == 1)
    echo "Yes, $number is an Armstrong number <br>";
else
    echo "No, $number is not an Armstrong number <br>";


$fact = Factorial($number);
echo "Factorial for $number is $fact ";


function Fibonacci($number){
    if ($number == 0)
        return 0;
    else if ($number == 1)
        return 1;
    else
        return (Fibonacci($number-1) +
                Fibonacci($number-2));
}

function Armstrong($number){
    $sum = 0;
    $x = $number;
    while($x != 0)
    {
        $rem = $x % 10;
        $sum = $sum + $rem * $rem * $rem;
        $x = $x / 10;
    }
    if ($number == $sum)
        return 1;
    return 0;
}

function Factorial($number){
    $factorial = 1;
    for ($i = 1; $i <= $number; $i++){
      $factorial = $factorial * $i;
    }
    return $factorial;
}


?>