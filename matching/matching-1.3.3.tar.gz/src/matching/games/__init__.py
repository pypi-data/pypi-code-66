""" Make the games and their algorithms accessible. """

from .hospital_resident import HospitalResident, hospital_resident
from .stable_marriage import StableMarriage, stable_marriage
from .stable_roommates import StableRoommates, stable_roommates
from .student_allocation import StudentAllocation, student_allocation

__all__ = [
    HospitalResident,
    StableMarriage,
    StableRoommates,
    StudentAllocation,
    hospital_resident,
    stable_marriage,
    stable_roommates,
    student_allocation,
]
