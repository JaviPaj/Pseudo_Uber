public class UberX extends Car {
   
    String brand;
    Integer model;

    public UberX(String license, Account driver, String brand, Integer model) {
        super(license, driver);
        this.brand = brand;
        this.model = model;
    }
}
