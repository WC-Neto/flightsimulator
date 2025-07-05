class Person:
    def __init__(self, name, person_id, age):
        self.__name = name
        self.__person_id = person_id
        self.__age = age

    @property
    def _name(self):
        return self.__name

    @_name.setter
    def _name(self, value):
        self.__name = value

    @property
    def _person_id(self):
        return self.__person_id

    @_person_id.setter
    def _person_id(self, value):
        self.__person_id = value

    @property
    def _age(self):
        return self.__age

    @_age.setter
    def _age(self, value):
        self.__age = value
