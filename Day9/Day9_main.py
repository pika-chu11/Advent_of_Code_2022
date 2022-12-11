fileName = "test.txt"

# Return 0 if we don't need to move
# Return 1 if we need to move diagonally
# Return 2 if we need to move horizontally or vertically
def check_steps(h_pos, t_pos):
    # Firstly, check the difference of  h_pos - t_pos
    diff = abs(h_pos[0] - t_pos[0]) + abs(h_pos[1] - t_pos[1])
    
    if diff > 2:
        return 2
    elif diff == 0:
        return 1
    # check if they are on the different column and row
    if diff == 0:
        return 1
    elif diff > 2:
        return 1
    else:
        return 0
    
if __name__ == "__main__":
    # Set up
    num_point_travel = 1 # starting point count as 1
    # Both Head and Tail is at the starting point
    H = [0,0]
    T = [0,0]
    # store the points that Tail traveled
    point_travel = [[0,0]]
    
    with open(fileName, "r") as f:
        # string of the line
        line = f.readline()
        while line != '': # The EOF char is an empty string
        # split the line by the space
            token = line.split(" ")
            if (token[0] == 'R'):
                for i in range(int(token[1])):
                    H[0] += 1
                    mov = check_steps(H, T)
                    if mov == 0:
                        continue
                    elif mov == 2:
                        T[0] += 1
                        if T not in point_travel:
                            temp = T.copy()
                            point_travel.append(temp)
                            num_point_travel += 1       
                    elif mov == 1:
                        T[0] += 1
                        if H[1] > T[1]:
                            T[1] += 1
                        else:
                            T[1] -= 1
                        if T not in point_travel:
                            temp = T.copy()
                            point_travel.append(temp)
                            num_point_travel += 1
            elif (token[0] == 'L'):
                for i in range(int(token[1])):
                    H[0] -= 1
                    mov = check_steps(H, T)
                    if mov == 0:
                        continue
                    elif mov == 2:
                        T[0] -= 1
                        if T not in point_travel:
                            temp = T.copy()
                            point_travel.append(temp)
                            num_point_travel += 1
                    elif mov == 1:
                        T[0] -= 1
                        if H[1] > T[1]:
                            T[1] += 1
                        else:
                            T[1] -= 1
                        if T not in point_travel:
                            temp = T.copy()
                            point_travel.append(temp)
                            num_point_travel += 1
            elif (token[0] == 'U'):
                for i in range(int(token[1])):
                    H[1] += 1
                    mov = check_steps(H, T)
                    if mov == 0:
                        continue
                    elif mov == 2:
                        T[1] += 1
                        if T not in point_travel:
                            temp = T.copy()
                            point_travel.append(temp)
                            num_point_travel += 1
                    elif mov == 1:
                        T[1] += 1
                        if H[0] > T[0]:
                            T[0] += 1
                        else:
                            T[0] -= 1
                        if T not in point_travel:
                            temp = T.copy()
                            point_travel.append(temp)
                            num_point_travel += 1
            elif (token[0] == 'D'):
                for i in range(int(token[1])):
                    H[1] -= 1
                    mov = check_steps(H, T)
                    if mov == 0:
                        continue
                    elif mov == 2:
                        T[1] -= 1
                        if T not in point_travel:
                            temp = T.copy()
                            point_travel.append(temp)
                            num_point_travel += 1
                    elif mov == 1:
                        T[1] -= 1
                        if H[0] > T[0]:
                            T[0] += 1
                        else:
                            T[0] -= 1
                        if T not in point_travel:
                            temp = T.copy()
                            point_travel.append(temp)
                            num_point_travel += 1
            line = f.readline()   
    print(num_point_travel)
    print(point_travel)

          
                    

                

            
            
        
       