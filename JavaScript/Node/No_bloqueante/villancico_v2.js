//no blockeante
var fs = require("fs");

console.log("\nAbriendo Archivo...");

var content = fs.readFile("archivo.txt","utf8", function(error,content){//callback 
console.log(content)
});
//ejecuta primero el da abajo
console.log("\nHaciendo cafe para leer villancico\n");
console.log(process.uptime());