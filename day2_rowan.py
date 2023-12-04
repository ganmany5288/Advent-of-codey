sum_ = 0
sum_powers = 0
red = 12
green = 13
blue = 14
failed = False
inside_sum = 1
lowest = 0
highest_red = 0
highest_blue = 0
highest_green = 0

file_open = open("day2_values.txt")

for colluom in file_open:
    col = colluom.split(":")
    
    game_num = col[0].split()
    game_num = int(game_num[1])
    
    
    col = col[1]

    first = True

    col = col.split(";")
    for inside_col in col:
        inside_col = inside_col.split(",")
        for inside_colour in inside_col:
            inside_colour = inside_colour.split()
            if inside_colour[1] == "red":
                if int(inside_colour[0]) > red:
                   failed = True
                if first:
                    highest_red = int(inside_colour[0])
                elif highest_red < int(inside_colour[0]):
                    highest_red = int(inside_colour[0])
            if inside_colour[1] == "green":
                if int(inside_colour[0]) > green:
                    failed = True
                if first:
                    highest_green = int(inside_colour[0])
                elif highest_green < int(inside_colour[0]):
                    highest_green = int(inside_colour[0])
            if inside_colour[1] == "blue":
                if int(inside_colour[0]) > blue:
                    failed = True
                if first:
                    highest_blue = int(inside_colour[0])
                elif highest_blue < int(inside_colour[0]):
                    highest_blue = int(inside_colour[0])

        if first:
            lowest = inside_sum
            first = False
        elif not first:
            if lowest > inside_sum:
                lowest = inside_sum
        inside_sum = 1
    
    


    
    sum_powers += (highest_blue * highest_red * highest_green)
    highest_blue = 0
    highest_red = 0
    highest_green = 0
    lowest = 0
    first = True

        






    if not failed:
        sum_ += game_num
    failed = False

print(sum_)
print(sum_powers)




file_open.close()
