const electron = require('electron')
const btnOdoo = document.getElementById('btnOdoo')

btnOdoo.addEventListener('click', function (event) {
    console.log(electron.dialog.showMessageBox({
        type: 'error',
        buttons: ['Cancel'],
        defaultId: 2,
        title: 'Error de base de datos',
        message: 'Ocurrio un error al ejecutar el query',
        detail: err,
    }));
    return;
})