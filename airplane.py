class Airplane:
    def __init__(self, model, airplane_id):
        self.__model = model
        self.__airplane = airplane_id
        

    @property
    def _model(self):
        return self.__model

    @_model.setter
    def _model(self, value):
        self.__model = value

    @property
    def _airplane(self):
        return self.__airplane

    @_airplane.setter
    def _airplane(self, value):
        self.__airplane = value

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