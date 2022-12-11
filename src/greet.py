from typing import Optional
from pprint import pprint

class Greetings(object):
    def __init__(self, name: str, address: Optional[str]=None, city: Optional[str]=None, state: Optional[str]=None,):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
    
    def intro(self):
        """introduce yourself in informal event
        """
        print("Hello My name is {}, Nice to meet You".format(self.name))

    def formal_event(self):
        """introduce youself in formal event
        """
        if self.address is not None:
            print("Hello Nice to meet you, my name is {} i live in {}, {}, {}".format(self.name, self.address, self.city, self.state))
        else:
            print("Hello Nice to meet you, my name is {} Nice to Meet Yo Bro")

    def identity(self):
        """Print your identity
        """

        data_dict: dict[str, str] = {
            "name": self.name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
        }
        print("here your identity")
        pprint(data_dict)

    