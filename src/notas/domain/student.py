from dataclasses import dataclass


@dataclass
class Student:
    """Represents a student"""

    full_name: str
    email: str
    padron: int
    group_number: int
