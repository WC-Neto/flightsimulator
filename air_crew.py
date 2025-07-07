from person import Person


class Pilot(Person):
    def __init__(self, name: str, person_id: str, age: int, func: str):
        super().__init__(name, person_id, age)
        self.__func = func

    @property
    def _func(self):
        return self.__func

    @_func.setter
    def _func(self, value):
        self.__func = value

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass


class AirAttendants(Person):
    def __init__(self, name: str, person_id: str, age: int, func: str):
        super().__init__(name, person_id, age)
        self.__func = func

    @property
    def _func(self):
        return self.__func

    @_func.setter
    def _func(self, value):
        self.__func = value

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
