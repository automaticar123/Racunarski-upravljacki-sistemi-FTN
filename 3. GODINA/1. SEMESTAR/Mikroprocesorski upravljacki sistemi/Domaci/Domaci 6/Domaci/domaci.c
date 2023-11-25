#include <at89c51rc2.h>

unsigned char counter = 0x00;
unsigned char status = 0x00;
unsigned char counter_set = 0xC8;
unsigned int var_1 = 0x01;
unsigned int var_2 = 0x02;

int program_3[7] = {0x81, 0x42, 0x24, 0x18, 0x24, 0x42};
int program_4[12] = {0x01, 0x02, 0x03, 0x05, 0x08, 0x0D, 0x15, 0x22, 0x37, 0x59, 0x90, 0xE9};
unsigned char counter_for_program;

unsigned char current_hardware_state_P0_0 = 0x01;
unsigned char current_hardware_state_P0_1 = 0x01;
unsigned char current_hardware_state_P0_2 = 0x01;

unsigned char previous_hardware_state_P0_0 = 0x01;
unsigned char previous_hardware_state_P0_1 = 0x01;
unsigned char previous_hardware_state_P0_2 = 0x01;

unsigned char current_software_state_P0_0 = 0x01;
unsigned char current_software_state_P0_1 = 0x01;
unsigned char current_software_state_P0_2 = 0x01;

unsigned char counter_P0_0 = 0x00;
unsigned char counter_P0_1 = 0x00;
unsigned char counter_P0_2 = 0x00;

void checkCurrentState(unsigned char* current_hardware, unsigned char* previous_hardware, unsigned char* current_software, unsigned char* counter) {
	
	if(*current_hardware == *previous_hardware) {
		if(++(*counter) == 0x05) {
			*counter = 0x00;
			*current_software = *current_hardware;
		}
	}
	else {
		*counter = 0x00;
	}

	return;	
}

void timer_1_interrupt(void) interrupt 3{

	TL1 = 0x00;
	TH1 = 0xEE;

	if(++counter == counter_set){
		status = 0x01;
		counter = 0x00;
	}
	current_hardware_state_P0_0 = P0_0;
	current_hardware_state_P0_1 = P0_1;
	current_hardware_state_P0_2 = P0_2;

	checkCurrentState(&current_hardware_state_P0_0, &previous_hardware_state_P0_0, &current_software_state_P0_0, &counter_P0_0);
	checkCurrentState(&current_hardware_state_P0_1, &previous_hardware_state_P0_1, &current_software_state_P0_1, &counter_P0_1);
	checkCurrentState(&current_hardware_state_P0_2, &previous_hardware_state_P0_2, &current_software_state_P0_2, &counter_P0_2);
	
	previous_hardware_state_P0_0 = current_hardware_state_P0_0;
	previous_hardware_state_P0_1 = current_hardware_state_P0_1;
	previous_hardware_state_P0_2 = current_hardware_state_P0_2;				
}

void diode_activate(unsigned char state, unsigned char* state_P2) {
		
	switch(state) {

		case 0x00:
			*state_P2 = ~(*state_P2);
			break;

		case 0x01:
			if(*state_P2 == 0x00 || *state_P2 == 0x80) {
				*state_P2 = 0x01;
				break;
			}
			*state_P2 <<= 1;
			break;
			
		case 0x02:
			if(counter_for_program == 0x06) {
				counter_for_program = 0x00;
			}
			*state_P2 = program_3[counter_for_program++];
			break;
			
		case 0x03:
			if(counter_for_program == 0x0C) {
				counter_for_program = 0x00;	
			}
			*state_P2 = program_4[counter_for_program++];
			break;

		case 0x04:
			if(var_1 > 0x80) {
				var_1 = 0x01;
			}
			if(var_2 > 0x80) {
				var_2 = 0x01;
			}
			*state_P2 = var_1 + var_2;
			var_1 <<= 1;
			var_2 <<= 1;
			break;
		
		default:
			*state_P2 = 0x0000;
			break;				
	}		
}

void main(void) {

	unsigned char state_P2 = 0x00;
	unsigned char start = 0x00;

	unsigned char current_state_P0_0 = 0x01;
	unsigned char current_state_P0_1 = 0x01;
	unsigned char current_state_P0_2 = 0x01;

	unsigned char previous_state_P0_0 = 0x01;
	unsigned char previous_state_P0_1 = 0x01;
	unsigned char previous_state_P0_2 = 0x01;

	unsigned char P0_0_programs = 0x00;
	unsigned char P0_1_programs = 0x00;
	unsigned char P0_2_programs = 0x00;

	unsigned char change_in_program = 0x00;

	EA = 0;
	TMOD = 0x10; 
	TR1 = 1;
	ET1 = 1;
	TL1 = 0x00;
	TH1 = 0xEE;
	EA = 1;

	P2 = 0x00;
			
	while(1) {
	
		if(status) {
			EA = 0;
			status = 0x00;

			current_state_P0_0 = current_software_state_P0_0;
			current_state_P0_1 = current_software_state_P0_1;
			current_state_P0_2 = current_software_state_P0_2;	

			if(current_state_P0_0 > previous_state_P0_0) {
				if(!P0_0_programs) {
					start = 0x01;
					state_P2 = 0xFF;
					P0_0_programs++;
				}
				else {
					start = 0x00;
					P0_0_programs = 0x00;
					P0_1_programs = 0x00;
					P0_2_programs = 0x00;
					change_in_program = 0x00;
					counter_set = 0xC8;
					counter_for_program = 0x00;
				}
			}

			if(start) {
				// Promjena brzine programa
				 if(current_state_P0_1 > previous_state_P0_1) {
					if(!P0_1_programs) {
						counter_set = 0x64;
						P0_1_programs++;
					}
					else {
						counter_set = 0xC8;
						P0_1_programs = 0x00;	
					}
				}

				// Promjena programa
				if(current_state_P0_2 > previous_state_P0_2) {
					change_in_program++;
					state_P2 = 0x00;
					counter_for_program = 0x00;
					if(P0_2_programs == 0x05) {
						P0_2_programs = 0x00;	
					}
					diode_activate(P0_2_programs++, &state_P2);
				}
				else if(change_in_program) {
					diode_activate(P0_2_programs-1, &state_P2);
				}
			}
			else {
				state_P2 = 0x00;
			}
				
			P2 = state_P2;

			previous_state_P0_0 = current_state_P0_0;
			previous_state_P0_1 = current_state_P0_1;
			previous_state_P0_2 = current_state_P0_2;
			EA = 1;
		}
	} 
}