<?php
	include('../session/session.php');

	include("../config/config.php");

	$sql = "UPDATE inquilino SET boleto = true where name='$user_check' ";
	  
	$r = mysqli_query($db, $sql);

	if(mysqli_num_rows($r) == true) {
		echo "TRUE";
	}
?>
