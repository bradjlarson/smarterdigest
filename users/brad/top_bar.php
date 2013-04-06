<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db('jobs');
$sql = "SELECT distinct b.prediction, count(d.id) as num_in_queue from
(select distinct a.id, a.item_title, a.item_url from test_unique a, test_user c
where c.user_name = 'brad'
and a.id > (c.starting_id - 30)) d, (select article_id, prediction, sum(ignore_flag) as num_ignore, sum(like_flag) as num_like from test_user_activity where user_name = 'brad' group by 1) b
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
$sql = "SELECT prediction, like_flag, count(like_flag) as num_articles from test_user_activity where user_name = 'brad' and like_flag is not null and prediction is not null group by 1,2 order by 1,2";
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
$total_accuracy = (($dislike_dislike + $like_like) / $total_liked) * 100;
$dislike_accuracy = (($dislike_dislike) / ($dislike_dislike + $dislike_like)) * 100;
$like_accuracy = (($like_like) / ($like_dislike + $like_like)) * 100;
$like = $like_like + $dislike_like;
$dislike = $dislike_dislike + $like_dislike;

$sql = "SELECT star_flag, count(distinct article_id) as num_starred from test_user_activity where user_name = 'brad' and star_flag = 1";
$result = mysql_query($sql);
$num_starred = 0;
while($row = mysql_fetch_array($result))
{
	$num_starred = $num_starred + $row["num_starred"];
}
echo '<div class="navbar navbar-inverse navbar-fixed-top">' . PHP_EOL;
echo '	<div class="navbar-inner">' . PHP_EOL;
echo '      <div class="container">' . PHP_EOL;
echo '       	<button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">' . PHP_EOL;
echo '           <span class="icon-bar"></span>' . PHP_EOL;
echo '           <span class="icon-bar"></span>' . PHP_EOL;
echo '           <span class="icon-bar"></span>' . PHP_EOL;
echo '       	</button>' . PHP_EOL;
echo '			<ul class="nav">' . PHP_EOL;
echo '   	 		<li><a class="brand" href="#">Welcome, brad</a></li>' . PHP_EOL;	
echo '   			<li class="dropdown"><a class="dropdown-toggle" data-toggle="dropdown" href="#">Articles in Queue: '.$num_in_queue.'<b class="caret"></b></a>' . PHP_EOL;
echo '      			<ul class="dropdown-menu">' . PHP_EOL;
echo '         				<li onclick="show_likes()"><a href="#"># Worth it: '.$num_like.'</a></li>' . PHP_EOL;
echo '         				<li onclick="show_dislikes()"><a href="#"># Not worth it: '.$num_dislike.'</a></li>' . PHP_EOL;
echo '      			</ul>' . PHP_EOL;
echo '   			</li>' . PHP_EOL;
echo '   			<li class="dropdown"><a href="#" class="dropdown-toggle" data-toggle="dropdown">Stats<b class="caret"></b></a>' . PHP_EOL;
echo '      			<ul class="dropdown-menu" role="menu">' . PHP_EOL;
echo '         				<li><a href="#">Overall Prediction Accuracy: '.round($total_accuracy,2).'%</a></li>' . PHP_EOL;
echo '         				<li><a href="#">Worth it Accuracy: '.round($like_accuracy,2).'%</a></li>' . PHP_EOL;
echo '         				<li><a href="#">Not Worth it Accuracy: '.round($dislike_accuracy,2).'%</a></li>' . PHP_EOL;
echo '         				<li><a href="#">Articles Read: '.$total_liked.'</a></li>' . PHP_EOL;
echo '         				<li><a href="#">Articles Liked: '.$like.'</a></li>' . PHP_EOL;
echo '         				<li><a href="#">Articles Disliked: '.$dislike.'</a></li>' . PHP_EOL;
echo '         				<li onclick="show_starred()"><a href="#">Articles Starred: '.$num_starred.'</a></li>' . PHP_EOL;
echo '      			</ul>' . PHP_EOL;
echo '   			</li>' . PHP_EOL;
echo '   			<li><a class="dropdown-toggle" data-toggle="dropdown" href="#">Options<b class="caret"></b></a>' . PHP_EOL;
echo '      			<ul class="dropdown-menu">' . PHP_EOL;
echo '         				<li onclick="hide_dislikes()"><a id="hide_dislike" href="#">Only show worth it articles</a></li>' . PHP_EOL;
echo '         				<li onclick="last_thirty()"><a href="#">Only show 30 most recent articles</a></li>' . PHP_EOL;
echo '         				<li onclick="reload_site()"><a href="#">Update feed</a></li>' . PHP_EOL;
echo '         				<li><a href="#">Load current view of HN</a></li>' . PHP_EOL;
echo '         				<li onclick="show_suggestion()"><a href="#">Submit suggestion or bug</a></li>' . PHP_EOL;
echo '     				</ul>' . PHP_EOL;
echo '  			</li>' . PHP_EOL;
echo '  			<li><a onclick="load_acct_mgmt()" href="#">Acct Mgmt</a></li>' . PHP_EOL;
echo '   			<li onclick="logout()"><a href="../../index.php">Logout</a></li>' . PHP_EOL;
echo '			</ul>' . PHP_EOL;
echo '		</div>' . PHP_EOL;
echo '	  </div>' . PHP_EOL;
echo '	</div>' . PHP_EOL;

?>