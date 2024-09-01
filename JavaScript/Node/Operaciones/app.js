/*console.log('Hola');
console.warn('ocurrio un error');
console.error('Menudo error');//lo muestra por pantalla

console.error(new Error('De verdad no puedo contigo,tonto'));
salta error con ese nombre
*/

//console.log(process);//descripcion de none y el proceso que se esta ejecutando

//para conocer los parametros que se pasan por consola se utiliza process.argv
const os = require('os');

console.log(process.argv)

if(process.argv.length>1){
    console.log(process.argv[2]); //porque 0 es node y 1 es app.js 1

    for(let i = 2;i < process.argv.length; i++){
        console.log(process.argv[i]);
    }
}

console.log(os.type());
console.log(os.homedir());
console.log(os.uptime());//el tiempo que ha estado ejecutandose el sistema operativo
console.log(os.userInfo());

