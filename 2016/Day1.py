def calculate_next_direction(current_direction, new_direction):
    """
    This function takes the direction the player is facing and
    the direction from user input and returns the player's next
    direction.
    """
    if new_direction == "R":
        if current_direction == "North":
            return "East"
        if current_direction == "East":
            return "South"
        if current_direction == "South":
            return "West"
        if current_direction == "West":
            return "North"
    if new_direction == "L":
        if current_direction == "North":
            return "West"
        if current_direction == "East":
            return "North"
        if current_direction == "South":
            return "East"
        if current_direction == "West":
            return "South"    
        
def parse_movement(input_str):
    """
    This function takes the user input and splits into
    direction and number of blocks moved. 
    """
    direction = input_str[0]
    distance = int(input_str[1:])
    
    return direction, distance

def find_distance(movements:list) -> int:
    """
    This function is the runner of the script. Takes a list 
    of movements and returns the distance from starting 
    position to headquarters given formual in advent of code. 
    """
    current_postion = [0,0]
    current_direction = "North"
    covered_positions = []
    distance_to_headquarter = float('inf')

    for i in movements:
        direction, distance = parse_movement(i)
        temp_current_position = current_postion.copy()
        current_direction = calculate_next_direction(current_direction, direction)

        if current_direction == "North":
            current_postion[1]+=distance
            for i in range(temp_current_position[1]+1, current_postion[1]+1):
                
                if([temp_current_position[0],i] in covered_positions):
                    distance_to_headquarter = abs(temp_current_position[0]) + abs(i)
                    return distance_to_headquarter
                else:
                    covered_positions.append([temp_current_position[0],i])
                
        elif current_direction == "East":
            current_postion[0]+=distance
            for i in range(temp_current_position[0]+1, current_postion[0]+1):                
                if([i,temp_current_position[1]] in covered_positions):
                    distance_to_headquarter = abs(i) + abs(temp_current_position[1])
                    return distance_to_headquarter
                else:
                    covered_positions.append([i,temp_current_position[1]])
        elif current_direction == "South":
            current_postion[1]-=distance
            for i in range( temp_current_position[1]-1,current_postion[1]-1, -1):
                if([temp_current_position[0],i] in covered_positions):
                    distance_to_headquarter = abs(temp_current_position[0]) + abs(i)
                    return distance_to_headquarter
                else:
                    covered_positions.append([temp_current_position[0],i])  
        elif current_direction == "West":
            current_postion[0]-=distance
            for i in range( temp_current_position[0]-1,current_postion[0]-1, -1):
                if([i,temp_current_position[1]] in covered_positions):
                    distance_to_headquarter = abs(i) + abs(temp_current_position[1])
                    return distance_to_headquarter
                else:
                    covered_positions.append([i,temp_current_position[1]])
                
    
    return distance_to_headquarter

if __name__ == "__main__":
    
    input_sequence = input("Enter Puzzle Input: ")
    movements = input_sequence.split(", ")
    print(find_distance(movements))

