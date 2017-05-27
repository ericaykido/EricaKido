<?php
	include ('session.php');
?>

<html>
	<head>
		<title>IMOVEL</title>
		
	</head>
	<body>
		<div align = "center">
            <div><b>Home</b></div>
			<div>
				<label><?php echo $user_check; ?></label></br> 
				<label>Bem-vindo à sua página!</label></br> 
				<b id="logout"><a href="logout.php">Log Out</a></b>
			</div>
		</div>
	</body>
</html>