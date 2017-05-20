<?php
	session_start();
	
	$user_check=$_SESSION['login_name'];

	if(!isset($user_check))
	{	
		$out = array('nome'=>' ');
		header('Location: home.html');
	}
	else
	{
		$out = array('nome'=>$nome);
	}
	echo json_encode($out);
?>