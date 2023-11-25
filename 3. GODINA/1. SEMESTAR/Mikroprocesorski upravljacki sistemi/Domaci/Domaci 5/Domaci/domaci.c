#include <at89c51rc2.h>

volatile char status = 0x00;
volatile int counter = 0x0000;
int counter_set = 0x0FA0;
unsigned char previous_state_P2 = 0x00;

//volatile char counter_250 = 0xFA;
//volatile char counter = 0x10;
//char counter_set = 0x10;

int program_3[7] = {0x81, 0x42, 0x24, 0x18, 0x24, 0x42};
int program_4[12] = {0x01, 0x02, 0x03, 0x05, 0x08, 0x0D, 0x15, 0x22, 0x37, 0x59, 0x90, 0xE9};
char counter_for_program;


void timer_1_interrupt(void) interrupt 3 {
	if(++counter == counter_set)	{
		counter = 0x0000;
	 	status = 0x01;
	}
	
	/*
	if(--counter_250 == 0x00) {
			if(--counter == 0x00) {
				status = 0x01;
				counter = counter_set;		
		}
		counter_250 = 0xFA;
	} 
	*/
}

void diode_activate(unsigned char state, unsigned char* state_P2) {
	previous_state_P2 = *state_P2;
	switch(state) {
		
		case 0x01: case 0x04:
			*state_P2 = ~(*state_P2);
			break;
		
		case 0x08:
			if(*state_P2 == 0x00 || *state_P2 == 0x80) {
				*state_P2 = 0x01;
				break;
			}
			*state_P2 <<= 1;
			break;

		case 0x10:
			if(counter_for_program == 0x06) {
				counter_for_program = 0x00;
			}
			*state_P2 = program_3[counter_for_program++];
			break;

	   case 0x20:
			if(counter_for_program == 0x0C) {
				counter_for_program = 0x00;	
			}
			*state_P2 = program_4[counter_for_program++];
			break;

		default:
			*state_P2 = 0x0000;
			break;		
	}			
}

void main(void) {

	// Inicijalizacija
	char previous_state_P0 = 0xFF;
	unsigned char state_chg_det = 0x00;
	unsigned char previous_state_chg_det = 0x00;
	char what_chg = 0x00;
	unsigned char state_P2 = 0x00;
	char start = 0x00;
	char flag_seventh = 0x00;

	EA = 0;
	TMOD = 0x20;
	TR1 = 1;
	ET1 = 1;
	TL1 = 0x1A;
	TH1 = 0x1A;
	EA = 1;

	P0 = 0xFF;
	P2 = 0x00;


	while(1) {
		if(status) {
			status = 0x00;
			// Zabrana izvrsavanja prije prekida

			state_chg_det = P0 ^ previous_state_P0;
			// XOR kolo detektuje koja se promjena desila
			
			previous_state_P0 = P0;
			// Cuva se trenutno stanje P0 porta
			
			what_chg = state_chg_det & P0;
			// AND kolo detektuje kakva se promjena desila (0->1, 1->0, const.)

			if(!P0_7) {	
				flag_seventh = 0x01;
				state_P2 = 0xFF;
			}
	
			else if((state_chg_det == 0x01 && !what_chg) || start) {
				start = 0x01;

				if(flag_seventh) {
					state_P2 = previous_state_P2;
					flag_seventh = 0x00;
				}

				if(!what_chg) {
					if(state_chg_det == 0x00) {
						diode_activate(previous_state_chg_det, &state_P2);
					}

					else if(state_chg_det == 0x002) {
						state_P2 = 0x00;
						counter = 0x0000;
						counter_set = 0x0FA0;
						start = 0x00;
					//	counter = 0x10;
					//	counter_set = 0x10;
					//	counter_250 = 0xFA;
					}

					else if(state_chg_det == 0x01 ||
							state_chg_det == 0x04 ||
							state_chg_det == 0x08 ||
							state_chg_det == 0x10 ||
							state_chg_det == 0x20) {
						
						state_P2 = 0x00;
					   	counter_for_program = 0x00;
						previous_state_chg_det = state_chg_det;
						diode_activate(state_chg_det, &state_P2);
					}

					else if(state_chg_det == 0x40) {
						counter = 0x0000;
						counter_set = 0x0FA0;
						diode_activate(previous_state_chg_det, &state_P2);
					//	counter = 0x10;
					//	counter_set = 0x10;
					//	counter_250 = 0xFA; 
					//  diode_activate(previous_state_chg_det, &state_P2);
					}	
				}
				else if(what_chg){
					diode_activate(previous_state_chg_det, &state_P2);	
				}
			}		
		}
		P2 = state_P2;			
	}
}