const mysql = require('mysql');
const { app, BrowserWindow } = require('electron');
const url = require('url');
const path = require('path');
const bcrypt = require('bcrypt');
const submitFormButton = document.querySelector("#ingresar");


var connection = mysql.createConnection({
    host: 'remotemysql.com',
    user: 'qs3lGxGdqy',
    password: 'OsZWjmzMkN',
    database: 'qs3lGxGdqy'
});

connection.connect(function (err) {
    // in case of error
    if (err) {
        console.log(err.code);
        console.log(err.fatal);
    }
});

submitFormButton.addEventListener("submit", function (event) {
    event.preventDefault();   // stop the form from submitting
    let email = document.getElementById('email').value;
    let pass = document.getElementById('password').value;
    $query = "SELECT * FROM `users` WHERE email = '" + email + "'";

    connection.query($query, function (err, rows, fields) {
        if (err) {
            console.log("Ocurrio un error a la hora de ejecutar el QRY.");
            console.log(err);
            return;
        }
        let hash = rows[0].pass
        console.log(hash);
    });

});

/* Perform a query


// Close the connection
connection.end(function(){
    // The connection has been closed
});

let mainWindow;

app.on('ready', () => {
    mainWindow = new BrowserWindow({
        webPreferences: {
            nodeIntegration: false
        }
    });
    mainWindow.setMenuBarVisibility(false);
    mainWindow.loadURL(url.format({
        pathname: path.join(__dirname, 'views/home.html'),
        protocol: 'file',
        slashes: true,
    }))
});*/