from Calculator import add, sub, div


def test_add():
    assert 6 == add(1, 5)
    assert 10 == add(5, 5)


def test_sub():
    assert 10 == sub(15, 5)
    assert 1 == sub(9, 8)


def test_div():
    assert 10 == div(20, 2)
    assert 2 == div(8, 4)
