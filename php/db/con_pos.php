<?php

//Leer excel
require_once 'lib/PHPExcel/Classes/PHPExcel.php';
$archivo = "libro1.xlsx";
$inputFileType = PHPExcel_IOFactory :: identify($archivo);
$objReader = PHPExcel_IOFactory :: createReader($inputFileType);
$objPHPExcel = $objReader -> load($archivo);
$sheet = $objPHPExcel -> getSheet(0);
$highestRow = $sheet -> getHighestRow();
$highestColumn = $sheet -> getHighestColumn();

//Conexión
$conn = pg_connect(
  "host=localhost port=5432 dbname=Pruebas user=julio password=julio"
);
    
?>