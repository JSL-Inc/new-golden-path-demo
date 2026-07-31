from testing.calculator import add, subtract


def test_add() -> None:
    assert add(2, 3) == 5


def test_subtract() -> None:
    assert subtract(5, 3) == 2


def test_intentional_failure():
    assert add(1, 1) == 3
