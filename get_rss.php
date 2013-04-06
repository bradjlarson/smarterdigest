#!/usr/bin/php5
<?php
include_once('/Dropbox/Coding/ShopSimply/simplepie/autoloader.php');
include_once('/Dropbox/Coding/ShopSimply/simplepie/idn/idna_convert.class.php');
include('/Dropbox/Coding/ShopSimply/db_connect.php');
$feed = new SimplePie();
/*
if (isset($_GET['js']))
{
	SimplePie_Misc::output_javascript();
	die();
}

// Make sure that page is getting passed a URL
if (isset($_GET['feed']) && $_GET['feed'] !== '')
{
	// Strip slashes if magic quotes is enabled (which automatically escapes certain characters)
	if (function_exists('get_magic_quotes_gpc') && get_magic_quotes_gpc())
	{
		$_GET['feed'] = stripslashes($_GET['feed']);
	}

	// Use the URL that was passed to the page in SimplePie
	$feed->set_feed_url($_GET['feed']);
}

// Allow us to choose to not re-order the items by date. (optional)
if (!empty($_GET['orderbydate']) && $_GET['orderbydate'] == 'false')
{
	$feed->enable_order_by_date(false);
}

// Trigger force-feed
if (!empty($_GET['force']) && $_GET['force'] == 'true')
{
	$feed->force_feed(true);
}
*/
// Initialize the whole SimplePie object.  Read the feed, process it, parse it, cache it, and
// all that other good stuff.  The feed's information will not be available to SimplePie before
// this is called.
$feed->set_feed_url('http://news.ycombinator.com/rss');
//$feed->force_feed(true);
$success = $feed->init();

// We'll make sure that the right content type and character encoding gets set automatically.
// This function will grab the proper character encoding, as well as set the content type to text/html.
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
		$sql = "INSERT into HN_RSS (source, item_title, item_url, item_rss_url, item_time_stamp) VALUES ('$title', '$item_title', '$permalink', '$item_rss_link', now())";
		//echo "$sql";
		$i = $i + 1;
		if (!mysql_query($sql))
		  {
		  $error = mysql_error();
		  $log = '/logs/php_errors.log';
		  $fh = fopen($log, 'a');
		  fwrite($fh, $error);
		  fclose($fh);
		  }
		//$result = mysql_query($sql);
	}
echo "SQL successful\n";
}
else 
{
echo "Feed Load not successful";
}
echo "<html>";
echo "<body>";
echo "<p>";

echo "$i Records inserted into Jobs.HN_RSS\n";
echo "</p>";
echo "</body>";
echo "</html>";
?>
