public class UberPool extends Car {
    
    String brand;
    Integer model;
    public UberPool(String license, Account driver, String brand, Integer model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;
    } 
}
