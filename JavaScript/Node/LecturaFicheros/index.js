const fs = require('fs');

fs.writeFile('./texto.txt','linea uno',function(err){
    if(err){
        console.log(err);
    }
    console.log('Archivo creado');
});

console.log('Ultima linea de codigo');//sale primero este print
//porque fs.writeFile solo esta esperando a que lo haga el sistema operativo
//a que cree

fs.readFile('./texto.txt',function(err,data) {
    if(err){
        console.log(err);
    }
    console.log(data.toString());
});