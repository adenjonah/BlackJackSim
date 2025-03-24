from enum import Enum, auto

class PlayOptions(Enum):
    STAY = 1
    HIT = 2
    DOUBLE = 3
    SURRENDER = 5
    SPLIT = 4

hardHand2CardLookup = [
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT],
    [PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

hardHandLookup = [
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

softHand2CardLookup = [
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

softHandLookup = [
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.HIT, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

pairHandLookup = [
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.DOUBLE, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.HIT, PlayOptions.HIT, PlayOptions.HIT],
    [PlayOptions.HIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT],
    [PlayOptions.STAY, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.STAY, PlayOptions.SPLIT, PlayOptions.SPLIT, PlayOptions.STAY],
    [PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY, PlayOptions.STAY],
]

def getBet(true_count, style, max_units):

    
    if style == 'Max_EV':
        if true_count < 2:
            return 1
        else:
            return max_units

    else:
        if true_count < 1:
            return 1
        elif true_count < 2:
            return .2 * max_units
        elif true_count < 3:
            return .4 * max_units
        elif true_count < 4:
            return .6 * max_units
        elif true_count < 5:
            return .8 * max_units
        elif true_count < 6:
            return .9 * max_units
        else:
            return max_units