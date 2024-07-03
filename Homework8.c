//1

// int main() {
//     int number = 0;
//     int n = 0;
//     int result_mul = 0;
//     int result_div = 0;
    
//     printf("Enter a number: ");
//     scanf("%d", &number);
//     printf("Enter the exponent n: ");
//     scanf("%d", &n);
    
//     result_mul = number << n;
    
//     result_div = number >> n;
    
//     printf("%d,%d  %d/n", number, n, result_mul);
//     printf("%d,%d is: %d/n", number, n, result_div);
    
// //2


//     int number = 0;
//     int mul = 0;
//     int div = 0;
//     printf("Enter a number: ");
//     scanf("%d", &number);
//     mul = number << 1;
//     div = number >> 1;
//     printf("%d,%d  %d\n", number, mul);
//     printf("%d,%d %d\n", number, div);
    

// //3


//     int countOnes = 0;
//     int countZeros = 0;
//     int num = 0;
//     scanf("%d",&num);
//     while (num != 0) {
//         if (num & 1) {
//             countOnes++;
        
//         } else {
//             countZeros++;
          
//         }
//         num >>= 1; 
//     }
//     printf("%d\n",countOnes);
//     printf("%d\n",countZeros);


// //4

//     int num = 0;
//     printf("Enter a number: ");
//     scanf("%d", &num);
    
//     if (num & 1) {
//         printf("%d is odd.\n", num);
//     } else {
//         printf("%d is even.\n", num);
//     }
//     return 0;


// //5
//     char ch;
//     if (ch >= 'a' && ch <= 'z') {
//     printf("Enter a character: ");
//     scanf("%c", &ch);
//     ch = ch ^ 32;
//     printf("%c\n", ch);
//     }
// //6

//     // int num;
    
//     // printf("Enter a number: ");
//     // scanf("%d", &num);

//     // int mask = 1;
//     // while (num & mask) {
//     //     mask <<= 1; 
//     // }
    
//     //     num |= mask;

//     // printf("Modified number: %d\n", num);    
//     // return 0;
// }