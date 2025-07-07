class Airline:
    def __init__(self, name, airline_id):
        self.__name = name
        self.__airline_id = airline_id

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _airline_id(self):
        return self.__airline_id

    @_airline_id.setter
    def _airline_id(self, value):
        self.__airline_id = value

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
