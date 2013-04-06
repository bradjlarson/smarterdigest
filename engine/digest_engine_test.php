#!/usr/bin/php5
<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
include_once('/Dropbox/Coding/ShopSimply/simplepie/autoloader.php');
include_once('/Dropbox/Coding/ShopSimply/simplepie/idn/idna_convert.class.php');
require_once '/Dropbox/Coding/classifier-php/bayes.php';
mysql_select_db('jobs');

$feed = new SimplePie();
$feed->set_feed_url('http://news.ycombinator.com/rss');
$success = $feed->init();

$feed->handle_content_type();
$i = 0;
if ($success) 
{
	$link = $feed->get_link();
	$title = $feed->get_title();
	$descrip = $feed->get_description();
	foreach($feed->get_items() as $item)
	{
		mysql_select_db('jobs');
		$permalink = $item->get_permalink();
		$item_title = $item->get_title();
		$item_title = str_replace("'", "", $item_title);
		$item_rss_link = $item->get_content();
		//$item_rss_link = "Testing";
		$item_rss_link = urlencode($item_rss_link);
		$sql = "INSERT into test_rss (source, item_title, item_url, item_rss_url, item_time_stamp) VALUES ('$title', '$item_title', '$permalink', '$item_rss_link', now())";
		//echo "$sql";
		$i = $i + 1;
		if (!mysql_query($sql))
		  {
		  die('Error: ' . mysql_error());
		  }
		//$result = mysql_query($sql);
	}
	echo "SQL successful\n";
}
else 
{
	echo "Feed Load not successful";
}

$sql = "INSERT into test_day (item_title, item_url, item_rss_url, feed_date)
select distinct min(a.item_title), a.item_url, min(a.item_rss_url), left(item_time_stamp,10) as feed_date from test_rss a,
(select item_url, sum(processed) as num_occur from test_rss group by 1) b
where a.item_url = b.item_url
and b.num_occur = 0
and a.processed = 0
group by 2, 4";
if (!mysql_query($sql))
  {
  die('Error: ' . mysql_error());
  }
//$result = mysql_query($sql);

$sql = "INSERT into test_unique (item_url, item_title, item_rss_url, entry_date)
select distinct min(a.item_url), a.item_title, min(a.item_rss_url), min(left(item_time_stamp,10)) as entry_date from test_rss a,
(select item_url, sum(processed) as num_occur from test_rss group by 1) b
where a.item_url = b.item_url
and b.num_occur = 0
and a.processed = 0
group by 2";
if (!mysql_query($sql))
{
	die('Error: ' . mysql_error());
}

$sql = "UPDATE test_rss set processed = 1 where processed = 0";
if (!mysql_query($sql))
  {
  die('Error: ' . mysql_error());
  }

$get_articles = "/Dropbox/Coding/goose/get_articles.sh";
$fh = fopen($get_articles, 'w') or die("cannot open get_articles.sh");
$sql = 'SELECT distinct id, item_url from test_unique where processed = 0 order by id asc';
$result = mysql_query($sql);
$shebang = "#!/bin/ksh\n";
fwrite($fh, $shebang);
//$shebang = "cd ../goose/";
//fwrite($fh, $shebang);
while($row = mysql_fetch_array($result))
{
$retrieve_article = 'MAVEN_OPTS="-Xms256m -Xmx2000m"; ./mvn exec:java -Dexec.mainClass=com.gravity.goose.TalkToMeGoose -Dexec.args="'.$row["item_url"].'" -e -q > /Dropbox/Coding/goose/article_test/'.$row["id"].'.txt'."\n";
fwrite($fh, $retrieve_article);
$text = 'echo "Article ' . $row["id"] . 'added"' . PHP_EOL;
fwrite($fh, $text);
}
fclose($fh);
$command = 'cd /Dropbox/Coding/goose/; ./get_articles.sh;';
$fetch_articles = system($command);

$sql = "DELETE from test_stats";
$exec = mysql_query($sql);

$sql = "SELECT distinct a.item_title, a.item_url, c.id, a.num_hours, b.num_days from
(select item_title, item_url, item_rss_url, count(id) as num_hours from test_rss group by 1, 2, 3) a, (select distinct id, item_url from test_unique) c,
(select item_url, count(distinct feed_date) as num_days from test_day group by 1) b
where a.item_url = b.item_url
and a.item_url = c.item_url";

$result = mysql_query($sql);

while($row = mysql_fetch_array($result))
{
	$title = str_replace("'", "", $row["item_title"]);
	$title_components = explode(" ", $title);
	$title_text = "";
	foreach($title_components as $value)
	{
		$title_text = $title_text . "T-" . $value . " ";
	}
	$url_components = explode(".",$row["item_url"]);
	if (count($url_components) == 2)
	{
		$extra = explode("/",$url_components[1]);
		$extra_text = "";
		foreach($extra as $value)
		{
			$extra_text = $extra_text . " DE-" . $value;
		}
		$extra_text = $extra_text . " ";
		$sql = "INSERT into test_stats (article_id, item_title, num_hours, num_days, domain_name, domain_locale) VALUES ('$row[id]', '$title_text', '$row[num_hours]', '$row[num_days]', '$url_components[0]', '$extra_text')";
		if (!mysql_query($sql))
		{
			die('Error: ' . mysql_error());
		}
	}
	else
	{
		$extra = explode("/",$url_components[2]);
		$extra_text = "";
		foreach($extra as $value)
		{
			$extra_text = $extra_text . " DE-" . $value;
		}
		$extra_text = $extra_text . " ";
		$sql = "INSERT into test_stats (article_id, item_title, num_hours, num_days, domain_name, domain_locale) VALUES ('$row[id]', '$title_text', '$row[num_hours]', '$row[num_days]', '$url_components[0] . $url_components[1]', '$extra_text')";
		if (!mysql_query($sql))
		{
			die('Error: ' . mysql_error());
		}
	}
}

$sql = "SELECT a.article_id, a.item_title, a.num_hours, a.num_days, a.domain_name, a.domain_locale from test_stats a, test_unique b where a.article_id = b.id and b.processed = 0";
$article_text = "";
$result = mysql_query($sql);
while ($row = mysql_fetch_array($result))
{
	//"hours-".$row["num_hours"]." days-".$row["num_days"]." ".
	$header = $row["domain_name"].$row["domain_locale"].$row["item_title"];
	$header = urlencode($header);
	$article_text = file_get_contents('/Dropbox/Coding/goose/article_test/'.$row["article_id"].'.txt');
	$article_text = urlencode($article_text);
	$sql = "INSERT into test_article (article_id, article_text) VALUES ('$row[article_id]', '$header+$article_text')";
	if (!mysql_query($sql))
	  {
	  die('Error: ' . mysql_error());
	  }
}

$cmd = '/Dropbox/Coding/smarterdigest/engine/./run_predictions.sh &';
$get_predictions = system($cmd);

$sql = "UPDATE test_unique set processed = 1 where processed = 0";
$exec = mysql_query($sql);

?>

