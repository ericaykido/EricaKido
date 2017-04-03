	<?php
		$first = $_POST['first'];
		$second= $_POST['second'];
		if($_POST['group'] == 'soma') {
			echo ($first + $second);
		}
		else if($_POST['group'] == 'subt') {
			echo ($first - $second);
		}
		else if($_POST['group'] == 'vezes') {
			echo ($first * $second);
		}
		else if($_POST['group'] == 'divi') {
			echo ($first / $second);
		}
	?>
