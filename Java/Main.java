class Main {
    public static void main(String[] args) {
        System.out.println("Aqui estoy con Java");
        Car car = new Car("AQY985", new Account("Asdrual Duarte", "COL89"));
        car.passenger   = 4;
        car.showDatacar();

        Car car1 = new Car("UJH746", new Account("Anibal Smith", "CUN64"));
        car1.passenger   = 3;
        car1.showDatacar();
    
        /*Correr para ver en la terminal*/
    }
}
