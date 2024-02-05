# from dataclasses import dataclass

# @dataclass
# class Person:
#     name: str
#     age: int = 18
#     gender: str = 'male'

# p1 = Person('John')
# print(p1)  # Person(name='John', age=18, gender='male')

# p2 = Person('Jane', 25, 'female')
# print(p2)  # Person(name='Jane', age=25, gender='female')

# -----------------------------------------------------------------------------------------------

# from dataclasses import dataclass, field

# def get_default_age():
#     return 18

# @dataclass
# class Person:
#     name: str
#     age: int = field(default_factory=get_default_age)
#     gender: str = 'male'

# p1 = Person('John')
# print(p1)  # Person(name='John', age=18, gender='male')

# p2 = Person('Jane', gender='female')
# print(p2)  # Person(name='Jane', age=18, gender='female')

# ----------------------------------------------------------------------------------

# from dataclasses import dataclass


# @dataclass(frozen=True)
# class Person:
#     name: str
#     age: int


# p = Person(name='John', age=30)
# print(p)  # Person(name='John', age=30)

# p.age = 40  # raises an AttributeError: can't set attribute

# ----------------------------------------------------------------------

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int


@dataclass
class Employee(Person):
    id: str
    department: str


e = Employee(name="John", age=30, id="1234", department="Sales")
print(e)  # Employee(name='John', age=30, id='1234', department='Sales')
