<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db('jobs');
$sql = "SELECT distinct b.prediction, count(d.id) as num_in_queue from
(select distinct a.id, a.item_title, a.item_url from test_unique a, test_user c
where c.user_name = 'crthews'
and a.id > (c.starting_id - 30)) d, (select article_id, prediction, sum(ignore_flag) as num_ignore, sum(like_flag) as num_like from test_user_activity where user_name = 'crthews' group by 1) b
where b.article_id = d.id
and num_ignore is null
and num_like is null
group by 1
order by 1";
$result = mysql_query($sql);
$num_in_queue = 0;
$num_dislike = 0;
$num_like = 0;
while($row = mysql_fetch_array($result))
{
	$num_in_queue = $num_in_queue + $row["num_in_queue"];
	if ($row["prediction"] == "dislike")
	{
		$num_dislike = $num_dislike + $row["num_in_queue"];
	}
	elseif ($row["prediction"] == "like")
	{
		$num_like = $num_like + $row["num_in_queue"];
	}
}
$sql = "SELECT prediction, like_flag, count(like_flag) as num_articles from test_user_activity where user_name = 'crthews' and like_flag is not null and prediction is not null group by 1,2 order by 1,2";
$result = mysql_query($sql);
$dislike_dislike = 0;
$dislike_like = 0;
$like_dislike = 0;
$like_like = 0;
$total_liked = 0;
$i = 1;
while($row = mysql_fetch_array($result))
{
	if ($row["prediction"] == "dislike" && $row["like_flag"] == 0)
	{
		$dislike_dislike = $row["num_articles"];
	}
	elseif ($row["prediction"] == "dislike" && $row["like_flag"] == 1)
	{
		$dislike_like = $row["num_articles"];
	}
	elseif ($row["prediction"] == "like" && $row["like_flag"] == 0)
	{
		$like_dislike = $row["num_articles"];
	}
	elseif ($row["prediction"] == "like" && $row["like_flag"] == 1)
	{
		$like_like = $row["num_articles"];
	}
	$total_liked = $total_liked + $row["num_articles"];
	$i = $i + 1;
}
if ($total_liked >= 20)
{
$total_accuracy = ($dislike_dislike + $like_like) / $total_liked;
$dislike_accuracy = ($dislike_dislike) / ($dislike_dislike + $dislike_like);
$like_accuracy = ($like_like) / ($like_dislike + $like_like);
$like = $like_like + $dislike_like;
$dislike = $dislike_dislike + $like_dislike;
}
else
{
$total_accuracy = 0;
$dislike_accuracy = 0;
$like_accuracy = 0;
$like = 0;
$dislike = 0;
}

$sql = "SELECT star_flag, count(distinct article_id) as num_starred from test_user_activity where user_name = 'crthews' and star_flag = 1";
$result = mysql_query($sql);
$num_starred = 0;
while($row = mysql_fetch_array($result))
{
	$num_starred = $num_starred + $row["num_starred"];
}

echo '<div id="cssmenu">'. PHP_EOL;
echo '<ul>' . PHP_EOL;
echo '   <li><a href="#"><span>Welcome, crthews</span></a></li>' . PHP_EOL;
echo '   <li class="has-sub"><a href="#"><span>Articles in Queue: '.$num_in_queue.'</span></a>' . PHP_EOL;
echo '      <ul>' . PHP_EOL;
echo '         <li><a href="#"><span onclick="show_likes()"># Worth it: '.$num_like.'</span></a></li>' . PHP_EOL;
echo '         <li class="last"><a href="#"><span onclick="show_dislikes()"># Not worth it: '.$num_dislike.'</span></a></li>' . PHP_EOL;
echo '      </ul>' . PHP_EOL;
echo '   </li>' . PHP_EOL;
echo '   <li class="has-sub"><a href="#"><span>Stats</span></a>' . PHP_EOL;
echo '      <ul>' . PHP_EOL;
echo '         <li><a href="#"><span>Overall Prediction Accuracy: '.round($total_accuracy,2).'%</span></a></li>' . PHP_EOL;
echo '         <li><a href="#"><span>Worth it Accuracy: '.round($like_accuracy,2).'%</span></a></li>' . PHP_EOL;
echo '         <li><a href="#"><span>Not Worth it Accuracy: '.round($dislike_accuracy,2).'%</span></a></li>' . PHP_EOL;
echo '         <li><a href="#"><span>Articles Read: '.$total_liked.'</span></a></li>' . PHP_EOL;
echo '         <li><a href="#"><span>Articles Liked: '.$like.'</span></a></li>' . PHP_EOL;
echo '         <li class="last"><a href="#"><span>Articles Disliked: '.$dislike.'</span></a></li>' . PHP_EOL;
echo '         <li class="last"><a href="#"><span onclick="show_starred()">Articles Starred: '.$num_starred.'</span></a></li>' . PHP_EOL;
echo '      </ul>' . PHP_EOL;
echo '   </li>' . PHP_EOL;
echo '   <li class="has-sub"><a href="#"><span>Options</span></a>' . PHP_EOL;
echo '      <ul>' . PHP_EOL;
echo '         <li><a href="#"><span id="hide_dislike" onclick="hide_dislikes()">Only show "Worth it" articles</span></a></li>' . PHP_EOL;
echo '         <li><a href="#"><span onclick="last_thirty()">Only show 30 most recent articles</span></a></li>' . PHP_EOL;
echo '         <li><a href="#"><span onclick="reload_site()">Update feed</span></a></li>' . PHP_EOL;
echo '         <li><a href="#"><span>Load current view of HN</span></a></li>' . PHP_EOL;
echo '         <li onclick="show_suggestion()" class="last"><a href="#"><span>Submit suggestion or bug</span></a></li>' . PHP_EOL;
echo '      </ul>' . PHP_EOL;
echo '   </li>' . PHP_EOL;
echo '   <li onclick="load_acct_mgmt()"><a href="#"><span>Acct Mgmt</span></a></li>' . PHP_EOL;
echo '   <li class="last"><a href="../../index.php"><span onclick="logout();">Logout</span></a></li>' . PHP_EOL;
echo '</ul>' . PHP_EOL;
echo '</div>' . PHP_EOL;
?>