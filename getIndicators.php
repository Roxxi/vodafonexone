<?php
	error_reporting(0);
	
	$ticker = $_GET['ticker'];

	$returnValues = array();
	$printValues = array();
	
	$torun = 'java -jar "C:\\getIndicators.jar" "'.$ticker.'"';
	
	
	$values = exec($torun);	
	
	$returnValues = split('[{=,}]',$values);
	
	
	for($i = 1; $i < 7; $i = $i+2)
	{
		$printValues[trim($returnValues[$i])] = trim($returnValues[$i+1]);
	}
	
	print_r(json_encode($printValues));
?>