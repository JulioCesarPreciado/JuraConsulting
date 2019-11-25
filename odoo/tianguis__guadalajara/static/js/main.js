odoo.define('permisionario', function (require) {
    'use strict';
    var ajax = require('web.ajax');
    var utils = require('web.utils');
    var Model = require('web.Model');
    var core = require('web.core');
    var website = require('permisionario'); // The important line
    $(window).load(function () {
        
        var array = ["Cantabria", "Asturias", "Galicia", "Andalucia", "Extremadura"];

        array.sort();

        var select = document.getElementById('tianguis_s');
        var value = []
        for (value in array) {
            var option = document.createElement("option");
            option.text = array[value];
            console.log(option);
            select.add(option);
        }

    });
});