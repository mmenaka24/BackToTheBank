from bank import value


def test_value_hello():
    assert value("hello") == 0


def test_value_h():
    assert value("hey there") == 20


def test_value_else():
    assert value("what's up") == 100


def test_value_caps():
    assert value("HEY THERE") == 20


def test_value_mixed_case():
    assert value("Hey There") == 20
