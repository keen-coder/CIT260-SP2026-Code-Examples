
class Person:
    def __init__(self, name, age, hair_color):
        self.__name = name
        self.__age = age
        self.__hair_color = hair_color

    def get_name(self):
        return self.__name
    
    def __str__(self):
        output = f'Name: {self.__name}\n'
        output += f'Age: {self.__age}\n'
        output += f'Hair Color: {self.__hair_color}'

        return output