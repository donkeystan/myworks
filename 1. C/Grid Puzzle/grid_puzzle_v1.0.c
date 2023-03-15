#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<windows.h>
#include<conio.h>
#include<wincon.h>
#include<string.h>

#define BOARD_ROW_SIZE 5
#define BOARD_COL_SIZE 5
#define UP 72
#define LEFT  75
#define RIGHT 77
#define DOWN 80
#define ESC 27
#define CLEAR_SCREEN system("cls");
char *TILE[] = {" ", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25" };
void shuffle(int *nums, int nums_size);
int isSolvable(int *nums, int numsSize);
void nums_swap(int *nums, int index1, int index2);
void print_board(char ***board, int row_size, int col_size);
void set_new_game();
void game_start(char ***board, char ***answer_board);
void movement(char ***board, int position);
void board_swap(char ***board, int row1, int col1, int row2, int col2);
int isWin(char ***board, char ***answer_board);
char ***draw_game_board(int *nums);
char ***draw_answer_board();
char ***draw_result_board();
void print_head();
void print_footer();
void quit();
void garbage_collect(char ***board);

int main(int argc, char const *argv[])
{
    set_new_game();
    return EXIT_SUCCESS;
}

void set_new_game()
{
    system("mode con cols=80 lines=40");
    int nums[BOARD_ROW_SIZE * BOARD_COL_SIZE];
    int nums_size = BOARD_ROW_SIZE * BOARD_COL_SIZE;
    int i;
    for (i=0; i<nums_size; i++)
    {
        nums[i] = i;
    }

    do
    {
        shuffle(nums, nums_size);
    } while (!isSolvable(nums, nums_size));
    
    char ***game_board = draw_game_board(nums);
    char ***answer_board = draw_answer_board();

    CLEAR_SCREEN
    print_head();
    print_board(game_board, BOARD_ROW_SIZE, BOARD_COL_SIZE);
    print_footer();

    while(1)
    {
        game_start(game_board, answer_board);
        if (isWin(game_board, answer_board))
        {
            garbage_collect(game_board);
            CLEAR_SCREEN
            print_head();
            print_board(game_board = draw_result_board(), BOARD_ROW_SIZE, BOARD_COL_SIZE);
            printf("\n\n< --- You win ! --- >\n");
            print_footer();
        }
    }
}

void game_start(char ***game_board, char ***answer_board)
{
    int ch;
    ch=getch();
    switch(ch)
    {
        case LEFT: 
            movement(game_board, LEFT);
            CLEAR_SCREEN
            print_head();
            print_board(game_board, BOARD_ROW_SIZE, BOARD_COL_SIZE);
            print_footer();
            break;
            
        case RIGHT:
            movement(game_board, RIGHT);
            CLEAR_SCREEN
            print_head();
            print_board(game_board, BOARD_ROW_SIZE, BOARD_COL_SIZE);
            print_footer();
            break;
            
        case DOWN:
            movement(game_board, DOWN);
            CLEAR_SCREEN
            print_head();
            print_board(game_board, BOARD_ROW_SIZE, BOARD_COL_SIZE);
            print_footer();
            break;
        
        case UP:
            movement(game_board, UP);
            CLEAR_SCREEN
            print_head();
            print_board(game_board, BOARD_ROW_SIZE, BOARD_COL_SIZE);
            print_footer();
            break;
            
        case ESC:
            CLEAR_SCREEN
            print_head();
            print_board(game_board, BOARD_ROW_SIZE, BOARD_COL_SIZE);
            print_footer();
            quit();
            break;
        
        case 'r':
            set_new_game();
            break;

        default:
            CLEAR_SCREEN
            print_head();
            print_board(game_board, BOARD_ROW_SIZE, BOARD_COL_SIZE);
            print_footer();
            break;
    }
}

void movement(char ***game_board, int position)
{
    int i, j;
    switch(position)
    {
        case LEFT: 
            for (i=0; i<BOARD_ROW_SIZE; i++)
            {
                for (j=0; j<BOARD_COL_SIZE; j++)
                {
                    if (j > 0 && game_board[i][j-1] == TILE[0])
                    {
                        board_swap(game_board, i, j, i, j-1);
                        return;
                    }
                }
            }
            break;
            
        case RIGHT:
            for (i=0; i<BOARD_ROW_SIZE; i++)
            {
                for (j=0; j<BOARD_COL_SIZE; j++)
                {
                    if (j < BOARD_COL_SIZE-1 && game_board[i][j+1] == TILE[0])
                    {
                        board_swap(game_board, i, j, i, j+1);
                        return;
                    }
                }
            }
            break;
            
        case DOWN:
            for (i=0; i<BOARD_ROW_SIZE; i++)
            {
                for (j=0; j<BOARD_COL_SIZE; j++)
                {
                    if (i < BOARD_ROW_SIZE-1 && game_board[i+1][j] == TILE[0])
                    {
                        board_swap(game_board, i, j, i+1, j);
                        return;
                    }
                }
            }
            break;
        
        case UP:
            for (i=0; i<BOARD_ROW_SIZE; i++)
            {
                for (j=0; j<BOARD_COL_SIZE; j++)
                {
                    if (i > 0 && game_board[i-1][j] == TILE[0])
                    {
                        board_swap(game_board, i, j, i-1, j);
                        return;
                    }
                }
            }
            break;

        default:
            break;
    }
}

void nums_swap(int *nums, int index1, int index2)
{
    int temp = nums[index1];
    nums[index1] = nums[index2];
    nums[index2] = temp;
}

int isSolvable(int *nums, int numsSize)
{
    int i, j;
    int count = 0;
    for (i=0; i<numsSize; i++)
    {
        for (j=i+1; j<numsSize; j++)
        {
            if (nums[i] && nums[j] && nums[i] > nums[j])
            {
                count += 1;
            }
        }
    }
    return (count%2 == 0) ? 1 : 0; 
}

void shuffle(int *nums, int nums_size)
{
    srand(time(0));
    int i;
    int pick;
    for (i=0; i<nums_size; i++)
    {
        pick = rand() % (nums_size);
        nums_swap(nums, i, pick);
    }
}

int isWin(char ***game_board, char ***answer_board)
{
    int i, j;
    for (i=0; i<BOARD_ROW_SIZE; i++)
    {
        for (j=0; j<BOARD_COL_SIZE; j++)
        {
            if (game_board[i][j] != answer_board[i][j])
            {
                return 0;
            }
        }
    }
    return 1;
}

void board_swap(char ***board, int row1, int col1, int row2, int col2)
{
    char *tmp = board[row1][col1];
    board[row1][col1] = board[row2][col2];
    board[row2][col2] = tmp;
}

char ***draw_game_board(int *nums)
{
    char ***game_board = (char ***)malloc(sizeof(char **) * BOARD_ROW_SIZE);
    int i, j , k=0;
    for (i=0; i<BOARD_ROW_SIZE; i++)
    {
        game_board[i] = (char **)malloc(sizeof(char *) * BOARD_COL_SIZE);
        for (j=0; j<BOARD_COL_SIZE; j++)
        {
            game_board[i][j] = TILE[nums[k++]];
        }
    }
    return game_board;
}

char ***draw_answer_board()
{
    char ***answer_board = (char ***)malloc(sizeof(char **) * BOARD_ROW_SIZE);
    int i, j , k=1;
    for (i=0; i<BOARD_ROW_SIZE; i++)
    {
        answer_board[i] = (char **)malloc(sizeof(char *) * BOARD_COL_SIZE);
        for (j=0; j<BOARD_COL_SIZE; j++)
        {
            if (i == BOARD_ROW_SIZE-1 && j == BOARD_COL_SIZE-1)
            {
                answer_board[i][j] = TILE[0];
                break;
            }
            answer_board[i][j] = TILE[k++];
        }
    }
    return answer_board;
}

char ***draw_result_board()
{
    char ***result_board = (char ***)malloc(sizeof(char **) * BOARD_ROW_SIZE);
    int i, j , k=1;
    for (i=0; i<BOARD_ROW_SIZE; i++)
    {
        result_board[i] = (char **)malloc(sizeof(char *) * BOARD_COL_SIZE);
        for (j=0; j<BOARD_COL_SIZE; j++)
        {
            result_board[i][j] = TILE[k++];
        }
    }
    return result_board;
}

void print_board(char ***board, int row_size, int col_size)
{
    int i, j;
    for (i=0; i<row_size; i++)
    {
        printf("     +");

        for (j=0; j<col_size; j++)
        {
            printf("------+");
        }
        printf("\n");

        printf("     |");
        for (j=0; j<col_size; j++)
        {
            printf("  %2s  |", board[i][j]);
        }
        printf("\n");
    }
    printf("     +");

        for (j=0; j<col_size; j++)
        {
            printf("------+");
        }
        printf("\n");
}

void quit()
{
    printf("\n\n< ---Exit Game!--- >\n\n");
    printf("Press [Y] to Quit\n\n");
    if (121 == getch())
    {
        printf("< --- Press [ any key ] to exit the game! --- >\n");
        getch();
        exit(0);
    }
}

void print_head()
{
    printf("< ----- The %d Puzzle Game ----- >\n\n", (BOARD_COL_SIZE*BOARD_ROW_SIZE)-1);
}

void print_footer()
{
    printf("\n\n< ----------------------------- >\n\n");
    printf("Instructions :\n\n");
    printf("ESC to QUIT GAME\n");
    printf("Press [ r ] to Restart a Game\n" );
    printf("Movement: Button [ Up ] [ Down ] [ Left ] [ Right ]\n");
}

void garbage_collect(char ***board)
{
    int i, j;
    for (i=0; i<BOARD_ROW_SIZE; i++)
    {
        for (j=0; j<BOARD_COL_SIZE; j++)
        {
            free(board[i][j]);
        }
        free(board[i]);
    }
    free(board);
}