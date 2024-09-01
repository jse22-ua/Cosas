def eat_ghost(power,touching_ghost):
    return power and touching_ghost

def score(power,touching_dot):
    return power or touching_dot

def lose(power, touching_ghost):
    return not power and touching_ghost

def win(all, power, touching_ghost):
    return all and not lose(power,touching_ghost)
