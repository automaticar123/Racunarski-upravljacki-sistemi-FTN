void convertStr(char* op, unsigned int* opN, char type, int size) {

    int i;
    int ak = 1;

    if(type == 'h') {
        for(i = size; i > 0; i--) {

            if(*(op+i) >= '0' && *(op+i) <= '9') {
                *opN += ak * ((unsigned int) *(op+i) - 48);
            }
            else if(*(op+i) >= 'A' && *(op+i) <= 'F') {
                *opN += ak * ((unsigned int) *(op+i) - 55);
            }
            else {
                *opN = -1;
                return;
            }

            ak *= 16;
        }
    }
    else if(type == 'b') {
        for(i = size; i > 0; i--) {

            if(*(op+i) != '1' && *(op+i) != '0') {
                *opN = -1;
                return;
            }
            else {
                *opN += ak * ((unsigned int) *(op+i) - 48);
                ak *= 2;
            }
        }
    }
    else if(type == 'd') {
        for(i = size-1; i >= 0; i--) {
            if(*(op+i) >= '0' && *(op+i) <= '9') {
                *opN += ak * ((unsigned int) *(op+i) - 48);
                ak *= 10;
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
    else if(*op >= '0' && *op <= '9') {
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
    int d;
    int k = 0;
    int ak = 100;

    do{
        d = r / ak;
        if(d == 0) {
            r = r % ak;
            continue;
        }
        *(rez+k) = (char) d+48;
        k++;
        r = r % ak;
        ak /= 10;
    }while(r != 0);

    *(rez+k) = '\0';
}

void izracunaj(char* op1, char* op2, char* rez, char operant) {
    
    unsigned int opN1=0, opN2=0;
    unsigned int r;
    
    recognizeType(op1, &opN1);
    recognizeType(op2, &opN2);

    if(opN1 == -1 || opN2 == -1) {
        *rez = 'N';
        return;
    }

    switch (operant){
        case '+':
            r = opN1 + opN2;
            if(r > 255) {
                *rez = 'N';
                break;
            }
            convertNum(r, rez);
            break;
        
        case '*':
            r = opN1*opN2;
            if(r > 255) {
                *rez = 'N';
                break;
            }
            convertNum(r, rez);
            break;
        
        case '/':
            if(opN2 == 0) {
                *rez = 'N';
                break;
            }
            r = opN1 / opN2;
            convertNum(r, rez);
            break;

        case 'c':
            r = 2*opN1;
			if(r > 255) {
				*rez = 'N';
				break;
			}
            r -= opN2;
			if(r < 0) {
				*rez = 'N';
				break;
			}

		   	convertNum(r, rez);
           	break;
        
        default:
            *rez = 'N';
            break;
        }
}

void main() {

    char br[] = {'2', '0', '\0'};
    char br2[] = {'3', '\0'};
    char r[3];

    izracunaj(br, br2, r, 'c');
}