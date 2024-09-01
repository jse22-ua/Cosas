const io = require('socket.io-client');
const socket = io('http://localhost:3000');

socket.on('mensaje', (data) => {
  console.log(`Mensaje recibido: ${data}`);
});

socket.emit('mensaje', 'Hola, servidor!');
