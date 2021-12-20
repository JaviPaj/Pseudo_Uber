public class UberVan extends Car {
    
    String tytpecaraccepted;
    String seatsmaterial;
    public UberVan(String license, Account driver, String tytpecaraccepted, String seatsmaterial) {
        super(license, driver);
        this.tytpecaraccepted = tytpecaraccepted;
        this.seatsmaterial = seatsmaterial;
    }
}
