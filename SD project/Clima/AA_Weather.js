//se le introduce el puerto de escucha
const random = require('../Random.js');
const fs = require('fs');
const http = require('http')
const server = http.createServer()
const io = require('socket.io')(server)

if (process.argv.length !== 3) {
    console.error('Error: El número de argumentos es incorrecto');
    console.error('Debe indicar el puerto de escucha del servidor');
    console.error('ejemplo: node AA_Weather.js 5000');
    process.exit(1);
}

io.on('connection', (socket) => {
  console.log('Un cliente se ha conectado');

  socket.on('mensaje', (data) => {
    console.log(`Mensaje recibido: ${data}`);
    
    io.emit('mensaje', data);
  });

  socket.on('disconnect', () => {
    console.log('Un cliente se ha desconectado')
  });
});

server.listen(3000, () => {
  console.log('El servidor de sockets está funcionando en el puerto 3000');
});


function returnCities() {
    let content = fs.readFileSync('Ciudades.txt', 'utf-8');

    let cities = content.split('\n');
    let random_cities = [];
    for (i = 0; i < 4; i++) {
        const ind = random.getRandomNumber(cities.length - 1);
        random_cities.push(cities[ind]);
        cities.splice(ind, 1);
    }

    return random_cities;
}

