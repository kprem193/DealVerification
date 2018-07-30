<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Large Deal Verification</title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="" />
<meta name="author" content="" />
<!-- styles -->
<link rel="stylesheet" href="assets/css/fancybox/jquery.fancybox.css">
<link href="assets/css/bootstrap.css" rel="stylesheet" />
<link href="assets/css/bootstrap-theme.css" rel="stylesheet" />
<link rel="stylesheet" href="assets/css/slippry.css">
<link href="assets/css/style.css" rel="stylesheet" />
<link rel="stylesheet" href="assets/color/default.css">
<!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
<!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
<script src="assets/js/modernizr.custom.js"></script>
<style type="text/css">

textarea {
width: 1090px;
height: 20em;
}

</style>


</head>
<body>
<header>

<div id="navigation" class="navbar navbar-inverse navbar-fixed-top default" role="navigation">
  <div class="container">

    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="index.html">Large Deal Verification</a>
    </div>

	<div class="navigation">
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1"><nav>
      <ul class="nav navbar-nav navbar-right">
		<li><a href="#works">Technologies Used</a></li>
		<li><a href="#contact">Prototype</a></li>
      </ul></nav>
    </div><!-- /.navbar-collapse -->
	</div>

  </div>
</div>

</header>

<section id="works" class="section gray">
<div class="container">
	<div class="row">
		<div class="col-md-8 col-md-offset-2">
			<div class="heading">
				<h1><span>Technologies Used</span></h1>
				
			</div>
			<div class="sub-heading">
			</div>
		</div>
	</div>
	<ul>
				<li><h3>DeepSpeech - Speech to Text</h3></li>
				<li><h3>Spacy - Feature Extraction</h3></li>
			</ul>
	<div class="row">
		<div class="col-md-12">
						<ul class="grid effect" id="grid">
						<li>
							<a class="fancybox" data-fancybox-group="gallery" title="Portfolio name" href="assets/img/portfolio/1.jpg">
								<img src="assets/img/portfolio/1.png" alt="" />
							</a>						
						</li>
						<li><a href="assets/img/portfolio/2.jpg" class="fancybox" data-fancybox-group="gallery" title="Portfolio name"><img src="assets/img/portfolio/2.jpg" alt="" /></a></li>
						<li><a href="assets/img/portfolio/3.jpg" class="fancybox" data-fancybox-group="gallery" title="Portfolio name"><img src="assets/img/portfolio/3.jpg" alt="" /></a></li>
						<li><a href="assets/img/portfolio/4.jpg" class="fancybox" data-fancybox-group="gallery" title="Portfolio name"><img src="assets/img/portfolio/4.jpg" alt="" /></a></li>
>

		</div>
	</div>

</div>
	
</section>
<!-- section works -->
<!--section of upload file-->
<section id="contact" class="section">
<div class="container">
	<div class="row">
		<div class="col-md-8 col-md-offset-2">
			<div class="heading">
				<h3><span>UPLOAD YOUR FILE</span></h3>
			</div>
		</div>
	</div>
</div>

<div class="container">
	<div class="row">
		<div class="col-md-6">
			<h4><i class="icon-envelope"></i><strong>Audio-to-Text</strong></h4>
			  <form enctype="multipart/form-data" action="index.php" method="POST">
				    <p>Upload your file</p>
    					<input type="file" name="file1"></input><br />
					<input type="submit" value="submit"></input><p>
			<br><br><br>	
        
  			   </form>

<div class="clear"></div></font>
		</div>
	</div>
</div>
</section>



<a href="#" class="scrollup"><i class="fa fa-angle-up fa-2x"></i></a>
<!-- javascript -->
<script src="assets/js/jquery-1.9.1.min.js"></script>
<script src="assets/js/jquery.easing.js"></script>
<script src="assets/js/classie.js"></script>
<script src="assets/js/bootstrap.js"></script>
<script src="assets/js/slippry.min.js"></script>
<script src="assets/js/nagging-menu.js"></script>
<script src="assets/js/jquery.nav.js"></script>
<script src="assets/js/jquery.scrollTo.js"></script>
<script src="assets/js/jquery.fancybox.pack.js"></script> 
<script src="assets/js/jquery.fancybox-media.js"></script> 
<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyASm3CwaK9qtcZEWYa-iQwHaGi3gcosAJc&sensor=false"></script>
<script src="assets/js/masonry.pkgd.min.js"></script>
<script src="assets/js/imagesloaded.js"></script>
<script src="assets/js/jquery.nicescroll.min.js"></script>
<script src="assets/js/validate.js"></script>	
<script src="assets/js/AnimOnScroll.js"></script>
    <script>
        new AnimOnScroll( document.getElementById( 'grid' ), {
            minDuration : 0.4,
            maxDuration : 0.7,
            viewportFactor : 0.2
        } );
    </script>
<script>
	$(document).ready(function(){
	  $('#slippry-slider').slippry(
		defaults = {
			transition: 'vertical',
			useCSS: true,
			speed: 5000,
			pause: 3000,
			initSingle: false,
			auto: true,
			preload: 'visible',
			pager: false,		
		} 	  
	  )
	});
</script>


</html>



<?php
$a= file_get_contents("/var/www/html/LargeDeal/output.txt");
echo "<p style='color:red; margin-left:15rem; margin-right:15rem; font-size:30px; font-family: Montserrat sans-serif;'><strong>DEEPSPEECH</strong> :<br></p>";
echo "<p style='color:black; margin-left:15rem; margin-right:15rem; font-size:20px;font-family: Montserrat sans-serif;'> $a </p>";
$b= file_get_contents("/var/www/html/LargeDeal/google.txt");
echo "<p style='color:red; margin-left:15rem; margin-right:15rem; font-size:30px; font-family: Montserrat sans-serif;'><strong><br><br>GOOGLE</strong> :<br> </p>";
echo "<p style='color:black; margin-left:15rem; margin-right:15rem; font-size:20px;font-family: Montserrat sans-serif;'> $b </p>";
      

if(!empty($_FILES['file1']))
{
	$name = $_FILES['file1']['name'];
//$size = $_FILES['file1']['size'];
//$type = $_FILES['file1']['type'];

$tmp_name = $_FILES['file1']['tmp_name'];

if (isset($name)) 
{
    if(!empty($name)) 
    {
        $location = 'uploads/';
        if(move_uploaded_file($tmp_name, $location."file.wav")) 
        {
            echo "Uploaded!";
            echo "hello World"; 
      $result = shell_exec('/var/www/html/LargeDeal/deep.sh ');
		   echo $result;
      $result = shell_exec('/var/www/html/LargeDeal/google.sh ');
	                }

    } 
    else
    {
        echo 'Please choose a file';
    }
    
}
}


?>
