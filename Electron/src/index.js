const mysql = require('mysql')

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