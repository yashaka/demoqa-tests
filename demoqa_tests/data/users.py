import dataclasses


@dataclasses.dataclass
class User:
    full_name: str
    email: str


admin = User(full_name='admina adminovych', email='super+admin@gmail.com')
guest = User('harry', 'potter@hg.com')
