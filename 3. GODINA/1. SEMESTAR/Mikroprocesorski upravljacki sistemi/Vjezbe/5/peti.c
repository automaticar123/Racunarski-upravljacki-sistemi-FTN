#include <at89c51rc2.h>
// TIMER 1 U OSMOBITNOM ZA DOMACI!!!
volatile char status = 0x00;
char counter = 0x00;

void timer_interrupt_0(void) interrupt 1{
	TL0 = 0x10;
	TH0 = 0x4C;
	
	if(++counter == 20) {
		status = 0x01;
		counter = 0x00;
		return;	
	}						
}

void main(void){
	// Inicijalizacija
	EA = 0;
	TL0 = 0x10;
	TH0 = 0x4C;
	TMOD = 0x01;
	TR0 = 1; 
	ET0 = 1; 
	EA = 1;

	P2 = 0x00;

	while(1) {
		
		if(status){
			P2 = ~P2;
			status = 0x00;	
		}	
	}		
}