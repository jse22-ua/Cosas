const { getRandomNumber } = require("../Random.js");

class Vacio {

  constructor() {

    this.mina = false;
    this.alimento = false;
    this.simbolo = " ";
    let contenido = getRandomNumber(100);

    if (contenido >= 60 && contenido < 80) {

      this.mina = true;
      this.simbolo = "M";

    }
    else if (contenido >= 80) {

      this.alimento = true;
      this.simbolo = "A";

    }

  }

}

module.exports = Vacio;
