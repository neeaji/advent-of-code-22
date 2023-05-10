f = open("day1_input.txt")

# input_list = f.readlines()

lines = f.read().strip().split("\n")
lines.append('')

elvs = []
sum_calories = 0

for line in lines:
    if line == "":
        # we reached the end of an elv's inventory
        # save the sum of calories to elvs
        elvs.append(sum_calories)
        sum_calories = 0
    else:
        # sum the calories
        calories = int(line)
        sum_calories = sum_calories + calories


print(max(elvs))

# part 2
elvs.sort(reverse=True)
#print(elvs)
top_three_elvs = elvs[:3]
print(sum(top_three_elvs))


