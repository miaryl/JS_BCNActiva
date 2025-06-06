class Tenda {
 //for clean code, keep these order 
  //Atributs
  nom = "";
  horariApertura = 0;
  horariTancament = 0;

  //Constructors
  constructor(nom, horariApertura, horariTancament){
    this.nom = nom;
    this.horariApertura = horariApertura;
    this.horariTancament = horariTancament;

  }

  //Getter
  getNom(){
    return this.nom;
  }
  getHorariApertura(){
    return this.horariApertura;
  }
  getHorariTancament(){
    return this.horariTancament;
  }

  //Setter
  setNom(nom){
    this.nom = nom;
  }
  setHorariApertura(horariApertura){
    this.horariApertura = horariApertura;
  }
  setHorariTancament(horariTancament){
    this.horariTancament = horariTancament;
  }

  //Mètodes Generals

  //Mètodes propis
  toString(){
    return "Soc una tenda anomenada " + this.nom + " que obro de " + this.horariApertura + " h fins " + this.horariTancament + " h."
  }
}