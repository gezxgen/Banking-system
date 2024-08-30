from getters import *


def test_validate_n_valid():
    assert validate("JohnDoe", "n")
    assert validate("Kevin", "n")
    assert validate("Anatol", "n")


def test_validate_n_invalid():
    assert not validate("", "n")
    assert not validate("John123", "n")
    assert not validate("A_JohnDoe", "n")
    assert not validate("JohnDoeJohnDoeJohnDoe", "n")


def test_validate_a_valid():
    assert validate("25", "a")
    assert validate("0", "a")
    assert validate("120", "a")


def test_validate_a_invalid():
    assert not validate("-1", "a")
    assert not validate("121", "a")
    assert not validate("abc", "a")
    assert not validate("25.5", "a")


def test_validate_p_valid():
    assert validate("Passw0rd!", "p")
    assert validate("P@ssw0rd", "p")


def test_validate_p_invalid():
    assert not validate("password", "p")
    assert not validate("PASSWORD", "p")
    assert not validate("12345678", "p")
    assert not validate("P@ss", "p")


def test_validate_b_valid():
    assert validate("1000", "b")
    assert validate("9999", "b")
    assert validate("0", "b")


def test_validate_b_invalid():
    assert not validate("-1", "b")
    assert not validate("10001", "b")
    assert not validate("abc", "b")


def test_validate_d_valid():
    assert validate("5000", "d")
    assert validate("0", "d")
    assert validate("9999", "d")


def test_validate_d_invalid():
    assert not validate("-1", "d")
    assert not validate("10001", "d")
    assert not validate("abc", "d")


def test_validate_w_valid():
    assert validate("5000", "w")
    assert validate("0", "w")
    assert validate("9999", "w")


def test_validate_w_invalid():
    assert not validate("-1", "w")
    assert not validate("10001", "w")
    assert not validate("abc", "w")


def test_validate_num_valid():
    assert validate_num("5000")
    assert validate_num("0")
    assert validate_num("9999")


def test_validate_num_invalid():
    assert not validate_num("-1")
    assert not validate_num("10001")
    assert not validate_num("abc")
