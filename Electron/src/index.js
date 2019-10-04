const mysql = require('mysql');
const { app, BrowserWindow } = require('electron');
const url = require('url');
const path = require('path');
const submitFormButton = document.querySelector("#login");

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

submitFormButton.addEventListener("submit", function(event){
    event.preventDefault();   // stop the form from submitting
    return Response('hola');
});

/* Perform a query
$query = 'SELECT * FROM `myTableName` LIMIT 10';

connection.query($query, function(err, rows, fields) {
    if(err){
        console.log("An error ocurred performing the query.");
        console.log(err);
        return;
    }

    console.log("Query succesfully executed", rows);
});

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