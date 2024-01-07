<?php
$db=new mysqli("localhost","root","");
if(!$db)
{
    echo "Failed";
}
else
{
    echo "Connection Successfull";
}
?>