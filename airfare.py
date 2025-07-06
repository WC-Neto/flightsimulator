class Airfare:
    def __init__(self, name: str, airfare_id, destino):
        self.__name = name
        self.__airfare_id = airfare_id
        self.__destino = destino

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _airfare_id(self):
        return self.__airfare_id

    @_airfare_id.setter
    def _airfare_id(self, value):
        self.__airfare_id = value

    @property
    def _destino(self):
        return self.__destino

    @_destino.setter
    def _destino(self, value):
        self.__destino = value

    
    def create():
        pass

    def read():
        pass

    def update():
        pass

    def delete():
        pass
    
    def fly():
        pass