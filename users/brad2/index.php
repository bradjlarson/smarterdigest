<?php
session_start();
$sesh_id = session_id();

include('/Dropbox/Coding/ShopSimply/db_connect.php');
mysql_select_db('jobs');
	if ($_SESSION['username'] == "brad2")
	{
		if ($_SESSION['pwd'] == "brad2")
		{
			$sql = "INSERT into test_user_access (user_name, access_type, access_time_stamp, session_id) values ('brad2', 'Login Success', now(), '$sesh_id')";
			$exec = mysql_query($sql);
			$user_predictions = '/Dropbox/Coding/smarterdigest/engine/users/brad2_predictions.php';
			include($user_predictions);
		}
		else
		{
			$sql = "INSERT into test_user_access (user_name, access_type, access_time_stamp, session_id) values ('brad2', 'Login PWD Fail', now(), '$sesh_id')";
			$exec = mysql_query($sql);
			$redirectURL = "http://smarterdigest.com/";
			header("Location: ".$redirectURL);
		}
	}
	else
	{
		$sql = "INSERT into test_user_access (user_name, access_type, access_time_stamp, session_id) values ('$_SESSION[username]', 'Login USERNAME Fail', now(), '$sesh_id')";
		$exec = mysql_query($sql);
		$redirectURL = "http://smarterdigest.com/";
		header("Location: ".$redirectURL);
	}
?>
<html>
<head>
<link rel="stylesheet" type="text/css" href="../../css/jobs_digest.css">
<link rel="stylesheet" type="text/css" href="../../css/font-awesome.min.css">
	<script src="../../lib/jquery.autosize.js"></script>	
	<script src="../../lib/jquery-1.8.3.min.js"></script>
	<script type="text/javascript" language="javascript">
	window.votes = [];
	window.stars = [];
	window.like_ids = [];
	window.dislike_ids = [];
	
	$(document).ready(function(){
		$("#suggestion_form").hide('fast');
	});
	
	$(window).bind('beforeunload', function() {
		send_votes();
		//return message;
	});
	
	function show_suggestion() {
		send_votes();
		$("#site").hide('fast');
		$("#suggestion_form").show('fast');
		$("#suggestion_box").autosize();
	}
	
	function submit_suggestion() {
		var suggestion = $("#suggestion_or_bug").serialize();
		$.ajax(
			{
				async: false,
				type: "POST",
				data: suggestion, 
				url: "submit_suggestion.php",
				success: function() {
					console.log("suggestion sent");
					$("#suggestion_form").hide('slow');
					$("#site").show('fast');
				}
			});
	}
	
	function load_acct_mgmt() {
		send_votes();
		$("#site").show("fast");
		$("#suggestion_form").hide('fast');
		$("#site").load('acct_mgmt.php');
	}
	
	function send_votes() {
	var post_data = $.param(votes);
	console.log(post_data);
	$.ajax(
		{
			async: false,
			type: "POST",
			data: post_data,
			url: "votes_test.php",
			success: function() {
				console.log("Success");
			}
		});
	post_data = $.param(stars);
	console.log(post_data);
	$.ajax(
		{
			async: false,
			type: "POST",
			data: post_data,
			url: "stars_test.php",
			success: function() {
				console.log("Success");
			}
		});
	}
	
	function show_likes() {
		$(".element").hide('fast');
		$(".element_dislike").hide('fast');
		$(".element_like").show('fast');
	}
	
	function show_dislikes() {
		$(".element").hide('fast');
		$(".element_like").hide('fast');
		$(".element_dislike").show('fast');
	}
	
	function hide_dislikes() {
		$(".element_dislike").hide('fast');
		$(".element_like").show('fast');
		$(".element_").show('fast');
		$("#hide_dislike").text("Show All Articles");
		$("#hide_dislike").attr('onclick', "show_all()"); 
	}
	
	function show_all() {
		$(".element_dislike").show('fast');
		$("#hide_dislike").text('Only show "Worth it" articles');
		$("#hide_dislike").attr('onclick', "hide_dislikes()"); 
	}
	
	function show_starred() {
		send_votes();
		$("#site").load('show_starred.php');
	}
			
	function reload_site() {
		send_votes();
		$("#site").load('queue.php');
		$("#top_bar").load('top_bar.php');
	}
	
	function last_thirty() {
		send_votes();
		$("#site").load('last_thirty.php');
		$("#top_bar").load('top_bar_thirty.php');
	}
	
	function logout() {
		send_votes();
		window.location = "logout.php";
	}
	
	function star_article(article_id) {
		$("#"+article_id).attr('class', "icon-star");
		$("#"+article_id).attr('onclick', "unstar_article(this.id)");
		var id = article_id.split("_");
		stars.push({name: id[0], value: "1"});
	}
	
	function unstar_article(article_id) {
		$("#"+article_id).attr('class', "icon-star-empty");
		$("#"+article_id).attr('onclick', "star_article(this.id)");
		var id = article_id.split("_");
		stars.push({name: id[0], value: "1"});
	}
	
	function show_text(article_id) {
		var id = article_id.split("_");
		$("#"+id[0]+"_b").load('../../goose/article_test/'+id[0]+'.txt');
		$("#"+article_id).attr("onclick","hide_text(this.id)");                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
	}
	
	function hide_text(article_id){
		var id = article_id.split("_");
		$("#"+id[0]+"_b").hide('fast');
		$("#"+article_id).attr("onclick","reshow_text(this.id)");                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
	}
	
	function reshow_text(article_id){
		var id = article_id.split("_");
		$("#"+id[0]+"_b").show('fast');
		$("#"+article_id).attr("onclick","hide_text(this.id)");     
	}
	
	function cast_vote(vote_choice,vote_value)
	{
		$("#"+vote_choice).attr('class',"vote_cast");
		var id = vote_choice.split("_");
		if (id[1] != "like")
		{
		$("#"+id[0]+"_like").attr('class',"vote");
		console.log("#"+id[0]+"_dislike");
		dislike_ids.push(id[0]);
		votes.push({name: id[0], value: "0"});
		}
		else
		{
		$("#"+id[0]+"_dislike").attr('class',"vote");	
		console.log("#"+id[0]+"_like");
		like_ids.push(id[0]);
		votes.push({name: id[0], value: "1"});
		}
	}
	
	</script>
</head>
<body>
<?php
include('/Dropbox/Coding/ShopSimply/db_connect.php');
echo '<div id="top_bar">' . PHP_EOL;
include('top_bar.php');
echo '</div>' . PHP_EOL;
echo '<div id="site">' . PHP_EOL;
include('queue.php');
echo '</div>' . PHP_EOL;
echo '<div id="suggestion_form">' . PHP_EOL;
echo '<form class="form-horizontal" id="suggestion_or_bug" action="" onsubmit="submit_suggestion()">' . PHP_EOL;
echo '<fieldset>' . PHP_EOL;
echo '<label for="suggestion">Please enter you suggestion or bug below:</label>' . PHP_EOL;
echo '<textarea id="suggestion_box" rows="4" name="suggestion_box"></textarea>' . PHP_EOL;
echo '<button type="submit" class="btn btn-inverse">Submit</button>' . PHP_EOL;
echo '</fieldset>' . PHP_EOL;
echo '</form>' . PHP_EOL;
echo '</div>' . PHP_EOL;
?>
</body>
</html>
