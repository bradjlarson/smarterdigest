<?php
$sesh_id = session_id();
$sql = "INSERT into test_user_access (user_name, access_type, access_time_stamp, session_id) VALUES ('brad', 'logout', now(), '$sesh_id')";
$exec = mysql_query($sql);
session_regenerate_id(FALSE);
session_unset();
$redirectURL = "http://smarterdigest.com/";
header("Location: ".$redirectURL);
?>