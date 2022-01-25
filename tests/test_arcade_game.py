from scripts.arcade_game import *


def test_eat_ghost_returns_false():
    assert eat_ghost(False, True) == False


def test_eat_ghost_returns_true():
    assert eat_ghost(True, True) == True


def test_score_returns_true():
    assert score(True, True) == True


def test_score_returns_true_when_true_false():
    assert score(False, True) == True


def test_score_returns_true_when_true_false():
    assert score(True, False) == True


def test_score_returns_false():
    assert score(False, False) == False


def test_lose_returns_true_if_ghost_ifnot_power_pallet():
    assert lose(False, True) == True


def test_lose_returns_false_if_ghost_if_powerpallet():
    assert lose(True, True) == False


def test_lose_returns_false_if_not_ghost_if_not_power_pallet():
    assert lose(False, False) == False


def test_win_returns_false():
    assert win(False, True, False) == False


def test_win_returns_true():
    assert win(True, True, False) == True


def test_win_returns_true():
    assert win(True, True, True) == True
