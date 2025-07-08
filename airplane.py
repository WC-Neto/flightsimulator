import random
import uuid
from seat import Seat 

class Airplane:
    def __init__(self, model, airplane_id, capacity: int = 250):
        self.__model = model
        self.__airplane_id = airplane_id
        self.passengers = []
        self.crew = []
        self.seats = self._generate_seats(capacity)

    def _generate_seats(self, capacity: int) -> list[Seat]:
        """Método privado para gerar os assentos do avião."""
        seats = []
        rows = (capacity // 6) + 1
        for row in range(1, rows + 1):
            for letter in "ABCDEF":
                if len(seats) < capacity:
                    seats.append(Seat(f"{row}{letter}"))
        return seats

    def get_available_seat(self) -> Seat | None:
        """Encontra e retorna um assento disponível."""
        for seat in self.seats:
            if not seat.is_occupied:
                return seat
        return None

    # --- Properties ---
    @property
    def model(self):
        return self.__model

    @property
    def airplane_id(self):
        return self.__airplane_id

    # --- Métodos de Instância ---
    def add_crew_member(self, crew_member):
        self.crew.append(crew_member)

    def add_passenger(self, passenger, seat: Seat):
        """Adiciona um passageiro e atribui um assento a ele."""
        seat.occupy()
        passenger.seat_assignment = seat
        self.passengers.append(passenger)

    # --- Método Estático para gerar múltiplos aviões ---
    @staticmethod
    def generate_multiple_airplanes(count: int) -> list:
        """Gera uma lista de aviões com modelos e IDs aleatórios."""
        airplanes = []
        models = ['Boeing 737', 'Airbus A320', 'Embraer E195', 'Boeing 787']
        for i in range(count):
            airplane = Airplane(
                model=random.choice(models),
                airplane_id=f"FLIGHT-{str(uuid.uuid4())[:4]}"
            )
            airplanes.append(airplane)
        print(f"{len(airplanes)} aviões gerados com sucesso.")
        return airplanes

