<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db("jobs");
$sql = "SELECT star_flag, count(distinct article_id) as num_starred from test_user_activity where user_name = '$username' and star_flag = 1";
$result = mysql_query($sql);
$num_starred = 0;
while($row = mysql_fetch_array($result))
{
	$num_starred = $num_starred + $row["num_starred"];
}
if ($num_starred > 0)
{
//and num_ignore is null and num_like is null
$sql = "SELECT distinct d.id, d.item_title, d.item_url, b.prediction, b.num_ignore, b.num_like  from
(select distinct a.id, a.item_title, a.item_url from test_unique a, test_user c
where c.user_name = '$username'
and a.id > (c.starting_id - 30)) d, (select article_id, prediction, sum(ignore_flag) as num_ignore, sum(like_flag) as num_like, sum(star_flag) as num_star from test_user_activity where user_name = '$username' group by 1) b
where b.article_id = d.id
and num_star > 0
order by d.id asc";
$result = mysql_query($sql);
while($row = mysql_fetch_array($result))
{
	if ($row["prediction"] == "like")
	{
	echo '<div class="element_like" id="'.$row["id"].'">' . PHP_EOL;	
	}
	elseif (is_null($row["prediction"]))
	{
	echo '<div class="element" id="'.$row["id"].'">' . PHP_EOL;	
	}
	else
	{
	echo '<div class="element_dislike" id="'.$row["id"].'">' . PHP_EOL;	
	}
	echo '<div class="element_container">' . PHP_EOL;
	echo '<div class="icons">' . PHP_EOL;
	echo '</br>'.PHP_EOL;
	echo '<div class="rating"><i id="'.$row["id"].'_star" class="icon-star-empty" onclick="star_article(this.id)"></i></div>' . PHP_EOL;
	echo '</br>'.PHP_EOL;
	echo '<div class="share"><i id="'.$row["id"].'_share" class="icon-share"></i></div>' . PHP_EOL;
	echo '</div>' . PHP_EOL;
	echo '<div class="element_header">' . PHP_EOL;
	echo '<p id="'.$row["id"].'_t" onclick="show_text(this.id)">'.$row["item_title"].'</p>' . PHP_EOL;
	echo '<p><a id="'.$row["id"].'_u" href="'.$row["item_url"].'">'.$row["item_url"].'</a></p>' . PHP_EOL;
	echo '</div>' . PHP_EOL;
	echo '<div class="element_vote">' . PHP_EOL;
	if ($row["prediction"] == "like")
	{
	echo '<p id="'.$row["id"].'_like" class="vote_p" onclick="cast_vote(this.id,1)">Worth It</p>' . PHP_EOL;
	echo '<p id="'.$row["id"].'_dislike" class="vote" onclick="cast_vote(this.id,0)">Not Worth It</p>' . PHP_EOL;
	}
	elseif (is_null($row["prediction"]))
	{
	echo '<p id="'.$row["id"].'_like" class="vote" onclick="cast_vote(this.id,1)">Worth It</p>' . PHP_EOL;
	echo '<p id="'.$row["id"].'_dislike" class="vote" onclick="cast_vote(this.id,0)">Not Worth It</p>' . PHP_EOL;	
	}
	else
	{
	echo '<p id="'.$row["id"].'_like" class="vote" onclick="cast_vote(this.id,1)">Worth It</p>' . PHP_EOL;
	echo '<p id="'.$row["id"].'_dislike" class="vote_p" onclick="cast_vote(this.id,0)">Not Worth It</p>' . PHP_EOL;
	}
	echo '</div>' . PHP_EOL;
	echo '</div>' . PHP_EOL;
	echo '<div class="element_text" id="'.$row["id"].'_b"></div>' . PHP_EOL;
	echo '</div>' . PHP_EOL;
}
}
else
{
	echo '<p>No starred articles yet</p>' . PHP_EOL;
}
?>