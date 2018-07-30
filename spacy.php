<?php

$name = $_FILES['file']['name'];
//$size = $_FILES['file']['size'];
//$type = $_FILES['file']['type'];

$tmp_name = $_FILES['file']['tmp_name'];

if (isset($name)) 
{
    if(!empty($name)) 
    {
        $location = 'uploads/';
        if(move_uploaded_file($tmp_name, $location."test_data.txt")) 
        {
            echo "Uploaded!ok";
            echo "hello World";
           $result = shell_exec('/home/sangeetha/lampstack-7.1.19-1/apache2/htdocs/prem/spacy_shell_scripting.sh');
           echo result;
        }

    } 
    else
    {
        echo 'Please choose a file';
    }
    
}


?>
