<?php
// Dummy credentials placed in HTML comments for participants to find
$dummy_user = 'user123';
$dummy_pass = 'password321';

session_start();

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['username']) && isset($_POST['password'])) {
        if ($_POST['username'] === $dummy_user && $_POST['password'] === $dummy_pass) {
            // Correct credentials; check if isAdmin cookie is set to True
            setcookie('isAdmin', 'False');
            if (isset($_COOKIE['isAdmin']) && $_COOKIE['isAdmin'] === 'True') {
                $_SESSION['flag'] = file_get_contents('flag.txt');
            } else {
                $_SESSION['error'] = 'Access denied. You are not an admin.';
            }
        } else {
            $_SESSION['error'] = 'Login failed. Invalid credentials.';
        }
        // Redirect to the result page
        header('Location: result.php');
        exit;
    }
}
?>
