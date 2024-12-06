import numpy as np

with open('/Users/monikaidzik/code/AdventOfCode2024/Day06/input.txt', 'r') as f:
    data = f.read().splitlines()  

maze = []
for line in data:
    maze.append(list(line))

maze_array=np.array([np.array(i) for i in maze])
x, y = np.where(maze_array == "^")
start_idx=x[0]
start_idy=y[0]
start_indeces= str(start_idx)+" "+str(start_idy)+"up"
print(start_idx, start_idy)


how_many_loops = 0
how_many_ignored = 0
for i in range(maze_array.shape[0]):
    for j in range(maze_array.shape[1]):
        counter = 0
        #print(i,j)
        set_of_indeces = set()
        set_of_indeces.add(start_indeces)
        go_up = True
        go_right = False
        go_down = False
        go_left = False
        looping=True
        new_maze_array = np.copy(maze_array)
        x_field = start_idx
        y_field = start_idy
        if not (i==start_idx and j==start_idy):
            new_maze_array[i][j] = "#"
        #print(new_maze_array[i][j])
        while looping:
            counter += 1
            if go_up:
                if new_maze_array[x_field - 1][y_field] != "#" :
                    #lengths[k] += 1
                    if (x_field-1) == 0:
                        looping=False
                        set_of_indeces.add(str(x_field)+" "+str(y_field)+"up")
                        #set_of_indeces.add(str(x_field-1)+" "+str(y_field)+"up")
                    else:
                        set_of_indeces.add(str(x_field)+" "+str(y_field)+"up")
                    x_field -=1  
                else:
                    go_up = False
                    go_right = True
                    if(str(x_field)+" "+str(y_field)+"up" in set_of_indeces):
                        how_many_loops += 1
                        looping = False
                    #k+=1
            if go_right:
                if new_maze_array[x_field][y_field+1] != "#" :
                    if (y_field+1) == new_maze_array.shape[0]-1:
                        looping=False
                        set_of_indeces.add(str(x_field)+" "+str(y_field)+"right")
                        #set_of_indeces.add(str(x_field)+" "+str(y_field+1)+"right")
                    else:
                        set_of_indeces.add(str(x_field)+" "+str(y_field)+"right")
                        
                    y_field +=1
                else:
                    go_right = False
                    go_down = True
                    if(str(x_field)+" "+str(y_field)+"right" in set_of_indeces):
                        how_many_loops += 1
                        looping = False
            if go_down:
                if new_maze_array[x_field+1][y_field] != "#" :
                    if (x_field+1) == new_maze_array.shape[0]-1:
                        looping=False
                        set_of_indeces.add(str(x_field)+" "+str(y_field)+"down")
                        #set_of_indeces.add(str(x_field+1)+" "+str(y_field)+"down")
                    else:
                        set_of_indeces.add(str(x_field)+" "+str(y_field)+"down")
                    x_field +=1
                else:
                    go_down = False
                    go_left = True
                    if(str(x_field)+" "+str(y_field)+"down" in set_of_indeces):
                        how_many_loops += 1
                        looping = False
            if go_left:
                #print(new_maze_array[x_field][y_field], x_field, y_field, i, j)
                if new_maze_array[x_field][y_field-1] != "#" :
                    if (y_field-1) == 0:
                        looping=False
                        set_of_indeces.add(str(x_field)+" "+str(y_field)+"left")
                        #set_of_indeces.add(str(x_field)+" "+str(y_field-1)+"left")
                    else:
                        set_of_indeces.add(str(x_field)+" "+str(y_field)+"left")
                    y_field -=1
                else:
                    go_left = False
                    go_up = True
                    if(str(x_field)+" "+str(y_field)+"left" in set_of_indeces):
                        how_many_loops += 1
                        looping = False
            if counter > 100000:
                print("oops, too much!")
                how_many_ignored += 1
                looping = False
                    

print(how_many_loops)
print(how_many_ignored) # 1663
