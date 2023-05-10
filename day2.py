# day2
# A-rock,B-paper, c -scissors
# x-rock, y-paper. z- scissors
f = open("day2_input.txt")
lines = f.read().strip().split("\n")
print(lines)

my_total_points = 0
for round_str in lines:
    print("New round, player 1 and player 2 chose this:")
    print(round_str)
    player_1 = round_str[0]
    print(player_1)
    player_2 = round_str[2]
    print(player_2)

    my_points_for_this_round = 0
    if player_1 == "A" and player_2 == "X":
        print("outcome is a draw")
        my_points_outcome = 3
        my_points_shape = 1
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round

    elif player_1 == "A" and player_2 == "Y":
        print("outcome is a win")
        my_points_outcome = 6
        my_points_shape = 2
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round

    elif player_1 == "A" and player_2 == "Z":
        print("player_1 wins")
        my_points_outcome = 0
        my_points_shape = 3
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round
    elif player_1 == "B" and player_2 == "X":
        print("player_1 wins")
        my_points_outcome = 0
        my_points_shape = 1
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round
    elif player_1 == "B" and player_2 == "Y":
        print("draw")
        my_points_outcome = 3
        my_points_shape = 2
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round
    elif player_1 == "B" and player_2 == "Z":
        print("player_2 wins")
        my_points_outcome = 6
        my_points_shape = 3
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round
    elif player_1 == "C" and player_2 == "X":
        print("player_2 wins")
        my_points_outcome = 6
        my_points_shape = 1
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round
    elif player_1 == "C" and player_2 == "Y":
        print("player_1 wins")
        my_points_outcome = 0
        my_points_shape = 2
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round
    elif player_1 == "C" and player_2 == "Z":
        print("draw")
        my_points_outcome = 3
        my_points_shape = 3
        my_points_for_this_round = my_points_outcome + my_points_shape
        my_total_points = my_total_points + my_points_for_this_round


print(my_total_points)