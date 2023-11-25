#include <at89c51rc2.h>

void delay(void) {
	int i, j, k;
	for(k = 0; k < 3; k++) {
		for(i = 0; i < 200; i++) {
			for(j = 0; j < 200; j++) {

			}
		}
	}
}

void main(void) {
	
	unsigned char stanje_P2 = 0x01;
	unsigned char lijevi = 0x01;
	unsigned char desni = 0x80;

	P0 = 0x00;
	P2 = 0x00;

	while(1) {
		
		if(lijevi << 1 == desni) {
		 	lijevi <<= 2;
			desni >>= 2;
		}
		else {
			lijevi <<= 1;
			desni >>= 1;
		}

		if(lijevi == 0) {
		  	lijevi = 0x01;
		}

		if(desni == 0) {
		  	desni = 0x80;
		}

		P2 = lijevi + desni;

		delay();
	}
}