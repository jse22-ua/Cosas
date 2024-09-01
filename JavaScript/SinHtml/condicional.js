var nota = 7;

console.log("He realizado el examen");

if(nota>=5){
    calificacion = "Suspendido";
}else{
    calificacion = "aprobado";
}

console.log("has", calificacion);

//o

var edad = 45;

console.log("Tu edad es: ", edad);

var comoEres = edad>=18 ? "mayor" : "menor";

console.log("eres ", comoEres, " de edad");

var dia = "miercoles";

console.log("Hoy es ", dia, "luego hay que: ");

switch(dia){
    case "lunes":
        console.log("hacer Mates");
        break;
    case "martes":
        console.log("Ducharse");
        break;
    case "jueves":
        console.log("Visitar a los abuelos");
        break;
    case "miercoles":
        console.log("Minar bitcoin");
        break;
    case "viernes":
        console.log("Saltar a la comba");
        break;
    default:
        console.log("Nada es finde");
        break;
}