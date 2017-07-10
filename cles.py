"""Common-Language Effect Size"""


def cles(lessers, greaters):
    """Common-Language Effect Size

    Probability that a random draw from `greater` is in fact greater
    than a random draw from `lesser`.

    Args:
      lesser, greater: Iterables of comparables.
    """
    if len(lessers) == 0 and len(greaters) == 0:
        raise ValueError('At least one argument must be non-empty')
    # These values are a bit arbitrary, but make some sense.
    # (It might be appropriate to warn for these cases.)
    if len(lessers) == 0:
        return 1
    if len(greaters) == 0:
        return 0
    numerator = 0
    lessers, greaters = sorted(lessers), sorted(greaters)
    lesser_index = 0
    for greater in greaters:
        while lesser_index < len(lessers) and lessers[lesser_index] < greater:
            lesser_index += 1
        numerator += lesser_index  # the count less than the greater
    denominator = len(lessers) * len(greaters)
    return float(numerator) / denominator
