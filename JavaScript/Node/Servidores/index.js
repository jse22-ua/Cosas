/*
const http = require('http');
const colors = require('colors')

const handleServer = function(req,response){//req es la peticion y response es la respuesta 
    response.writeHead(200,{'Content-type': 'text/html'});
    response.write('<h1>Hola Mundo</h1>');
    response.end(); //termina el contacto con el cliente para seguir recibiendo peticiones
}

const server =http.createServer(handleServer); //puerto

server.listen(3000, function(){
    console.log('Server on port 3000'.yellow);
})*/

const colors = require('colors');
const express = require('express');//con express te ahorras el http

const server = express();

server.get('/',(req,res)=>{
    res.send('<h1>Hola mundo</h1>');
})

server.listen(3000, () => {
    console.log('Server on port 3000'.green);
})