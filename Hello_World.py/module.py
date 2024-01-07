import data
class Weather:
    def __init__(self):
        self.__parameter = data.lst
    def __contains__(self, item):
        return True if item in self.__parameter else False
