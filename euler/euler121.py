def probability(outcome):
    round = 1
    prob = 1.0
    for color in outcome:
        blue_prob = 1.0 / (round + 1)
        red_prob = 1.0 - blue_prob
        if color == 'blue':
            prob *= blue_prob
        else:
            prob *= red_prob
        round += 1
    return prob

def is_winner(outcome):
    return outcome.count('blue') > outcome.count('red')

def visit_all_outcomes(outcome_so_far, more_rounds, win_probability):
    if more_rounds == 0:
        prob = probability(outcome_so_far)
        if is_winner(outcome_so_far):
            return win_probability + probability(outcome_so_far)
        else:
            return win_probability
    else:
        win_probability = visit_all_outcomes(outcome_so_far + ['red'], more_rounds - 1, win_probability)
        win_probability = visit_all_outcomes(outcome_so_far + ['blue'], more_rounds - 1, win_probability)
        return win_probability

def win_probability(rounds):
    return visit_all_outcomes([], rounds, 0.0)

def max_prize(rounds):
    return int(1.0 / win_probability(rounds))

print max_prize(15)

