<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db("jobs");
foreach ($_POST as $key => $value)
{
	//$sql = "INSERT INTO test_user_activity (article_id, user_name, like_flag, prediction, star_flag, share_flag, ignore_flag, action_time_stamp) values ($key, 'brad', NULL, NULL, $value, NULL, NULL, now())";
	$sql = "UPDATE test_user_activity set star_flag = $value where article_id = $key and user_name = 'brad'";
	$result = mysql_query($sql);
}
?>
