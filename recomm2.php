<?php

  

    // $command = escapeshellcmd('python3 /tech.py');
    // $output = shell_exec($command);
    // echo $output;
	// exec("python /tech.py",$lst);
	// echo implode($lst);
	// echo shell_exec("python C:/xampp/htdocs/tech.py 'Turbo'");
$url = "https://script.googleusercontent.com/macros/echo?user_content_key=te3kZBVcGJrgBQ048Q986yOSpl5Otg80dhB3My-t3SuxSkQmbMCphBZn3oAATUETsIq0U-6kf-T61V81sMLK-i7DAqaZgNFrm5_BxDlH2jW0nuo2oDemN9CCS2h10ox_1xSncGQajx_ryfhECjZEnP-RXbENZSdunsTBWhlBgeBvJ81NB2xT-_6wZ3i7V-HhXfNI3NLts0zjb5oTiopo_Z0mgLDwm9cO&lib=M2vvNVK-Pz8ZzUqGIKbPwh9NmVEP2uox5";
$json = file_get_contents($url);
$json_data = json_decode($json, true);

        	
        	// echo "\n";
 
echo '<div class="w3-container">';
        echo "<h2>Recommendation</h2>";
        foreach(array_reverse($json_data) as $product){
        foreach(array_reverse($product) as $p){
        echo '<div class="w3-panel w3-blue w3-round-xlarge">';
        echo $p;
        echo '</div>';
               }
    }
echo "</div>";


?>