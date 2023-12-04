sum_ = 0
red = 12
green = 13
blue = 14
failed = False

file_open = open("text.txt")

for colluom in file_open:
    col = colluom.split(":")
    
    game_num = col[0].split()
    game_num = int(game_num[1])


    col = col[1]



    col = col.split(";")
    for inside_col in col:
        inside_col = inside_col.split(",")
        for inside_colour in inside_col:
            inside_colour = inside_colour.split()
            if inside_colour[1] == "red":
                if int(inside_colour[0]) > red:
                   failed = True

            if inside_colour[1] == "green":
                if int(inside_colour[0]) > green:
                    failed = True
                    

            if inside_colour[1] == "blue":
                if int(inside_colour[0]) > blue:
                    failed = True
            
    if not failed:
        sum_ += game_num
    failed = False

print(sum_)





file_open.close()
