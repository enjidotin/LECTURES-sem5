<?php
if(isset($_POST['submit'])) {
    $user =$_POST['username'];
    $BId = $_POST['bookid'] ;

    $conn = new mysqli("localhost", "root", "1234", "q5db");
    if (!$conn) {
		die("Error connecting to database: " . mysqli_connect_error());
	}
    $sql1 = "SELECT * FROM lib where username='$user' ";  
	$result = $conn->query($sql1);
	if ($result->num_rows> 0) {
	    while($row = $result->fetch_assoc()) {
		    if($row["bookid"]==$BId){
                session_start();
                $_SESSION["BookId"]=$BId;
                $_SESSION["author"]=$row["username"];
			    header("location:book.php");
		    }
		    else{
		    	echo "Invalid Book Id!!";
		    }
          }
        }
    }
?>