from person import Person

class Passenger(Person):
    def __init__(self, name: str, person_id: str, age: int, adress: str):
        super().__init__(name, person_id, age)
        self.__adress = adress
        self.seat_assignment = None

    # --- Properties ---
    @property
    def adress(self):
        return self.__adress

    @adress.setter
    def adress(self, value):
        self.__adress = value

    # --- Método Estático para gerar múltiplos passageiros ---
    @staticmethod
    def generate_multiple_passengers(count: int, faker_instance) -> list:
        """
        Gera uma lista de passageiros únicos usando a biblioteca Faker.
        """
        import random
        
        passengers = []
        for _ in range(count):
            passenger = Passenger(
                name=faker_instance.name(),
                person_id=faker_instance.cpf(),
                age=random.randint(18, 80),
                adress=faker_instance.address()
            )
            passengers.append(passenger)
        print(f"{len(passengers)} passageiros gerados com sucesso.")
        return passengers
