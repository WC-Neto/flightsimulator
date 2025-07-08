import random
from faker import Faker

from passenger import Passenger
from airplane import Airplane
from air_crew import Pilot, AirAttendant

def prepare_flights(airplanes: list[Airplane], faker_instance: Faker):
    """Gera e aloca a tripulação para cada avião."""
    print("\n--- Preparando Tripulação para os Voos ---")
    for airplane in airplanes:
        pilot = Pilot(name=faker_instance.name(), person_id=faker_instance.cpf(), age=random.randint(30, 60))
        attendants = [AirAttendant(name=faker_instance.name(), person_id=faker_instance.cpf(), age=random.randint(21, 45)) for _ in range(4)]
        
        airplane.add_crew_member(pilot)
        for attendant in attendants:
            airplane.add_crew_member(attendant)

        print(f"\nTripulação do avião {airplane.airplane_id} se apresentando:")
        for crew_member in airplane.crew:
            crew_member.report_for_duty()

def allocate_passengers(passengers: list[Passenger], airplanes: list[Airplane]):
    """Aloca passageiros e assentos nos aviões de forma aleatória."""
    print("\nIniciando alocação de passageiros e assentos...")
    
    random.shuffle(passengers)
    
    passenger_index = 0
    for airplane in airplanes:
        passengers_for_this_flight = passengers[passenger_index : passenger_index + len(airplane.seats)]
        
        for passenger in passengers_for_this_flight:
            available_seat = airplane.get_available_seat()
            if available_seat:
                airplane.add_passenger(passenger, available_seat)
            else:
                print(f"AVISO: Lotação máxima do avião {airplane.airplane_id} atingida. Passageiro {passenger.name} não pôde embarcar.")
                break 
        
        passenger_index += len(airplane.passengers)
        print(f"Alocados {len(airplane.passengers)} passageiros no avião {airplane.airplane_id}.")

def display_flight_allocations(airplanes: list[Airplane], num_samples: int = 10):
    """Exibe uma amostra aleatória de passageiros e seus assentos para cada voo."""
    print("\n--- Verificação da Alocação dos Voos ---")
    for i, airplane in enumerate(airplanes, 1):
        print(f"\n--- Voo {i}: Avião {airplane.model} (ID: {airplane.airplane_id}) ---")
        print(f"Total de passageiros a bordo: {len(airplane.passengers)}")
        
        if len(airplane.passengers) >= num_samples:
            sample_passengers = random.sample(airplane.passengers, num_samples)
            print(f"Amostra de {num_samples} passageiros e seus assentos:")
            for passenger in sample_passengers:
                print(f"  - Passageiro: {passenger.name}, Assento: {passenger.seat_assignment}")
        else:
            print("Não há passageiros suficientes para exibir uma amostra.")

# --- Ponto de Entrada do Programa ---
if __name__ == "__main__":
    PASSENGERS_TOTAL = 2500
    AIRPLANES_TOTAL = 10
    
    print("Iniciando a simulação de voos...")

    faker_instance = Faker('pt_BR')

    all_passengers = Passenger.generate_multiple_passengers(PASSENGERS_TOTAL, faker_instance)
    all_airplanes = Airplane.generate_multiple_airplanes(AIRPLANES_TOTAL)

    prepare_flights(all_airplanes, faker_instance)
    allocate_passengers(all_passengers, all_airplanes)
    display_flight_allocations(all_airplanes, num_samples=10)
