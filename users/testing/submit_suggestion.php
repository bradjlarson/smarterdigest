<?php
session_start();
$sesh_id = session_id();
include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db('jobs');
$suggestion = $_POST['suggestion_box'];
$suggestion = urlencode($suggestion);
$sql = "INSERT into test_user_suggest (user_name, suggestion_text, session_id, suggestion_time_stamp) VALUES ('testing', '$suggestion', '$sesh_id', now())";
if (!mysql_query($sql))
{
	die('error: ' . mysql_error());
}
?>