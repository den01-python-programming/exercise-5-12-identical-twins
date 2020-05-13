import pytest
import os

def test_exercise():
    os.chdir('src')

    from simple_date import SimpleDate
    from person import Person

    date = SimpleDate(22, 4, 2016)
    date2 = SimpleDate(21, 6, 2015)

    leo = Person("Leo", date, 62, 9)
    lily = Person("Lily", date2, 65, 8)

    assert not leo == lily

    leo_with_different_weight = Person("Leo", date, 62, 10)

    assert not leo == leo_with_different_weight
