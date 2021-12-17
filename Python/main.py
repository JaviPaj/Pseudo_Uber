from car import Car
# desde el archivo importo la clase

if __name__ == "__main__":
    print('Aqui estoy con PY')
    
    # Seguido se crearan los objets car instanciando la clase Car.
    car = Car()
    car.license = "WQE785"
    car.driver = "Anibal Vasquez"
    print(vars(car))

    car1 = Car()
    car1.license = "OPD165"
    car1.driver = "Oscar Duarte"
    print(vars(car1))
