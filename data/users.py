from dataclasses import dataclass
from typing import List, Literal

from faker import Faker

from practice.utils.utils import RussiaPhoneNumberProvider

fake = Faker()
fake.add_provider(RussiaPhoneNumberProvider)


@dataclass
class User:
    firstname: str
    lastname: str
    email: str
    phone: str
    bdate: list
    avatar: str
    address: str
    gender: Literal['Male', 'Female', 'Other']
    subjects: List[Literal['Maths', 'Computer Science', 'English']]
    hobbies: List[Literal['Sports', 'Music', 'Reading']]
    state: Literal['NCR', 'Delhi', 'Uttar Pradesh']
    city: Literal['Lucknow', 'Agra']


Student = User(firstname=fake.name_male(),
                  lastname=fake.last_name_female(),
                  email=fake.email(),
                  gender='Male',
                  phone=fake.russia_phone_number(),
                  subjects=['Maths', 'Computer Science'],
                  hobbies=['Sports', 'Music'],
                  avatar='cat.jpeg',
                  address=fake.street_address(),
                  state='Uttar Pradesh',
                  city='Lucknow',
                  bdate=['12', '3', '2000'])



