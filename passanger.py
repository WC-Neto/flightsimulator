from person import Person


class Passanger(Person):
    def __init__(self, name: str, person_id: str, age: int, adress: str):
        super().__init__(name, person_id, age)
        self.__adress = adress

    @property
    def _adress(self):
        return self.__adress

    @_adress.setter
    def _adress(self, value):
        self.__adress = value

    @property
    def _ticket(self):
        return self.__ticket

    @_ticket.setter
    def _ticket(self, value):
        self.__ticket = value
