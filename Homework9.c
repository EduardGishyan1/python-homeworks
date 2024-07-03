// // Task1

// int main() {
//     int num = 10;
//     int num2 = 3;
//     int num3 = 5;

//     int *c_num = &num;
//     int *c_num2 = &num2;
//     int *c_num3 = &num3;

//     printf("%p\n",c_num);
//     printf("%p\n",c_num2);
//     printf("%p\n",c_num3);
//     return 0;
// }

// // Task2

// int main(){
//     int arr[5];
//     arr[0] = 1;
//     arr[1] = 2;
//     arr[2] = 3;
//     arr[3] = 4;
//     arr[4] = 5;
//     int *arr0 = arr; 
//     printf("%p\n",arr0);
//     for (int i = 0;i < 5;++i){
//         printf("%d",*arr0);
//         arr0++;
//     }
//     return 0;
// }

// // Task3

// int main() {
//     int arr[5] = {1, 2, 3, 4, 5};
//     int arr2[5] = {6, 7, 8, 9, 10};
//     int *arr3 = arr;
//     int *arr4 = arr2;
//     int mix[10];

//     for (int j = 0; j < 5; ++j) {
//         mix[j] = arr3[j];
//         mix[j + 5] = arr4[j];
//     }

//     for (int i = 0; i < 10; i++) {
//         printf("%d\n", mix[i]);
//     }

//     return 0;
// }

// // Task 4
// int main(){
// int arr[5] = {1,2,3,4,5};
// int arr2[5] = {1,2,4,4,5};

// for (int k = 0;k < 5;k++){
//     if (arr[k] == arr2[k]){
//         printf("True\n");
//     }
//     else{
//         printf("False\n");
//     }
// }
// }

// // Task 5


// int main() {
//     char str[100]; 
//     int length = 0;
    
//     scanf("%99[^\n]", str);

//         while (str[length] != '\0') {
//         length++;
//     }
//     printf("%d\n", length);
//     return 0;
// }

// // Task 6

// int main() {
//     char str[100]; 
//     int length = 0; 
//     scanf("%99[^\n]", str);

//     while (str[length] != '\0') {
//         length++;
//     }
    
//     printf("%d\n", length);

//     for (int i = length - 1; i >= 0; i--) {
//         printf("%c", str[i]);
//     }
//     printf("\n");

//     return 0;
// }

// // Task 7

// // int main() {
// //     char str[100];
// //     int i = 0;
// //     printf("Enter a string: ");
// //     scanf("%99[^\n]", str);
// //     while (str[i] != '\0') {
// //         if (str[i] >= 'a' && str[i] <= 'z') {   
// //             str[i] = str[i] ^ 32;
// //         }
// //         i++;
// //     }
// //     printf("Uppercase string: %s\n", str);
// //     return 0;
// // }

// // Task 8


// int main() {
//     int size;
//     printf("Enter the size of the array: ");
//     scanf("%d", &size);

//     if (size <= 0) {
//         printf("Invalid size. Please enter a positive integer.\n");
//         return 1; 
//     }
//     int arr[size]; 
//     int max_number; 

//     printf("Enter %d integers:\n", size);
//     for (int i = 0; i < size; i++) {
//         scanf("%d", &arr[i]);
//     }

//     max_number = arr[0];

//     for (int j = 1; j < size; j++) {
//         if (arr[j] > max_number) {
//             max_number = arr[j];
//         }
//     }

//     printf("Maximum number: %d\n", max_number);

//     return 0;
// }

// // Task 9

// int main() {
//     int size;
//     printf("Enter the size of the array: ");
//     scanf("%d", &size);

//     if (size <= 0) {
//         printf("Invalid size. Please enter a positive integer.\n");
//         return 1; 
//     }
//     int arr[size]; 
//     int min_number; 

//     printf("Enter %d integers:\n", size);
//     for (int i = 0; i < size; i++) {
//         scanf("%d", &arr[i]);
//     }

//     min_number = arr[0];

//     for (int j = 1; j < size; j++) {
//         if (arr[j] < min_number) {
//             min_number = arr[j];
//         }
//     }

//     printf("Minimum number: %d\n", min_number);

//     return 0;
// }

// // Task 10

// int main() {
//     int number, reversed = 0;

//     printf("Enter an integer greater than 12: ");
//     scanf("%d", &number);

//     if (number <= 12) {
//         printf("Invalid input. Please enter an integer greater than 12.\n");
//         return 1;
//     }

//     while (number > 0) {
//         reversed = reversed * 10 + number % 10; 
//         number = number / 10; 
//     }

//     printf("Reversed number: %d\n", reversed);

//     return 0;
// }