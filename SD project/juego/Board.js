const Vacio = require("./Vacio.js")

class Board{
  constructor(paises){
    this.board = new Map();
    this.paises = paises;
    for(let i = 0; i<20;i++){
      for(let j=0; j<20;j++){
        this.board.set([i,j],new Vacio());
      }
    }
  }

  dibujarMapa(){
    
  }
}

mapa = new Board();