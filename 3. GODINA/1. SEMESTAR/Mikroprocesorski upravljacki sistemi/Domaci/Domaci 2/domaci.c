#include <at89c51rc2.h>
/*  
    P0_0 - START
    P0_1 - STOP
    P0_2 - PROGRAM 1
    P0_3 - PROGRAM 2
    P0_4 - PROGRAM 3
    P0_5 - PROGRAM 4
    PO_6 - BRZINA 1
    PO_7 - BRZINA 2
*/

// FIBONACI NIZ: 0x01, 0x02, 0x03, 0x05, 0x08, 0x0D, 0x15, 0x22, 0x37, 0x59, 0x90, 0xE9 

void delay(unsigned char speed) {
    int i, j;
    // BRZINA 1
    if(!speed) {
        for(i = 0; i < 200; i++) {
            for(j = 0; j < 200; j++) {

            }
        }
    }							   
    // BRZINA 2
    else {
        for(i = 0; i < 400; i++) {
            for(j = 0; j < 400; j++) {

            }
        }
    }
}

void state(unsigned char state_chg_det, unsigned char* state_P2, unsigned char* help) {
    switch (state_chg_det) {
        // PROGRAM 1
        default:
            *state_P2 = ~(*state_P2);
            break;
        // PROGRAM 2 
        case 0x08:
            if(*state_P2 == 0x00) {
                *state_P2 = 0x01;
            }
            else {
                *state_P2 <<= 1;
            }
            break;
        // PROGRAM 3
        case 0x10:
            if(*state_P2 == 0x00) {
                *state_P2 = 0x80 + 0x01;
            }
            else if(*state_P2 == 0x18 || *state_P2 == 0x81) {
                *help = ~(*help);
            }

            if(*help == 0x00) {
                *state_P2 = (((*state_P2)&0x0F)<<1) + (((*state_P2)&0xF0)>>1);
            }
            else {
                *state_P2 = (((*state_P2)&0x0F)>>1) + (((*state_P2)&0xF0)<<1);
            }
			break;
        // PROGRAM 4
        case 0x20:
            if(*state_P2 == 0xE9 || *state_P2 == 0x00) {

                *state_P2 = 0x01;
                *help = 0x01;
            }
            else{
                state_chg_det = *state_P2;
                *state_P2 += *help;
                *help = state_chg_det;
            }
            break;
        case 0x80:
            if(*state_P2 == 0xFF) {
                *state_P2 = 0x00;
            }
            *state_P2 = *state_P2 + 0x01;
            break;
    }
}

void main() {

    unsigned char previous_state_P0 = P0;
    unsigned char state_P2 = 0x00;
    unsigned char state_chg_det = 0x00;	 
    unsigned char what_chg;
	unsigned char help = 0x00;
    unsigned char previous_state_chg_det = 0x00;
    unsigned char speed = 0x00;
    unsigned char start = 0x00;
    unsigned char stop = 0x00;

    P2 = 0x00;
    P0 = 0xFF;

    while(1) {

        state_chg_det = P0 ^ previous_state_P0; 
        // XOR kolo detektuje na kojem bitu je promjena
        previous_state_P0 = P0; 
        // Cuva se prethodno stanje P0 porta0x0
        what_chg = state_chg_det & P0; 
        // AND kolo - kada je promjena = 0 (1->0), kada je promjena != 0 (0->1) 

        if((state_chg_det == 0x02 && what_chg == 0x00)) {
            start = 0x00;
        }
        // Stisnut STOP - start se iskljucuje i ostaje se u istom stanju

        if((state_chg_det == 0x01 && what_chg == 0x00) || start == 0x01) {

            start = 0x01;

            // Ako nije detektovana promjena brzine ili ako se opet stisne start
            // Znaci da se bira novi MOD
            if(state_chg_det != 0x00 &&
               state_chg_det != 0x01 && 
               state_chg_det != 0x40 && 
               what_chg == 0x00) {
                
                state_P2 = 0x00;
                help = 0x00;
                state(state_chg_det, &state_P2, &help);
                previous_state_chg_det = state_chg_det;
            }
            // Ako je detektovana promjena brzine ili nikakva promjena uopste,
            // Mijenja se brzina ili se iterira stari MOD
            else {
                if(state_chg_det == 0x40 && what_chg == 0x00) {
                    speed = 0x01;
                }
                state(previous_state_chg_det, &state_P2, &help);
            }
        }
        P2 = state_P2;
        delay(speed);
    }
}