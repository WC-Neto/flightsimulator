import random
from faker import Faker
import uuid
from passanger import Passanger
from airplane import Airplane

# Inicializando o Faker para gerar dados falsos
fake = Faker('pt_BR')


def generate_passengers(count: int) -> list[Passanger]:
    """Gera uma lista de passageiros únicos."""
    passengers = []
    for _ in range(count):
        passenger = Passanger(
            name=fake.name(),
            person_id=fake.cpf(),
            age=random.randint(18, 80),
            adress=fake.address()
        )
        passengers.append(passenger)
    print(f"{len(passengers)} passageiros gerados com sucesso.")
    return passengers


def generate_airplanes(count: int) -> list[Airplane]:
    """Gera uma lista de aviões."""
    airplanes = []
    models = ['Boeing 737', 'Airbus A320', 'Embraer E195', 'Boeing 787']
    for i in range(count):
        airplane = Airplane(
            model=random.choice(models),
            # fatiamento para deixar as id's mais legiveis ao usuário.
            airplane_id=f"FLIGHT-{str(uuid.uuid4())[:4]}"
        )
        airplanes.append(airplane)
    print(f"{len(airplanes)} aviões gerados com sucesso.")
    return airplanes


def allocate_passengers(passengers: list[Passanger], airplanes: list[Airplane], passengers_per_plane: int):
    """Aloca passageiros nos aviões de forma aleatória e sem repetição."""
    print("\nIniciando alocação de passageiros...")

    # Embaralha a lista de passageiros para garantir a aleatoriedade
    random.shuffle(passengers)

    passenger_index = 0
    for airplane in airplanes:
        passengers_for_this_flight = passengers[passenger_index:
                                                passenger_index + passengers_per_plane]
        airplane.passengers.extend(passengers_for_this_flight)
        passenger_index += passengers_per_plane
        print(
            f"Alocados {len(airplane.passengers)} passageiros no avião {airplane._airplane_id}.")


def display_flight_allocations(airplanes: list[Airplane], num_samples: int = 10):
    """Exibe uma amostra aleatória de passageiros para cada voo."""
    print("\n--- Verificação da Alocação dos Voos ---")
    for i, airplane in enumerate(airplanes, 1):
        print(
            f"\n--- Voo {i}: Avião {airplane._model} (ID: {airplane._airplane_id}) ---")
        print(f"Total de passageiros a bordo: {len(airplane.passengers)}")

        if len(airplane.passengers) >= num_samples:
            # Pega uma amostra aleatória de 10 passageiros deste voo
            sample_passengers = random.sample(airplane.passengers, num_samples)
            print(f"Amostra de {num_samples} passageiros:")
            for passenger in sample_passengers:
                print(f"  - {passenger._name}")
        else:
            print("Não há passageiros suficientes para exibir uma amostra.")


# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    PASSENGERS_TOTAL = 2500
    AIRPLANES_TOTAL = 10
    PASSENGERS_PER_PLANE = 250

    print("Iniciando a simulação de voos...")

    all_passengers = generate_passengers(PASSENGERS_TOTAL)
    all_airplanes = generate_airplanes(AIRPLANES_TOTAL)

    allocate_passengers(all_passengers, all_airplanes, PASSENGERS_PER_PLANE)

    display_flight_allocations(all_airplanes, num_samples=10)
