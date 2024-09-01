//ejemplo de setTimeout
function mostrarTema(tema){
    console.log(`Estoy aprendiendo ${tema}`);
}

setTimeout(mostrarTema, 5000,'Node.js');//asincrono
//hace un temporizador que ejecuta la funcion a los 5 segundos

function sumar(a,b){
    console.log(a+b);
}

setTimeout(sumar,2000,5,3);//asincrono
//se ejecuta la funcion a los 2 segundos
//(los argumentos se especifica despues del retraso)

//por lo que como es no bloqueante primero se ejecutara sumar y luego mostrar tema

//ejemplo de setImmediate
function mostrarComida(alimento){
    console.log(`Hoy se va a comer ${alimento}`);
}

console.log('Antes del setImmediate()');//sincrono

setImmediate(mostrarComida,'Arroz');//ejecuta despues del codigo sincrono

console.log('Despues del setImmediate()');//sincrono

//ejemplo de setInterval

function mostrarVideojuego(videojuego){
    console.log(`Mi videojuego favorito es ${videojuego}`);
}

setInterval(mostrarVideojuego,1500,'Kirby');//repite la funcion cada 1,5 minutos infinitamente