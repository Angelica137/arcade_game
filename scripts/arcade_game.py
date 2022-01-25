def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Tells us if Pac-Man eats ghost
    """
    if power_pellet_active and touching_ghost:
        return True
    return False


def score(touching_pallet: bool, touching_dot: bool) -> bool:
    """
    Tells us if user has scored
                """
    if touching_pallet or touching_dot:
        return True
    return False


def lose(power_pallet_active: bool, touching_ghost: bool) -> bool:
    """
    Tells us if the user has lost
    """
    if not power_pallet_active and touching_ghost:
        return True
    return False
