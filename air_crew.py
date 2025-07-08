from person import Person
from airplane_crew_interface import IAirplaneCrew

class Pilot(Person, IAirplaneCrew):
    def __init__(self, name: str, person_id: str, age: int, func: str = "Piloto"):
        super().__init__(name, person_id, age)
        self.__func = func

    @property
    def func(self):
        return self.__func

    def check_credentials(self) -> bool:
        print(f"Verificando licença de voo para o piloto {self.name}...")
        return True

    def report_for_duty(self):
        print(f"Piloto {self.name} se apresentando para o voo.")


class AirAttendant(Person, IAirplaneCrew):
    def __init__(self, name: str, person_id: str, age: int, func: str = "Comissário(a)"):
        super().__init__(name, person_id, age)
        self.__func = func

    @property
    def func(self):
        return self.__func

    def check_credentials(self) -> bool:
        print(f"Verificando certificação de segurança para o comissário(a) {self.name}...")
        return True

    def report_for_duty(self):
        print(f"Comissário(a) {self.name} se apresentando para o serviço.")