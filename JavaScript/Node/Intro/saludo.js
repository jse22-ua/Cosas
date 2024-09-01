function saludar(nombre){
  return `Hola ${nombre}`;
}

function hello(){
  return "Hola mundo";
}

//module.exports.saludar = saludar;

//console.log(module.exports);

module.exports = {
  saludar : saludar,
  hello : hello
};