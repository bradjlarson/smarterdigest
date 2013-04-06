<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db('jobs');
$username = $_POST['login_user_name'];
$pwd = $_POST['login_password'];

session_start();
$sesh_id = session_id();

$_SESSION['username'] = $username;
$_SESSION['pwd'] = $pwd;

$sql = "INSERT into test_user_access (user_name, access_type, access_time_stamp, session_id) values ('$username', 'Login Attempt', now(), '$sesh_id')";
$exec = mysql_query($sql);

$redirecturl = "http://smarterdigest.com/users/$username/index.php";
header("Location: ".$redirecturl);

?>
