<?php
	include("config.php");

	$idImovel = file_get_contents('php://input');
	$idImovel = trim($idImovel);
	$id = 1;

	$sql = "SELECT * FROM imovel WHERE idImovel = '$id'";
	  
	$r = mysqli_query($db, $sql)->fetch_array(MYSQLI_ASSOC);

	if(mysqli_num_rows($r) == true) {
		session_start();
		
		for ($i=0; $i < sizeof($r); $i++) { 
			echo $r[1];
		}
	}
?>