<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db("jobs");
//and num_ignore is null and num_like is null
$sql = "SELECT x.* from 
(SELECT distinct d.id, d.item_title, d.item_url, b.prediction, b.num_ignore, b.num_like  from
(select distinct a.id, a.item_title, a.item_url from test_unique a, test_user c
where c.user_name = 'testing'
and a.id > (c.starting_id - 30)) d, (select article_id, prediction, sum(ignore_flag) as num_ignore, sum(like_flag) as num_like from test_user_activity where user_name = 'testing' group by 1) b
where b.article_id = d.id
order by d.id desc
limit 30) x 
order by x.id asc";
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
?>