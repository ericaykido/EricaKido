<?php
	session_start();
	
	$user_check=$_SESSION['login_name'];

	if(!isset($user_check))
	{	
		$out = array('user_check'=>' ');
		header('Location: ../home/home.html');
	}
	else
	{
		$out = array('user_check'=>$user_check);
	}
	json_encode($out);
?>