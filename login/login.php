<?php
   include("config.php");
   session_start();
   
   if($_SERVER["REQUEST_METHOD"] == "POST") {
		$username = mysqli_real_escape_string($db,$_POST['username']);
		$password = mysqli_real_escape_string($db,$_POST['password']); 
	  
		$sql = "SELECT userID FROM users WHERE name = '$username' and password = '$password'";
	  
		$r = mysqli_query($db,$sql);
		  
		if(mysqli_num_rows($r) == true) { 
			$json_str = '{"result":"1", "info": "Usuario autenticado."}';

			$obj = json_decode($json_str);

			echo "result: $obj->result<br>"; 
			echo "info: $obj->info<br>"; 
		} else {
			$json_str = '{"result":"2", "info": "Usuario ou senha incorreta."}';

			$obj = json_decode($json_str);

			echo "result: $obj->result<br>"; 
			echo "info: $obj->info<br>"; 
		}
		
		
   }
?>