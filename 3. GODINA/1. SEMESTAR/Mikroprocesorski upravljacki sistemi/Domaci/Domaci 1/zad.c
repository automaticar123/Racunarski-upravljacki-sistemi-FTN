#include <stdio.h>
#include <stdlib.h>
#include <math.h>

/*int hexDeg[] = {1, 16};
int binDeg[] = {1, 2, 4, 8, 16, 32, 64, 128};
int decDeg[] = {1, 10, 100};*/

void convertStr(char* op, unsigned int* opN, char type, int size) {

    int i;

    if(type == 'h') {
        for(i = size; i > 0; i--) {
            if(*(op+i) >= '0' && *(op+i) <= '9') {
                *opN += pow(16, size-i) * ((unsigned int) *(op+i) - 48);
            }
            else if(*(op+i) >= 'A' && *(op+i) <= 'F') {
                *opN += pow(16, size-i) * ((unsigned int) *(op+i) - 55);
            }
            else {
                *opN = -1;
                return;
            }
        }
    }
    else if(type == 'b') {
        for(i = size; i > 0; i--) {
            if(*(op+i) != '1' && *(op+i) != '0') {
                *opN = -1;
                return;
            }
            else {
               *opN += pow(2, size-i) * ((unsigned int) *(op+i) - 48); 
            }
        }
    }
    else if(type == 'd') {
        for(i = size; i > 0; i--) {
            if(*(op+i-1) >= '0' && *(op+i-1) <= '9') {
                *opN += pow(10, size-i) * ((unsigned int) *(op+i-1) - 48);
            }
        }
        if(*opN > 255) {
            *opN = -1;
            return;
        }
    }
}

void recognizeType(char* op, unsigned int* opN) {
    
    int size = 0;

    if(*op == 'H' || *op == 'h') {
        int i = 1;
        while(*(op+i) != '\0') {
            size++;
            i++;
        }
        if(size > 2){
            *opN = -1;
            return;
        }
        convertStr(op, opN, 'h', size);
    }
    else if(*op == 'B' || *op == 'b') {
        int i = 1;
        while(*(op+i) != '\0') {
            size++;
            i++;
        }
        if(size > 8) {
            *opN = -1;
            return;
        }
        convertStr(op, opN, 'b', size);
    }
    else if(*op >= '0' && *op <= '2') {
        int i = 0;
        while(*(op+i) != '\0') {
            size++;
            i++;
        }
        if(size > 3) {
            *opN = -1;
            return;
        }
        convertStr(op, opN, 'd', size);
    }
    else{
        *opN = -1;
        return;
    }
}

void convertNum(unsigned int r, char* rez) {
    int i;
    int d;
    int k = 0;
    for(i = 0; i <= 2; i++) {
        d = r / pow(10, 2-i);
        if(d == 0) {
            r = r % (unsigned int) pow(10, 2-i);
            continue;
        }
        *(rez+k) = (char) d+48;
        k++;
        r = r % (unsigned int) pow(10, 2-i);
        if(r == 0) {
            break;
        }
    }
    *(rez+k) = '\0';
}

void izracunaj(char* op1, char* op2, char* rez, char operant) {
    
    unsigned int opN1=0, opN2=0;
    
    recognizeType(op1, &opN1);
    recognizeType(op2, &opN2);

    if(opN1 == -1 || opN2 == -1) {
        *rez = 'N';
        return;
    }
    
    unsigned int r;
    switch (operant){
        case '+':
            r = opN1 + opN2;
            if(r > 255) {
                *rez = 'N';
                return;
            }
            convertNum(r, rez);
            break;
        
        case '*':
            r = opN1*opN2;
            if(r > 255) {
                *rez = 'N';
                return;
            }
            convertNum(r, rez);
            break;
        
        case '/':
            if(opN2 == 0) {
                *rez = 'N';
                return;
            }
            r = opN1 / opN2;
            convertNum(r, rez);
            break;
        
        default:
            *rez = 'N';
            break;
        }

        printf("%d", r);
}

void main() {

    char br[] = {'H', 'F', '7', '\0'};
    char br2[] = {'1', '0', '\0'};
    char r[3];

    izracunaj(br, br2, r, '/');
}