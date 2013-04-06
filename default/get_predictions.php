<?php
$start_time = date('Y-m-d H:i:s');
include('/Dropbox/Coding/ShopSimply/db_connect.php');
require_once '/Dropbox/Coding/classifier-php/bayes.php';
mysql_select_db('jobs');
$sql = "SELECT max(article_id) as last_inserted from test_user_activity where user_name = '$username'";
$result = mysql_query($sql);
$last_inserted = 0;
while($row = mysql_fetch_array($result))
{
	$last_inserted = $last_inserted + $row["last_inserted"];
}
$sql = "INSERT into test_user_activity (article_id, user_name, like_flag, prediction, star_flag, share_flag, ignore_flag, action_time_stamp) SELECT id, '$username', NULL, NULL, NULL, NULL, NULL, now() from test_unique where id > $last_inserted";
$exec = mysql_query($sql);

$sql = "SELECT case when last_like = last_action then 1 when num_no_prediction > 0 then 1 else 0 end as engine_check from
(select max(action_time_stamp) as last_like from test_user_activity where user_name = '$username' and like_flag is not null) a,
(select max(action_time_stamp) as last_action from test_user_activity where user_name = '$username') b,
(select count(article_id) as num_no_prediction from test_user_activity where prediction is null and like_flag is null and user_name = '$username') c";
$result = mysql_query($sql);
$engine_check = 0;
while($row = mysql_fetch_array($result))
{
	$engine_check =$engine_check + $row["engine_check"];
}
if ($engine_check <> 0)
{
$sql = "SELECT count(like_flag) as num_like from test_user_activity
where user_name = '$username' and like_flag is not null";
$result = mysql_query($sql);
$num_like = 0;
while($row = mysql_fetch_array($result))
{
$num_like = $num_like + $row['num_like'];
}
if ($num_like >= 20)
{
//classifier text goes here

 
$classifier = new Bayes('like','dislike');
 
$sql = "SELECT a.article_id, a.article_text from test_article a, test_user_activity b where a.article_id = b.article_id and b.like_flag = 1 and user_name = '$username'";
$result = mysql_query($sql);
 
while ($row = mysql_fetch_array($result))
{
                $article_text = urldecode($row["article_text"]);
                $classifier->train('like', $article_text);
}
 
$sql = "SELECT a.article_id, a.article_text from test_article a, test_user_activity b where a.article_id = b.article_id and b.like_flag = 0 and user_name = '$username'";
$result = mysql_query($sql);
 
while ($row = mysql_fetch_array($result))
{
                $article_text = urldecode($row["article_text"]);
                $classifier->train('dislike', $article_text);
}
 
$sql = "SELECT d.article_id, d.article_text from
(SELECT a.article_id, a.article_text from test_article a, test_user b where a.article_id >= b.starting_id and b.user_name = '$username') d
left join (select article_id, sum(ignore_flag) as num_ignore, sum(like_flag) as num_like, count(prediction) as num_predict from test_user_activity where user_name = '$username' group by 1) b
on b.article_id = d.article_id
where num_ignore is null
and num_like is null";
 
$result = mysql_query($sql);
$num_classified = 0;
 
while ($row = mysql_fetch_array($result))
{
                $article_text = urldecode($row["article_text"]);
                //echo $classifier->classify($article_text) . PHP_EOL;
                $prediction = $classifier->classify($article_text);
                //echo $prediction . PHP_EOL;
 
                //$sql = "UPDATE test_unique SET prediction = '$prediction' where id = '$row[article_id]'";
                //$sql = "INSERT INTO test_user_activity (article_id, user_name, like_flag, prediction, star_flag, share_flag, ignore_flag, action_time_stamp) VALUES ('$row[article_id]', '$username', NULL, '$prediction', NULL, NULL, NULL, now())";
				$sql = "UPDATE test_user_activity SET prediction = '$prediction', action_time_stamp = now() where article_id = '$row[article_id]' and user_name = '$username'";
  //echo $sql . PHP_EOL;
                if (!mysql_query($sql))
                  {
                  die('Error: ' . mysql_error());
                  }
				$num_classified = $num_classified + 1;
}
 
$end_time = date('Y-m-d H:i:s');
$sql = "INSERT into test_user_classify_logs (user_name, start_time_stamp, end_time_stamp, num_classified) VALUES ('$username','$start_time', '$end_time', '$num_classified')";
if (!mysql_query($sql))
{
die('Error: ' . mysql_error());
}
}
else
{
	$end_time = date('Y-m-d H:i:s');
	$sql = "INSERT into test_user_classify_logs (user_name, start_time_stamp, end_time_stamp, num_classified) VALUES ('$username','$start_time', '$end_time', '$num_classified')";
	if (!mysql_query($sql))
	{
	die('Error: ' . mysql_error());
	}
}
}
else
{
$end_time = date('Y-m-d H:i:s');
$sql = "INSERT into test_user_classify_logs (user_name, start_time_stamp, end_time_stamp, num_classified) VALUES ('$username','$start_time', '$end_time', '0')";
if (!mysql_query($sql))
{
die('Error: ' . mysql_error());
}	
}

?>