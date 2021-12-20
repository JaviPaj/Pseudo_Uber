class Card extends Payment(){
    constructor(id, cardBank, cvv){
        super(id)
        this.cardBank = cardBank;
        this.cvv = cvv;
    }
}