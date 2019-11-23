<?php
//Create pass
$passHash = password_hash('luisesgay1', PASSWORD_BCRYPT);

//Verify pass
password_verify('luisesgay1', '$2y$10$ISMMFLcvt4pZEYH4Cl08B.v/8r7N2k1ZZIPyEx1SyvyPlrwtFd5mW');

?>

<h1>Hola</h1>