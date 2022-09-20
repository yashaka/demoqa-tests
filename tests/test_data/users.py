from dataclasses import dataclass
from enum import Enum
from typing import Tuple


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Pysics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    gender: Gender
    name: str
    last_name: str = 'YouMeanIt'
    email: str = 'abc@efg.com'
    user_number: str = '0123456789'
    birth_day: str = '30'
    birth_month: str = 'September'
    birth_year: str = '1972'
    subjects: Tuple[Subject] = (Subject.History,)
    current_address: str = 'bla bla bla'
    hobbies: Tuple[Hobby] = (Hobby.Sports,)
    picture_file: str = 'photo.jpg'
    state: str = 'Haryana'
    city: str = 'Karnal'


yuri = User(name='yuri', gender=Gender.Male)
