from scripts.arcade_game import *


def test_eat_ghost_returns_false():
    assert eat_ghost(False, True) == False


def test_eat_ghost_returns_true():
    assert eat_ghost(True, True) == True


def test_score_returns_true():
    assert score(True, True) == True
