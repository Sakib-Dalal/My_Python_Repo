from abc import ABC, abstractmethod
class Character(ABC):
    @abstractmethod
    def patriotism(self):
        print("IN Character")

class Actor:
    def style(self):
        print("In Actor")

class Person(Character, Actor):
    def do_acting(self):
        pass

    def style(self):
        print("In Person")
    def patriotism(self):
        print("In Person")

p = Person()
p.patriotism()
a = Actor()
a.style()