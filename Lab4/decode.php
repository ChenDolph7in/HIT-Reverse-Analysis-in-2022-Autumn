<?php
	
	function E($D,$K){
		for($i=0;$i<strlen($D);$i++){
			$D[$i] = $D[$i]^$K[($i+1)&15];
		}
		return $D;
	}
		
	function O($D){
		$D1=str_replace(" ","+",$D); 
		return base64_decode($D1);
	}
	
	function Q($D){
		return base64_encode($D);
	}
		
	$P="OgRUWzZ%2FDUw5ZQRaZAUnfylbVFwGfwlPOXQAWlBjNAo0Wg1fAH4KTjdfb1tkTidcOltUYjJpXAQ%3D";
	$T='3c6e0b8a9c15224a';
	$F=O(E(O(urldecode($P)),$T));
	echo $F;
	
	echo "<hr>";
	
	$ret="11cd6a8758984163AQQWey4LO1EAWAwBVgcCRQJ+N0QAe1lPIFx/WmsGFVgBBFxJLlYjVgBwXkpxYChELlwgRC9sJE0uW2RVf3A0BS1yKAYvUihzLHV4AXFiKHg5Wx1YOEFUTgJ5dHh/ZQpKLnIsSC5sJEEvZXwCe3AgAixcKAQtUjALIGVsBnFiKHgCYVBbOGAGTAB2XUVxYCR5LlwkSS9rUUEuYgVLfHcgRC1iCgAvfA5ALVZeS39lDWAgUVgN6c37ac826a2a04bc";
	
	$ret1=substr($ret,16);
	$ret2=substr($ret1,0,-16);
	echo $ret2;
	echo "<hr>";
	$R=urldecode(E(O(urldecode($ret2)),$T));
	echo $R;
?>

