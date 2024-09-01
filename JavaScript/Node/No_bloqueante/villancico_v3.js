//no bloqueante version 2
//para evitar hacer parentesis dentro de parentesis dentro de pasentesis
//hacemos
var fs = require("fs");

console.log("\nAbriendo Archivo...");

function imprimir(error , content){
    console.log(content);

}

var content = fs.readFile("archivo.txt","utf8", imprimir)//en vez de crear la funcion aqui
//ejecuta primero el da abajo
console.log("\nHaciendo cafe para leer villancico\n");
console.log(process.uptime());