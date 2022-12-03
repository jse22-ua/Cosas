//bloqueante
var fs = require("fs")

console.log("\nAbriendo Archivo...")

var content = fs.readFileSync("archivo.txt","utf8")
console.log(content)
//espero a que se ejecute fs.readFile...
console.log("\nHaciendo cafe para leer villancico\n")
console.log(process.uptime())