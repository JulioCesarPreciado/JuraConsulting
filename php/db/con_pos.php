<?php

//Leer excel
require_once '../lib/PHPExcel-1.8/Classes/PHPExcel.php';
$archivo = "../doc/test.xlsx";
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

if($conn){
    for ($row = 2; $row <= $highestRow; $row++){ 
        $id = $sheet->getCell("A".$row)->getValue();
        $nombre = $sheet->getCell("B".$row)->getValue();
        $precio_total = $sheet->getCell("C".$row)->getValue();
        $qry = "INSERT INTO main  (id,nombre, precio_total, create_date,write_date) VALUES ($id,'$nombre', $precio_total,NOW(),NOW())";
        //echo $qry; die();
        $result = pg_query($conn, $qry);
    }
    echo 'Exito';    
}else{
    echo 'Error';
}
    
?>