class Query:
    def __init__(self):
        self.__parameters = {}

    def add(self, key, value):
        self.__parameters[key] = value

    def get(self, key):
        return self.__parameters[key]    