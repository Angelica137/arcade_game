def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Tells us if Pac-Man eats ghost
    """
    return power_pellet_active and touching_ghost


def score(touching_pallet: bool, touching_dot: bool) -> bool:
    """
    Tells us if user has scored
    """
    return touching_pallet or touching_dot


def lose(power_pallet_active: bool, touching_ghost: bool) -> bool:
    """
    Tells us if the user has lost
    """
    return not power_pallet_active and touching_ghost


def win(eaten_all_dots: bool, power_pallet_active: bool, touching_ghost: bool) -> bool:
    """
    Tells us if the user has won
    """
    if eaten_all_dots and not lose(power_pallet_active, touching_ghost):
        return True
    return False
