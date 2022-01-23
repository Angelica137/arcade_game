def eat_ghost(power_pellet_active: bool, touching_ghost: bool) -> bool:
    """
    Tells us if Pac-Man eats ghost
    """
    if power_pellet_active and touching_ghost:
        return True
    return False
