#include <at89c51rc2.h>

unsigned char counter = 0;
unsigned char proslaSekunda = 0;
unsigned char trenutnoP0_0HardverskoStanje = 1;
unsigned char prethodnoP0_0HardverskoStanje = 1;
unsigned char brojacZaTaster = 0;
unsigned char trenutnoP0_0SoftverskoStanje = 1;  

void t0_interrupt(void) interrupt 1 {
	
	TL0 = 0x01;
	TH0 = 0xEE;

	if(++counter == 200) {
		proslaSekunda = 1;
		counter = 0;	
	}

	trenutnoP0_0HardverskoStanje = P0_0;

	if(trenutnoP0_0HardverskoStanje == prethodnoP0_0HardverskoStanje) {

		if(++brojacZaTaster == 5) {
			trenutnoP0_0SoftverskoStanje = trenutnoP0_0HardverskoStanje;
			brojacZaTaster = 0;
		}
	}
	else {
		brojacZaTaster = 0;
	}

	prethodnoP0_0HardverskoStanje = trenutnoP0_0HardverskoStanje;	
}
	
void main(void) {

	unsigned char trenutnoP0_0 = 1;
	unsigned char prethodnoP0_0 = 1; 
	unsigned char start = 0;
	P2 = 0x00;
	
	//EA = 0;
	TL0 = 0x01;
	TH0 = 0xEE;
	TMOD = 0x01;
	ET0 = 1;	
	TR0 = 1;
	EA = 1;

	while(1) {
		
		trenutnoP0_0 = trenutnoP0_0SoftverskoStanje;

		if(prethodnoP0_0 > trenutnoP0_0) {
			start = ~start;
		}

		if(start) {
			if(proslaSekunda) {
				P2 = ~P2;
				proslaSekunda = 0;
			}
		}
		else {
			P2 = 0;
		}

		prethodnoP0_0 = trenutnoP0_0;
	}
}