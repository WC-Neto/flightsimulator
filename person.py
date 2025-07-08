class Person:
    def __init__(self, name, person_id, age):
        self.__name = name
        self.__person_id = person_id
        self.__age = age
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def person_id(self):
        return self.__person_id

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
