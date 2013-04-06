<html>
<head>
	<link rel="stylesheet" type="text/css" href="css/font-awesome.min.css">
	<link href="css/bootstrap.min.css" rel="stylesheet" media="screen">
	<!-- <link rel="stylesheet" type="text/css" href="css/splash.css">	-->
	<script src="lib/jquery-1.8.3.min.js"></script>
</head>
<body>
<div class="container">
<div class="row-fluid" id="splash_screen">
	<div class="span12" id="welcome">
		<h2 class="text-center" id="welcome_text">Welcome to SmarterDigest for HackerNews</h2>
		<h3 class="text-center">Please choose one of the options below:</h3>
	</div>
</div>
<div class="row-fluid" id="options_container">
	<div class="span4 offset2" id="create_account">
		<h3 class="text-left" id="create_account_text">Create Account</h3>
		<form class="form-horizontal" id="create_account_form" action="create_acct.php" method="POST">
			<fieldset>      
		    <label for="create_email">Email</label>
		    <input type="text" id="create_email" name="create_email" placeholder="Email">
		    <label for="create_user_name">Username</label>
		    <input type="text" id="create_user_name" name="create_user_name" placeholder="Username">
		    <label for="create_password">Password</label>
		    <input type="password" id="create_password" name="create_password" placeholder="Password">
			</br>
			</br>
		   	<button type="submit" class="btn btn-inverse btn-large">Create Account</button>
			</fieldset>
		</form>
	</div>
		<div class="span4 offset1" id="login">
			<h3 class="text-left" id="login_text">Login</h3>
			<form class="form-horizontal" id="login_account_form" action="login.php" method="POST">
				<fieldset>      
				</br>
				</br>					
			    <label for="login_user_name">Username</label>
			    <input type="text" id="login_user_name" name="login_user_name" placeholder="Username">
			    <label for="login_password">Password</label>
			    <input type="password" id="login_password" name="login_password" placeholder="Password">
				</br>
				</br>
			   	<button type="submit" class="btn btn-inverse btn-large">Login</button>
				</fieldset>
			</form>
		</div>
</div>
</div>
</body>
</html>		
