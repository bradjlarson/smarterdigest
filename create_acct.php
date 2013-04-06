<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db('jobs');
$username = $_POST['create_user_name'];
$pwd = $_POST['create_password'];
$email = $_POST['create_email'];


$sql = "SELECT max(id) as starting_id from test_unique";
$result = mysql_query($sql);
$starting_id = -29;
while($row = mysql_fetch_array($result))
{
	$starting_id = $starting_id + $row['starting_id'];
}
$sql = "SELECT count(id) as existing from test_user where user_name ='$username'";
$result = mysql_query($sql);
$existing = 0;
session_start();
$_SESSION['username'] = $username;
$_SESSION['pwd'] = $pwd;
$sesh_id = session_id();
while($row = mysql_fetch_array($result))
{	
	$existing = $existing + $row['existing'];
}	
if ($existing == 0)
{
	$sql = "INSERT into test_user (user_email, user_name, starting_id) values ('$email', '$username', '$starting_id')";
	$exec = mysql_query($sql);
	$sql = "INSERT into test_user_access (user_name, access_type, access_time_stamp, session_id) values ('$username', 'create_acct', now(), '$sesh_id')";
	$exec = mysql_query($sql);
	$sql = "INSERT into test_user_activity (article_id, user_name, like_flag, prediction, star_flag, share_flag, ignore_flag, action_time_stamp) SELECT id, '$username', NULL, NULL, NULL, NULL, NULL, now() from test_unique where id >= $starting_id";
	$exec = mysql_query($sql);

$file = '/Dropbox/Coding/smarterdigest/create_acct.sh';
$fh = fopen($file, 'w') or die("cannot open create_acct.sh");
$text = '#!/bin/ksh
username="'.$username.'"
password="'.$pwd.'"

mkdir /Dropbox/Coding/smarterdigest/users/$username
cp /Dropbox/Coding/smarterdigest/default/index.php /Dropbox/Coding/smarterdigest/users/$username/index_1.php
cp /Dropbox/Coding/smarterdigest/default/stars_test.php /Dropbox/Coding/smarterdigest/users/$username/stars_test_1.php
cp /Dropbox/Coding/smarterdigest/default/top_bar.php /Dropbox/Coding/smarterdigest/users/$username/top_bar_1.php
cp /Dropbox/Coding/smarterdigest/default/votes_test.php /Dropbox/Coding/smarterdigest/users/$username/votes_test_1.php
cp /Dropbox/Coding/smarterdigest/default/share_test.php /Dropbox/Coding/smarterdigest/users/$username/share_test_1.php
cp /Dropbox/Coding/smarterdigest/default/submit_suggestion.php /Dropbox/Coding/smarterdigest/users/$username/submit_suggestion_1.php
cp /Dropbox/Coding/smarterdigest/default/acct_mgmt.php /Dropbox/Coding/smarterdigest/users/$username/acct_mgmt_1.php
cp /Dropbox/Coding/smarterdigest/default/last_thirty.php /Dropbox/Coding/smarterdigest/users/$username/last_thirty_1.php
cp /Dropbox/Coding/smarterdigest/default/logout.php /Dropbox/Coding/smarterdigest/users/$username/logout_1.php
cp /Dropbox/Coding/smarterdigest/default/queue.php /Dropbox/Coding/smarterdigest/users/$username/queue_1.php
cp /Dropbox/Coding/smarterdigest/default/show_starred.php /Dropbox/Coding/smarterdigest/users/$username/show_starred_1.php
cp /Dropbox/Coding/smarterdigest/default/top_bar_thirty.php /Dropbox/Coding/smarterdigest/users/$username/top_bar_thirty_1.php
cp /Dropbox/Coding/smarterdigest/default/get_predictions.php /Dropbox/Coding/smarterdigest/users/$username/'.$username.'_predictions_1.php
cd /Dropbox/Coding/smarterdigest/users/$username
cp index_1.php index_2.php

sed -e \'s/$username/'.$username.'/g\' index_2.php > index_1.php
sed -e \'s/$password/'.$pwd.'/g\' index_1.php > index.php
sed -e \'s/$username/'.$username.'/g\' stars_test_1.php > stars_test.php
sed -e \'s/$username/'.$username.'/g\' top_bar_1.php > top_bar.php
sed -e \'s/$username/'.$username.'/g\' votes_test_1.php > votes_test.php
sed -e \'s/$username/'.$username.'/g\' share_test_1.php > share_test.php
sed -e \'s/$username/'.$username.'/g\' submit_suggestion_1.php > submit_suggestion.php
sed -e \'s/$username/'.$username.'/g\' acct_mgmt_1.php > acct_mgmt.php
sed -e \'s/$username/'.$username.'/g\' last_thirty_1.php > last_thirty.php
sed -e \'s/$username/'.$username.'/g\' logout_1.php > logout.php
sed -e \'s/$username/'.$username.'/g\' queue_1.php > queue.php
sed -e \'s/$username/'.$username.'/g\' show_starred_1.php > show_starred.php
sed -e \'s/$username/'.$username.'/g\' top_bar_thirty_1.php > top_bar_thirty.php
sed -e \'s/$username/'.$username.'/g\' '.$username.'_predictions_1.php > '.$username.'_predictions.php

mv '.$username.'_predictions.php /Dropbox/Coding/smarterdigest/engine/users/

rm *_1.php
rm *_2.php
chmod a+rwx -R /Dropbox/Coding/smarterdigest/users/$username/.' . PHP_EOL;

fwrite($fh, $text);
fclose($fh);
$command = "/Dropbox/Coding/smarterdigest/./create_acct.sh";
$create_user = system($command);

$redirectURL = "http://smarterdigest.com/users/$username/";
header("Location: ".$redirectURL);

}
else
{
echo '<h3>Warning: That username is already taken. Please choose a different username and try again</h3>' . PHP_EOL;
include('index.php');
}
?>
