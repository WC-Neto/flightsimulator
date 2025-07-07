class Airplane:
    def __init__(self, model, airplane_id):
        self.__model = model
        self.__airplane_id = airplane_id
        self.passengers = []

    @property
    def _model(self):
        return self.__model

    @_model.setter
    def _model(self, value):
        self.__model = value

    @property
    def _airplane_id(self):
        return self.__airplane_id

    @_airplane_id.setter
    def _airplane_id(self, value):
        self.__airplane_id = value

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def fly(self):
        pass
