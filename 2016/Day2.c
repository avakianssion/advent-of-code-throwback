/*
Realizing again that C is not simple to code in!

1 2 3
4 5 6
7 8 9
we start at 5. 
We want to get a digit per line of input.
Can't go out of bounds, stay where you are if move out of bounds.
current_position changes at the end of each line. 

input = array of lines
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define BUFFER_MAX 5000
#define MAX_LINE 500
#define LINE_LEN_MAX 1000

/*initialize keypad*/
const int keypad[3][3] = {
    {1,2,3},
    {4,5,6},
    {7,8,9}
};
/*define starting positions*/
int current_position_row = 1;
int current_position_col = 1;
/*Define movements*/
// 'R' = [][+1]
// 'L' = [][-1]
// 'U' = [+1][]
// 'D' = [-1][]

/*Check if the character incoming is a valid move of right, left, up, or down*/
bool valid_move(char c){
    if (c != 'R' && c != 'L' && c != 'U' && c != 'D')
        return false;
    return true;
}

/*Check if the next move will put the player out of bound*/
bool out_of_bounds(char move) {
    int new_row = current_position_row;
    int new_col = current_position_col;

    switch (move) {
        case 'U':
            new_row -= 1;
            break;
        case 'D':
            new_row += 1;
            break;
        case 'L':
            new_col -= 1;
            break;
        case 'R':
            new_col += 1;
            break;
        default:
            return true; 
    }

    if (new_row < 0 || new_row >= 3 || new_col < 0 || new_col >= 3) {
        return true; // Out of bounds
    }

    return false; // Within bounds
}

/*Driver function to crack the code given a set of moves*/
void find_code(const char puzzle_input[]){
    int code[BUFFER_MAX];
    int code_size=0;
    int temp_code_to_add;
    int test_valid_move_num=0;

    for(int i=0; i<BUFFER_MAX;i++){
        if (valid_move(puzzle_input[i])){
            test_valid_move_num++;
            if (out_of_bounds(puzzle_input[i]) == false){
                switch (puzzle_input[i]) {
                    case 'U':
                        current_position_row -= 1;
                        break;
                    case 'D':
                        current_position_row += 1;
                        break;
                    case 'L':
                        current_position_col -= 1;
                        break;
                    case 'R':
                        current_position_col += 1;
                        break;
                }
                //printf("New position: (%d)\n", keypad[current_position_row][current_position_col]);
            }
        
            // If move puts us out of bounds - do nothing
            // else temp_code is the next position
        }
        else if (puzzle_input[i] == '\n'){
            // append temp_code to code
            code[code_size] = keypad[current_position_row][current_position_col];
            // printf("This is a new line, move to the next digit of code.\n");
            code_size++;
        }
        else{
            // Do nothing
        }
    }
    // printf("We have %d valid moves in this patternn.\n",test_valid_move_num);
    // printf("The len of the passcode is: %d\n", code_size);
    printf("The code is: ");
    for (int i=0; i<code_size;i++){
        printf("%d", code[i]);
    }
    printf("\n");
    //iterate on code array up to code_size, this is the answer

}

int main(){
    char *buffer = NULL;
    char temp_line[LINE_LEN_MAX];
    size_t buffer_length = 0;

    printf("Enter the puzzle input Then enter Ctrl+D to end: ");
    while(fgets(temp_line,LINE_LEN_MAX,stdin) != NULL) {
        size_t temp_line_len = strlen(temp_line);
        
        char *temp_buffer = realloc(buffer, temp_line_len+buffer_length+1);
        buffer = temp_buffer;
        strcpy(buffer + buffer_length, temp_line);
        buffer_length+=temp_line_len;
    }
     
    find_code(buffer);
    free(buffer);
    return 0;
}