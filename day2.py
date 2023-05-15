def decide_outcome(opponent_shape, my_shape):
    """
    :param opponent_shape: str, could be 'A', 'B' or 'C'.
    :param my_shape: str, could be 'X', or 'Y', or 'Z'
    :return: if I win, or lose or draw.
    """
    outcome = ''
    if opponent_shape == 'A' and my_shape == 'Y':
        outcome = "win"
    elif opponent_shape == 'B' and my_shape == 'Y':
        outcome = "draw"
    elif opponent_shape == 'C' and my_shape == 'Z':
        outcome = "draw"
    elif opponent_shape == 'A' and my_shape == 'X':
        outcome = "draw"
    elif opponent_shape == 'A' and my_shape == 'Z':
        outcome = "lose"
    elif opponent_shape == 'B' and my_shape == 'X':
        outcome = "lose"
    elif opponent_shape == 'B' and my_shape == 'Z':
        outcome = "win"
    elif opponent_shape == 'C' and my_shape == 'X':
        outcome = "win"
    elif opponent_shape == 'C' and my_shape == 'Y':
        outcome = "lose"

    return outcome


def compute_outcome_score(my_outcome):
    """
    :param my_outcome: str, 'win', 'lose' or 'draw'
    :return: the score based on the outcome of the round
    """
    # given an outcome
    # return what score I will get, win=6 pts, lose=0 pts, draw=3 pts
    outcome_score = 0
    if my_outcome == 'win':
        outcome_score = 6
    elif my_outcome == 'lose':
        outcome_score = 0
    elif my_outcome == 'draw':
        outcome_score = 3

    return outcome_score


def compute_shape_score(my_shape):
    """
    :param my_shape: str, can be 'X', or 'Y', or 'Z'
    :return: the score I get based on the shape I chose
    """
    shape_score = 0
    if my_shape == 'X':
        shape_score = 1
    elif my_shape == 'Y':
        shape_score = 2
    elif my_shape == 'Z':
        shape_score = 3

    return shape_score


def compute_total_score(outcome_score, shape_score):
    """
    :param outcome_score: integer
    :param shape_score: int
    :return: the sum of the scores
    """
    total_score = outcome_score + shape_score
    return total_score


f = open("day2_input.txt", "r")
input_list = f.read().strip().split("\n")

print(input_list)
total_score_for_all_rounds = 0
for my_input in input_list:
    print('the n-th time in the loop')
    opponent = my_input[0]
    me = my_input[2]
    print(f'opponent chose the shape {opponent}')
    print(f'I chose the shape {me}')

    my_outcome = decide_outcome(opponent, me)
    my_outcome_score = compute_outcome_score(my_outcome)
    my_shape_score = compute_shape_score(me)
    total_for_a_round = compute_total_score(my_outcome_score, my_shape_score)
    total_score_for_all_rounds = total_score_for_all_rounds + total_for_a_round

# compute the final score (sum of all rounds)
print(total_score_for_all_rounds)

