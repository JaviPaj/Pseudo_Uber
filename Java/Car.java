public class Car {
    /*listado de atributos*/
    Integer id;
    String license;
    Account driver;
    Integer passenger;

    /*Creamos un METODO CONSTRUCTOR*/
    public Car(String license, Account driver) {
        this.license = license;
        this.driver = driver;
    }

    /*Se crea un METODO para imprimir*/

    void showDatacar() {
        System.out.println("License: " + license + " Driver name: " + driver.name + " Documetn: "+ driver.document);
    }
}
