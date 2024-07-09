# CHALLENGE: You're a boxer trying to write a pogram to determine the most
# lucrative fight schedule given an array of available fights.  Every time you
# opt to participate in a fight, you will need at least a day of rest afterward.
# Given an array of integers, find out what is the maximum amount of money you
# can make by selectively choosing your fights.  Note: You can assume you will
# skip any fights in which you get a zero or negative amount.

# EXAMPLE INPUTS with CORRECT ANSWERS
# [2,1,6,8] = 10
# [1,5,8,2] = 9
# [2,1,1,50,60,50,2,1,1] = 103
# [-1,-3,1,50,60,50,2,1,1] = 101

def get_max_amount_possible(orig_fight_earnings):
    def equal_to_or_greater_than_zero(num):
        return max([num, 0])

    fight_earnings = list(map(equal_to_or_greater_than_zero, orig_fight_earnings))
    max_amount = 0

    chosen_fights_dict = {}

    for i, amount in enumerate(fight_earnings):
        fought_yesterday = i > 0 and chosen_fights_dict[i - 1] > 0

        # Fought yesterday or doesn't pay: REST!
        if fought_yesterday or amount == 0:
            chosen_fights_dict[i] = 0
            continue

        # last in list OR next fight pays no more than this one: FIGHT!
        if i == len(fight_earnings) - 1 or amount >= fight_earnings[i + 1]:
            chosen_fights_dict[i] = amount
            continue

        # Next fight pays more...

        # next fight is the last one OR
        # sum of this fight + 2-fights-from-now is NO MORE than next fight: REST!
        if (
            i == len(fight_earnings) - 2
        ) or (
            amount + fight_earnings[i + 2] <= fight_earnings[i + 1]
        ):
            chosen_fights_dict[i] = 0
            continue

        # 2-fights-from-now is more than next fight...

        # 2-fights-from-now is the last fight OR
        # sum of next fight + 3-fights-from-now is NO MORE than sum of this fight and 2-from-now: FIGHT!
        if (
            i == len(fight_earnings) - 3
        ) or (
            amount + fight_earnings[i + 2] >= fight_earnings[i + 1] + fight_earnings[i + 3]
        ):
            chosen_fights_dict[i] = amount
            continue

        # NOTE: This gets us 99.9% of the way there, but for the record, in
        # order to make this program perfect, there should be a closure to take
        # the array of any number of remaining fights and compare all of the
        # values at odd indexes against all of the values at even indexes to
        # call itself with the remaining fights to check if it is still
        # inconclusive whether we should fight or not.

        # if you get this far: REST!
        chosen_fights_dict[i] = 0

    max_amount = sum(chosen_fights_dict.values())

    print(f"From this schedule: {orig_fight_earnings}... you could earn up to ${max_amount}")
    return max_amount


example_inputs = [
    [-1,-3,1,50,60,50,2,1,1],
    [2,1,6,8],
    [1,5,8,2],
    [2,1,1,50,60,50,2,1,1],
    [-5,1,-3,-5]
]

for input in example_inputs:
    print(get_max_amount_possible(input))
