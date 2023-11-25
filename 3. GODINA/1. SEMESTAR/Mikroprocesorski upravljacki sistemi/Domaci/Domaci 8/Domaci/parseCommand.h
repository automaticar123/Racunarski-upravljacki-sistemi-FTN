#include "display.h"

extern unsigned char buffer[10];

extern unsigned char status;
extern unsigned char start;
extern unsigned char state;
extern unsigned char previous_state;
extern unsigned char speed;
extern unsigned char state_P2; 

extern unsigned char counter;
extern unsigned char counter_set;

extern unsigned char counter_for_program_3;
unsigned char program_3[7] = {0x81, 0x42, 0x24, 0x18, 0x24, 0x42};
extern unsigned char counter_for_program_4;
unsigned char program_4[12] = {0x01, 0x02, 0x03, 0x05, 0x08, 0x0D, 0x15, 0x22, 0x37, 0x59, 0x90, 0xE9};

void displayState() {
				
/*	writeLine("PR: ");
	writeChar(state + 0x30 - 1);	    */
	if(start) {
		writeLine("Start");
	}
	else {
		writeLine("Stop");
	}
	newLine();
	writeLine("BR: ");
	writeChar(speed + 0x30);
}

void parseCommand(void) {
	
	if(buffer[0] == '(' &&
	   buffer[1] == 'S' &&
	   buffer[2] == 'T' &&
	   buffer[3] == 'A' &&
	   buffer[4] == 'R' &&
	   buffer[5] == 'T' &&
	   buffer[6] == ')') {

	   if(!start) {
	   
			start = 0x01;
			state = 0x01;
			state_P2 = 0x00; 

			wait1s();
			//wait1s();
	
			displayState();
		}

		else {}
	}
	
	else if(buffer[0] == '(' &&
			buffer[1] == 'S' &&
			buffer[2] == 'T' &&
			buffer[3] == 'O' &&
			buffer[4] == 'P' &&
			buffer[5] == ')') {

		if(start) {
			
			start = 0x00;
			state = 0x00;
			previous_state = 0x00;
			speed = 0x01;
			state_P2 = 0x00;
	
			counter_set = 0xC8;
			counter = 0x00;
	
			counter_for_program_3 = 0x06;
			counter_for_program_4 = 0x0C;	
			
			displayState();
		}
		
		else {}	
	}

	else if(buffer[0] == '(' && 
			buffer[1] == 'P' &&
			buffer[2] == 'R' &&
			buffer[3] == ':' &&
			buffer[4] >= '1' && buffer[4] <= '4' &&
			buffer[5] == ')') {

		if(state != buffer[4] - 0x30 + 1 && start) {
			
			state = buffer[4] - 0x30 + 1;
			//displayState();
		}
		
		else {}		
	}
	
	else if(buffer[0] == '(' &&
			buffer[1] == 'B' &&
			buffer[2] == 'R' &&
			buffer[3] == ':' &&
		   (buffer[4] == '1' || buffer[4] == '2') &&
			buffer[5] == ')') {

		if(speed != buffer[4] - 0x30) {
			
			speed = buffer[4] - 0x30;
	
			if(speed == 2) {
				counter = 0x00;
				counter_set = 0x64;
			}
			else {
				counter = 0x00;
				counter_set = 0xC8;
			}

		   	clearDisplay();
			displayState();
		}
		
		else {}
	}
	
	else {
	
		state = 0x06; // Error state
		previous_state = 0x00;
		start = 0x00;
		speed = 0x01;
		
		counter = 0x00;
		counter_set = 0xC8;
		counter_for_program_3 = 0x06;
		counter_for_program_4 = 0x0C;

		clearDisplay();
		writeLine("Error!");
	}		
}

void diode_activate() {
	
	switch(state) {
	
		case 0x01: case 0x02: 
			state_P2 = ~state_P2;
			break;

		case 0x03:
			if(state_P2 == 0x00 || state_P2 == 0x80) {
			
				state_P2 = 0x01;
				break;
			}	
			state_P2 <<= 1;
			break;

		case 0x04:
			if(counter_for_program_3 == 0x06) {
				counter_for_program_3 = 0x00;	
			}
			state_P2 = program_3[counter_for_program_3++];
			break;			

		case 0x05:
			if(counter_for_program_4 == 0x0C) {
				counter_for_program_4 = 0x00;	
			}
			state_P2 = program_4[counter_for_program_4++];
			break;

		default:
			state_P2 = 0xFF;
			break;
	}
}
