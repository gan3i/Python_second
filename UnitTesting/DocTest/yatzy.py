




def small_straight(dice):
    """ Score the given roll in the "small straight" yatzy category

        >>> small_straight([1,2,3,4,5])
        15
        >>> small_straight([1])
        0

        It doesn't handle sets or unsoted lists
        >>> small_straight({1,2,3,4,5})
        0
        >>> small_straight([2,3,1,4,5])
        0
    """ 
    if dice == [1,2,3,4,5]:
        return sum(dice)
    return 0

# to run with doctest
# python -m doctest yatzy.py -v   -- -v is for verbose
# to run with pytest
# python -m pytest --doctest-modules 

# fucntion to handle sorted list, Doc tests fail of you don't update the docstring with proper examples


def small_straight_sorted(dice):
    """ Score the given roll in the "small straight" yatzy category

        >>> small_straight_sorted([1,2,3,4,5])
        15
        >>> small_straight_sorted([1])
        0

        Now it handles set or unsoted lists
        >>> small_straight_sorted({1,2,3,4,5})
        15
        >>> small_straight_sorted([2,3,1,4,5])
        15
    """ 
    if sorted(dice) == [1,2,3,4,5]:
        return sum(dice)
    return 0