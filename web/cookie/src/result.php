<?php
session_start();
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Result</title>
    <style>
        /* Your CSS styles here */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .result-container {
            text-align: center;
        }
    </style>
</head>
<body>
<body>
    <div class="result-container">
        <?php
		if (isset($_COOKIE['isAdmin']) && $_COOKIE['isAdmin'] === 'True') {
		$flag = file_get_contents('flag.txt');


		echo '<p style="color: green;">Welcome Admin. Here is the flag - '. $flag .'</p>';

		}
            	elseif (isset($_COOKIE['isAdmin']) && $_COOKIE['isAdmin'] === 'False') {
                echo '<p style="color: green;"> Welcome User. Only Admin can see the flag. </p>';
            } else {
                echo '<p style="color: red;">No access or invalid credentials.</p>';
            }
        ?>
        <a href="index.html">Go back to login</a>
    </div>
</body>
</body>
</html>
