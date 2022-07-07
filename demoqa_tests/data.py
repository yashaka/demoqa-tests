from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    subjects: list[str]


'''
class User:
    foo = 'bar'

    def __init__(self, first_name: str, last_name: str, subjects: list[str]):
        self.first_name = first_name
        self.last_name = last_name
        self.subjects = subjects
'''
