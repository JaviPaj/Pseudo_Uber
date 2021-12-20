public class UberBlack extends Car {
    
    String typecaraccepted;
    String seatsmaterial;
    public UberBlack(String license, Account driver, String typecaraccepted, String seatsmaterial) {
        super(license, driver);
        this.typecaraccepted = typecaraccepted;
        this.seatsmaterial = seatsmaterial;
    }
}
