from faker import Faker
fake = Faker()


class Airfare:
    def __init__(self):
        self.__name = fake.name()
        self.__airfare_id = fake.uuid4()[:4]
        self.__destino = fake.country()

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _airfare_id(self):
        return self.__airfare_id

    @property
    def _destino(self):
        return self.__destino

    @_destino.setter
    def _destino(self, value):
        self.__destino = value

    def create(self):
        new_user = Airfare()
        return (print(new_user))

    def read(airfare_id):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def fly(self):
        pass


new_airfare = Airfare()
print(
    f'Nova passagem gerada para {new_airfare._name}, com código {new_airfare._airfare_id} com destino a {new_airfare._destino}')
