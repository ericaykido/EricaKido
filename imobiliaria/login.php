<?php
   include("config.php");
   
   if($_SERVER["REQUEST_METHOD"] == "POST") {
		$username = mysqli_real_escape_string($db,$_POST['name']);
		$password = mysqli_real_escape_string($db,$_POST['password']);
	  
		$sql = "SELECT userID FROM users WHERE name = '$username' and password = '$password'";
	  
		$r = mysqli_query($db,$sql);
		  
		if(mysqli_num_rows($r) == true) {
			session_start();
			$_SESSION['login_name'] = $username;
			$_SESSION['login_password'] = $password;
			
			$typeUser = "SELECT typeUser FROM users WHERE name = '$username' AND password = '$password'";
			
			$r = mysqli_query($db,$typeUser)->fetch_array(MYSQLI_ASSOC);

			switch($r['typeUser']){
				case "1":
					header("Location: http://localhost/imobiliaria/inquilino.php");
					$data = array('username'=>$username, 'typeUser'=>$r['typeUser']);
					echo json_encode($data);
					exit;
				case "2":
					header("Location: http://localhost/imobiliaria/imovel.php");
					$data = array('username'=>$username, 'typeUser'=>$r['typeUser']);
					echo json_encode($data);
					exit;
				case "3":
					header("Location: http://localhost/imobiliaria/proprietario.php");
					$data = array('username'=>$username, 'typeUser'=>$r['typeUser']);
					echo json_encode($data);
					exit;
			}
		} else {
			session_destroy();

			unset($_SESSION['name']);
			unset($_SESSION['password']);

			header("location:login.html");
		}
		msqli_close();
   }
?>