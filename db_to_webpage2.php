
<html>
<head>
	<title>Actulus home</title>
	<style type="text/css">
	body
	{
		background-image: url("safety.jpg");
	}
	</style>
</head>

<body>
<h2 style="color:#ff00ff">Actulus Securitas Analyser</h2>
   <form action="hi.php" method="post">
<input type="submit" value="submit" onclick="hi.php"><br/><br/><br/>
<table border="1" style="width:100%"><tr><td style="width:33%" id="worker1">
<font size="5" color="Green">WORKER 1</font><br/>
-----------------------------<br/>

<?php
   class MyDBs extends SQLite3
   {
      function __construct()
      {
         $this->open('database.db');
      }
   }
   $db = new MyDBs();
   if(!$db){
      echo $db->lastErrorMsg();
   } else {
      //echo "Opened database successfully\n</br><br/>";
   }

   $sql =<<<EOF
      SELECT * from Datas;
EOF;
   $ret = $db->query($sql);
   while($row = $ret->fetchArray(SQLITE3_ASSOC) ){
if ($row['TEMP']>37)
{
echo "<font color='Green'>";
}
if ($row['BPM']>120)
{
echo "<font color='Blue'>";
}
if ($row['VAL'] == 1)
{
	echo "<font color='Red'>";
}


  echo "TEMPERATURE =". $row['TEMP'] . "\n</br>"; 
  echo "Beats/minute = ". $row['BPM']."\n</br>";  
  echo "Button=0". $row['VAL'] ."\n</br><br>";  
   
 
   }
   echo "Operation done successfully\n";
   $db->close();


?></td>

<td style="width:33%">WORKER 2 </td>
<td style="width:33%">WORKER 3 </td></tr>
</table>

</form>
</body>
</html>

