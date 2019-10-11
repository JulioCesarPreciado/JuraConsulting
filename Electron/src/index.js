const mysql = require('mysql');
const { BrowserWindow } = require('electron');
const electron = require('electron').remote;
const url = require('url');
const path = require('path');
var hash = require("node-php-password");
const submitFormButton = document.querySelector("#ingresar");

// Conexión con la base de datos
var connection = mysql.createConnection({
    host: 'remotemysql.com',
    user: 'qs3lGxGdqy',
    password: 'OsZWjmzMkN',
    database: 'qs3lGxGdqy'
});

//Validaciones y conector de la base de datos
connection.connect(function (err) {
    // in case of error
    if (err) {
        console.log(err.code);
        console.log(err.fatal);
    }
});

//Evento del botón
submitFormButton.addEventListener("submit", function (event) {
    event.preventDefault();   // stop the form from submitting
    let email = document.getElementById('email').value;
    let pass = document.getElementById('password').value;
    $query = "SELECT * FROM `users` WHERE email = '" + email + "'";

    connection.query($query, function (err, rows, fields) {
        if (err) {
            console.log(electron.dialog.showMessageBox({
                type: 'error',
                buttons: ['Cancel'],
                defaultId: 2,
                title: 'Error de base de datos',
                message: 'Ocurrio un error al ejecutar el query',
                detail: err,
            }));
            return;
        }
        //Validación de si el correo es el correcto
        if (rows.length > 0) {
            //Validación de que la contraseña sea correcta
            if (hash.verify(pass, rows[0].pass)) {
                //Authentication OK
                connection.end(function () { });
                document.location.href = 'home.html';
            } else {
                //Authentication FAILED
                console.log(electron.dialog.showMessageBox({
                    type: 'error',
                    buttons: ['Cancel'],
                    defaultId: 2,
                    title: 'Contraseña incorrecta.',
                    message: 'La contraseña es incorrecta.',
                    detail: 'Asegure que la contreseña sea la correcta.',
                }));
                document.getElementById('password').value = '';
                return;
            }
        } else {
            console.log(electron.dialog.showMessageBox({
                type: 'error',
                buttons: ['Cancel'],
                defaultId: 2,
                title: 'Correo no valido o incorrecto.',
                message: 'El correo no existe.',
                detail: 'Asegure de que introdujo el correo correcto.',
            }));
            return;
        }
    });
});