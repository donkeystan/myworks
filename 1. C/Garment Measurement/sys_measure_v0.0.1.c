#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<windows.h>
#include<conio.h>

#define SIZE_L 5000
#define SIZE_M 100
#define SIZE_S 20
#define TRUE 1
#define FALSE 0

typedef enum option
{
    KEY_NUM1 = 49, 
    KEY_NUM2 = 50,
    KEY_NUM3 = 51,
    KEY_NUM_Y = 121,
    KEY_NUM_N = 110,
    KEY_ENTER = 13,
    KEY_ECS = 27
    
} option;

typedef struct shirt
{
    struct shirt *prev;
    char blank[SIZE_S];
    char name[SIZE_S];
    char sn[SIZE_S];
    char shoulder[SIZE_S];
    char sleeve[SIZE_S];
    char shirtLength[SIZE_S];
    char collar[SIZE_S];
    char chest[SIZE_S];
    char waist[SIZE_S];
    char hip[SIZE_S];
    struct shirt *next;
} SHIRT;

SHIRT *create_new_empty_node( SHIRT *);
void GOTO_X_Y(int, int);
int input_char(char *, int,  SHIRT *);
int input_pause( SHIRT *);
int single_getchar();
int create_new_garment();
int create_to_ex_garment();
int main_menu();
int sub_menu();
int read_file();
void exit_program();
void error_resume();
void error_resume_sub_menu();
void main_frame_display();
void main_options_display();
void sub_options_display();
SHIRT * data_input(SHIRT*);
SHIRT *save_file_append(SHIRT *);
SHIRT *save_file_overwrite(SHIRT *);
SHIRT *save_file_header_display(SHIRT *);
char * get_time();
void time_stamp();


int main()
{
    while (TRUE)
    {
        main_menu();
    }
    return 0;
}

//////////////////// Menu Operations ////////////////////

int main_menu()
{ 
    while (TRUE)
    {
        int i;
        int input_val;
        option choice;

        main_frame_display();
        main_options_display();
        GOTO_X_Y(15,41);
        choice = getch();
        
        switch (choice)
        {
            case KEY_NUM1:
                sub_menu();
                break;

            case KEY_NUM2:
                read_file();
                break;

            case KEY_NUM3:
                exit_program();
                break;

            default:
                error_resume();
                break;
        }
    }

}

int sub_menu()
{
    while (TRUE)
    {
        int i;
        int input_val;
        option choice;
        
        main_frame_display();
        sub_options_display();

        GOTO_X_Y(15,41);
        choice = getch();
        
        switch (choice)
        {
            case KEY_NUM1:
                create_to_ex_garment();
                break;

            case KEY_NUM2:
                create_new_garment();
                break;

            case KEY_NUM3:
                main_menu();
                break;

            default:
                error_resume_sub_menu();
                break;
        }
    }
    return 0;
}

//////////////////// Main Functions ////////////////////

int create_to_ex_garment()
{
    system("cls");
    SHIRT *head = create_new_empty_node(head);
    main_frame_display();
    GOTO_X_Y(11,37);
    printf("<--------- Append Mode -------->\n");
    head = data_input(head);
    option opt;
    
    GOTO_X_Y(26,0);
    printf("< -------------------------------------------------------------- >\n");
    printf("< ----  Press Enter to Save File, or Else to Abandon Record ---- >\n");
    printf("< -------------------------------------------------------------- >\n");
    opt = getch();

    if (opt == KEY_ENTER)
    {
        // time_stamp();
        save_file_append(head);
        GOTO_X_Y(28,0);
        printf("< --- Append to File, Saved! --- >\n");
        getch();
    }
    else
    {
        GOTO_X_Y(28,0);
        printf("< --- Abandon Saving ! --- > ");
        getch();
    }

    free(head);
    return 0;
}


int create_new_garment()
{
    system("cls");
    SHIRT *head = create_new_empty_node(head);

    GOTO_X_Y(11,37);
    printf("<------- Overwrite Mode ------->\n");

    main_frame_display();
    head = data_input(head);
    option opt;
    
    GOTO_X_Y(26,0);
    printf("< -------------------------------------------------------------- >\n");
    printf("< ----  Press Enter to Save File, or Else to Abandon Record ---- >\n");
    printf("< -------------------------------------------------------------- >\n");
    opt = getch();

    if (opt == KEY_ENTER)
    {
        save_file_overwrite(head);
        GOTO_X_Y(28,0);
        printf("< --- Overwrite File, Saved! --- >\n");
        getch();
    }
    else
    {
        GOTO_X_Y(28,0);
        printf("< --- Abandon Saving ! --- > ");
        getch();
    }

    free(head);
    return 0;
}


SHIRT *save_file_append( SHIRT *head)
{
    SHIRT * ptr= head;
    FILE *file_ptr = fopen("record.txt","a");
    fprintf(file_ptr," %-8s", ptr->sn);
    fprintf(file_ptr,"  %-8s", ptr->name);
    fprintf(file_ptr,"  %-10s", ptr->shoulder);
    fprintf(file_ptr,"  %-8s", ptr->sleeve);
    fprintf(file_ptr,"  %-10s", ptr->shirtLength);
    fprintf(file_ptr,"  %-8s", ptr->collar);
    fprintf(file_ptr,"  %-8s", ptr->chest);
    fprintf(file_ptr,"  %-8s", ptr->waist);
    fprintf(file_ptr,"  %-8s", ptr->hip);
    fprintf(file_ptr,"\n");
    fclose(file_ptr);

    return head;
}

SHIRT *save_file_overwrite( SHIRT *head)
{
    SHIRT * ptr= head;
    FILE *file_ptr = fopen("record.txt","w+");
    fprintf(file_ptr,"--------------------------------------------------------------------------------------\n");
    fprintf(file_ptr,"- SN     | NAME   | SHOULDER | SLEEVE | SHIRT L. | COLLAR | CHEST  | WAIST  | HIP    |\n");
    fprintf(file_ptr,"--------------------------------------------------------------------------------------\n");
    fprintf(file_ptr," %-8s", ptr->sn);
    fprintf(file_ptr,"  %-8s", ptr->name);
    fprintf(file_ptr,"  %-10s", ptr->shoulder);
    fprintf(file_ptr,"  %-8s", ptr->sleeve);
    fprintf(file_ptr,"  %-10s", ptr->shirtLength);
    fprintf(file_ptr,"  %-8s", ptr->collar);
    fprintf(file_ptr,"  %-8s", ptr->chest);
    fprintf(file_ptr,"  %-8s", ptr->waist);
    fprintf(file_ptr,"  %-8s", ptr->hip);
    fprintf(file_ptr,"\n");
    fclose(file_ptr);

    return head;
}


int read_file()
{
    main_frame_display();
    main_options_display();
    GOTO_X_Y(26,0);
    printf("< --- Under Construction... --- >\n");
    printf("< --- Press any key to continue program --- >\n");
    getch();
    return 0;
}

//////////////////// Menu ////////////////////

void exit_program()
{
    main_frame_display();
    main_options_display();
    GOTO_X_Y(26,0);
    printf("< --- Exit Program --- >\n");
    printf("< --- Press any key to exit the program! --- >\n");
    getch();
    exit(0);
}

void error_resume()
{
    main_frame_display();
    main_options_display();
    GOTO_X_Y(27,0);
    printf("< --- Error! --->\n< --- Resume Main Menu --- >\n");
    printf("< --- Press any key to continue program --- >\n");
    getch();
}

void error_resume_sub_menu()
{
    main_frame_display();
    sub_options_display();
    GOTO_X_Y(27,0);
    printf("< --- Error! Resume Sub Menu --- >\n");
    printf("< --- Press any key to continue program --->\n");
    getch();
}


//////////////////// Level-1 Data Handling ////////////////////

 SHIRT *create_new_empty_node( SHIRT *head)
{
    SHIRT *new_node = ( SHIRT *)malloc(sizeof( SHIRT));
    new_node->prev = NULL;
    new_node->next = NULL;
    head = new_node;
    return head;
}


SHIRT * data_input( SHIRT* ptr)
{
    char input[100];

    GOTO_X_Y(12,37);
    printf("--------------------------\n");
    GOTO_X_Y(13,37);
    printf("----Input Measurements----\n");
    GOTO_X_Y(14,37);
    printf("--------------------------\n");

    GOTO_X_Y(15,37);
    printf("Enter Name : ");
    input_char(input, 100, ptr);
    strcpy(ptr->name, input);

    GOTO_X_Y(16,37);
    printf("Enter Serial Number : ");
    input_char(input, 100, ptr);
    strcpy(ptr->sn, input);

    GOTO_X_Y(17,37);
    printf("Shoulder : ");
    input_char(input, 100, ptr);
    strcpy(ptr->shoulder, input);

    GOTO_X_Y(18,37);
    printf("Sleeve : ");
    input_char(input, 100, ptr);
    strcpy(ptr->sleeve, input);

    GOTO_X_Y(19,37);
    printf("Shirt Length : ");
    input_char(input, 100, ptr);
    strcpy(ptr->shirtLength, input);

    GOTO_X_Y(20,37);
    printf("Collar : ");
    input_char(input, 100, ptr);
    strcpy(ptr->collar, input);

    GOTO_X_Y(21,37);
    printf("Chest : ");
    input_char(input, 100, ptr);
    strcpy(ptr->chest, input);

    GOTO_X_Y(22,37);
    printf("Waist : ");
    input_char(input, 100, ptr);
    strcpy(ptr->waist, input);

    GOTO_X_Y(23,37);
    printf("Hip : ");
    input_char(input, 100, ptr);
    strcpy(ptr->hip, input);


    return ptr;
}

//////////////////// General Functions ////////////////////


void time_stamp()
{
    char* time_str = get_time();
    FILE *file_ptr = fopen("record.txt","a");
    fprintf(file_ptr,"\n ##### Following Records Starts at : %s ", time_str);
    fclose(file_ptr);
    free(time_str);
}

char *get_time()
{
    char* time_str = (char *)malloc(sizeof(time_str));
    time_t now; // declaration
    time(&now); // get the time in string
    time_str = ctime(&now); // print the time in string.
    return time_str;
}

int single_getchar()
{
    int ch;
    ch = getchar();
    return ch;
}

int input_char(char *tmp_input, int limit,  SHIRT* ptr)
{
    int ch = 0;
    int i = 0;

    i = 0;
    while ((ch = getchar()) != '\n')
    {
        if (i < limit)
        {
            tmp_input[i] = ch;
            i++;
        }
        if (27 == ch)
        {
            input_pause(ptr);
        }
    }
    tmp_input[i] = '\0';

    return i;
}

int input_pause( SHIRT * head)
{
    option opt;

    main_frame_display();
    GOTO_X_Y(12,12);
    printf("Abandon Input? Enter ESC Again...\n");
    GOTO_X_Y(13,12);
    printf("Else Continue...\n");

    opt = getch();

    if (opt == KEY_ECS)
    {
        free(head);
        return 0;
    }
    else
    {
        main();
    }
    return 0;
}

//////////////////// Move Coordinates ////////////////////

void GOTO_X_Y(int x, int y)
{
    COORD coord;
    coord.X = y;
    coord.Y = x;
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), coord);
}

//////////////////// Menu Layout ////////////////////

void main_options_display()
{
    GOTO_X_Y(11,12);
    printf("Options:");
    GOTO_X_Y(12,12);
    printf("1. Create a New Garment");
    GOTO_X_Y(13,12);
    printf("2. Read Current Record ");
    GOTO_X_Y(14,12);
    printf("3. Exit Program");

    GOTO_X_Y(15,12);
    printf("Please enter your option : ");
}


void sub_options_display()
{
    GOTO_X_Y(11,12);
    printf("Options:");
    GOTO_X_Y(12,12);
    printf("1. Append Current Record");
    GOTO_X_Y(13,12);
    printf("2. Overwrite Current Record ");
    GOTO_X_Y(14,12);
    printf("3. Back to Main Menu");

    GOTO_X_Y(15,12);
    printf("Please enter your option : ");
}

//////////////////// Frames ////////////////////

void main_frame_display()
{
        system("cls");
        printf("\n#####################################################################################################\n");
        printf("############                                                                             ############\n");
        printf("############               Garment Measurement Data Input and Record System              ############\n");
        printf("############                                                                             ############\n");
        printf("############                  Version 1.0 Beta, System built by Stan L.                  ############\n");
        printf("############                                                                             ############\n");
        printf("############                             Copyright (C) 2021                              ############\n");
        printf("############                                                                             ############\n");
        printf("#####################################################################################################\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("############                                                                             ############\n");
        printf("#####################################################################################################\n\n\n");
}