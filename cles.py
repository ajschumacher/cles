"""Common-Language Effect Size"""


def cles(lessers, greaters):
    """Common-Language Effect Size

    Probability that a random draw from `greater` is in fact greater
    than a random draw from `lesser`.

    Args:
      lesser, greater: Iterables of comparables.
    """
    if not lessers or not greaters:
        raise ValueError('Both arguments must be non-empty')
    numerator = 0
    lessers, greaters = sorted(lessers), sorted(greaters)
    lesser_index = 0
    for greater in greaters:
        while lesser_index < len(lessers) and lessers[lesser_index] < greater:
            lesser_index += 1
        numerator += lesser_index  # the count less than the greater
    denominator = len(lessers) * len(greaters)
    return float(numerator) / denominator
