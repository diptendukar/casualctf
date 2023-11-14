<?php
$message = '';
if (isset($_POST['ip'])) {
    $ip = $_POST['ip'];
    // The following line is vulnerable to command injection
    $output = shell_exec("ping -c 4 " . $ip);
    $message = nl2br(htmlspecialchars($output));
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ping Service</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            flex-direction: column;
        }
        .container {
            background-color: white;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            padding: 20px;
            border-radius: 8px;
        }
        h2 {
            color: #333;
        }
        form {
            margin-bottom: 20px;
        }
        input[type="text"] {
            padding: 10px;
            margin-right: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
            width: 200px;
        }
        input[type="submit"] {
            padding: 10px 20px;
            background-color: #5cb85c;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        input[type="submit"]:hover {
            background-color: #4cae4c;
        }
        pre {
            background-color: #222;
            color: #5cb85c;
            padding: 20px;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Ping Service</h2>
        <form method="post">
            IP Address: <input type="text" name="ip" required><br>
            <input type="submit" value="Ping">
        </form>
        <?php if ($message): ?>
            <pre><?php echo $message; ?></pre>
        <?php endif; ?>
    </div>
</body>
</html>
