import pytest
from src.simple_date import SimpleDate
from src.person import Person

def test_exercise():
    date = SimpleDate(22, 4, 2016)
    date2 = SimpleDate(21, 6, 2015)

    leo = Person("Leo", date, 62, 9)
    lily = Person("Lily", date2, 65, 8)

    assert not leo == lily

    leo_with_different_weight = Person("Leo", date, 62, 10)

    assert not leo == leo_with_different_weight
