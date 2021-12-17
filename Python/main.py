# desde el archivo importo las clases
from car import Car
from account import Account

if __name__ == "__main__":
    print('Aqui estoy con PY')
    
    # Seguido se crearan los métodos constructores.
    car = Car("WQE785", Account("Anibal Vasquez", "COL34"))
    print(vars(car))
    print(vars(car.driver))
