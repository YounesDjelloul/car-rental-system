#include <stdio.h>
#include <stdbool.h>
    int option, suboption, id_num, num_confirm, day, month, year, endday;
    int endmonth, endyear, card_num;
    char name[100];
    char phone_number[50];
    char phone_number2[50];
    char password[30];
    char password2[30];
    char repassword[30];
    bool sign_up=false;
   
    char real_num[50];
    void details(void);
    void funcswitch(void);
    void car_info(void);
    void passwordfunc(void);

void details(void)

{
    printf("\nWelcome to the Car Rental System ");
    printf("\n1- Login To System\n");
    printf("2- Signup To system\n");
    printf("Please select an option from the above menu: ");
    scanf("%d", &option);
    funcswitch();
}

void car_info(void)
{
            printf("\nPlease choose any of the available cars: ");
            printf("\nId number  car brand     stars    price\n");
            printf("    1         VOLVO         4.7    $140/day\n");
            printf("    2         VOLVO         4.5    $110/day\n");
            printf("    3         BENZ          4.9    $200/day\n");
            printf("    4         POCSCHE       4.9    $190/day\n");
            scanf("%d", &id_num);
            printf("Please type 1 to confirm your booking. ");
            scanf("%d", &num_confirm);
            printf("Please enter the start date: ");
            scanf("%d%*c%d%*c%d", &day, &month, &year);
            printf("Please enter the end date: ");
            scanf("%d%*c%d%*c%d", &endday, &endmonth, &endyear);
            printf("Please enter your visa/master card number: ");
            scanf("%d", &card_num);
            printf("Booking successful! Your booking id is %d.", id_num);
            
}

void passwordfunc(void)
{
    printf("\nPlease enter your password: ");
    scanf("%s", password);
    printf("Please re-enter your password: ");
    scanf("%s", repassword);
}


void funcswitch(void)
{
    switch(option) {
        case 1:
        if (sign_up==false) {
            printf("No record found. Please sign up first!");
            details();}
        else {
            printf("Please enter your Phone Number: ");
            scanf("%s", phone_number2);
            if (real_num[50]!=phone_number2[50])
            {
                printf("This phone number has no account. Please sign up.");
                details();
            }
            else {    
            printf("Please a valid Password: ");
            scanf("%s", password2);
            car_info();
            break;}}
        
        case 2:
        sign_up=true;
        printf("Please enter your fullname: ");
        scanf("%s", name);
        printf("Please enter your phone number:");
        scanf("%s", phone_number);
        real_num==phone_number;
        printf("Please enter your password: ");
        scanf("%s", password);
        printf("Please re-enter your password: ");
        scanf("%s", repassword);
        if (password[30]!=repassword[30]){
            printf("Passwords are not same.");
            passwordfunc();
            printf("Signup Successfull! Please login to the system.");
            details();
        }
        else
        {
            printf("Signup Successfull! Please login to the system.");
            details();}
        
        default:
        printf("\nPlease inout from the menu.");
        details();
}
}

int main()
{
    printf("Welcome to the Car Rental System ");
    printf("\n1- Login To System\n");
    printf("2- Signup To system\n");
    printf("Please select an option from the above menu: ");
    scanf("%d", &option);
    funcswitch();
    return 0;
    }
