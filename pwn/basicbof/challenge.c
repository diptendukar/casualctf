#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

void setup() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void print_flag() {
    char c;
    FILE *f = fopen("flag.txt", "r");
    while ((c = fgetc(f)) != EOF) {
        putc(c, stdout);
    }
}

int main() {
    char name[40];
   
    uint64_t number = 0xdeadbeef;

    setup();

    puts("Welcome to the first PWN challenge!");
    puts("If you can change the number to 0xa0b1c2d3, you win!");
    puts("What's your name?");

    gets(name);

    if (number == 0xa0b1c2d3) {
        print_flag();
    } else {
        printf("The number is 0x%lx right now.\nTry again!\n",
               number);
    }

    return 0;
}
