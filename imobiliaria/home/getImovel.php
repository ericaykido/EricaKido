<?php
	include("../config/config.php");

	$idImovel = file_get_contents('php://input');
	$idImovel = trim($idImovel);

	$sql = "SELECT * FROM imovel WHERE idImovel = '$id'";
	  
	$r = mysqli_query($db, $sql)->fetch_array(MYSQLI_ASSOC);

	if(mysqli_num_rows($r) == true) {
		$out = array('caracteristicas'=>$r['caracteristicas'],'image'=>$r['image'], 'idUserInquilino'=>$r['idUserInquilino']);
		json_encode($out);
	}
?>