from icecream import ic
from dataclasses import dataclass
'''
name, phone, email, address
'''


@dataclass
class Contacts:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def to_string(self):
        ic(f'{self.name}, {self.phone}, {self.email}, {self.address}')

    @staticmethod
    def set_contact() -> object:
        return Contacts(input('name: '), input('phone: '), input('email: '), input('address: '))

    @staticmethod
    def get_contact(ls):
        for i in ls:
            i.to_string()

    @staticmethod
    def del_contact(contacts, name):
        for i, val in enumerate(contacts):
            if name == val.name:
                del contacts[i]
                # contacts.pop(i)
                break





