#include <at89c51rc2.h>

unsigned char buffer[10];
unsigned char buffer_pointer = 0x00;
unsigned char error_flag = 0;

unsigned char status = 0x00;
unsigned char start = 0x00;
unsigned char state = 0x00;
unsigned char previous_state = 0x00;
unsigned char speed = 0x01;
unsigned char state_P2 = 0x00;

unsigned char counter = 0x00;
unsigned char counter_set = 0xC8;

unsigned char counter_for_program_3 = 0x06;
unsigned char program_3[7] = {0x81, 0x42, 0x24, 0x18, 0x24, 0x42};
unsigned char counter_for_program_4 = 0x0C;
unsigned char program_4[12] = {0x01, 0x02, 0x03, 0x05, 0x08, 0x0D, 0x15, 0x22, 0x37, 0x59, 0x90, 0xE9};

unsigned char test;

void init(void) {
	
	EA = 0;	

	SCON = 0x50; // 8-bit UART sa promjenljivim baud rate-om
	PCON = 0x80;
	BDRCON = 0x1C;
	BRL = 0xFD;
	ES = 1;

	TMOD = 0x10; // Timer 1 u 16-bit modu rada
	TR1 = 1;
	ET1 = 1;
	TL1 = 0x00;
	TH1 = 0xEE;

	EA = 1;

	P2 = 0x00;
}

void diode_activate(unsigned char state) {

	switch(state) {
	
		case 0x01 : case 0x02 :
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

void parseCommand(void) {

	if(buffer[0] == '(' &&
	   buffer[1] == 'S' &&
	   buffer[2] == 'T' &&
	   buffer[3] == 'A' &&
	   buffer[4] == 'R' &&
	   buffer[5] == 'T' &&
	   buffer[6] == ')' && start != 0x01) {
	   
	  	start = 0x01;
		state = 0x01;
		state_P2 = 0x00;
	}
	
	else if(buffer[0] == '(' &&
	   buffer[1] == 'S' &&
	   buffer[2] == 'T' &&
	   buffer[3] == 'O' &&
	   buffer[4] == 'P' &&
	   buffer[5] == ')' && start != 0x00) {
	   
		start = 0x00;
		state = 0x00;
		speed = 0x01;
		previous_state = 0x00;
		state_P2 = 0x00;
		counter_set = 0xC8;
		counter_for_program_3 = 0x06;
		counter_for_program_4 = 0x0C;
		counter = 0x00;	
	}

	else if(buffer[0] == '(' && 
			buffer[1] == 'P' &&
			buffer[2] == 'R' &&
			buffer[3] == ':' &&
			buffer[4] >= '1' && buffer[4] <= '4' &&
			buffer[5] == ')' &&
			state != buffer[4] - 48 + 1 && start) {
			
		state = buffer[4] - 48 + 1;		
	}

	else if(buffer[0] == '(' &&
			buffer[1] == 'B' &&
			buffer[2] == 'R' &&
			buffer[3] == ':' &&
			(buffer[4] == '1' || buffer[4] == '2') &&
			buffer[5] == ')' && speed != buffer[4] - 48 && start) {

		speed = buffer[4] - 0x30;
		if(speed == 2) {
			counter = 0x00;
			counter_set = 0x64;
		}
		else {
			counter = 0x00;
			counter_set = 0xC8;
		}
	}
	else if(buffer[0] == '(' &&
			buffer[1] == 'P' &&
			buffer[2] == '?' &&
			buffer[3] == ')') {
			
			SBUF = 0x30 + state - 1;
			}
	else {
		state = 0x06; // Error state
		start = 0x00;
		speed = 0x01;
		previous_state = 0x00;
		counter_set = 0xC8;
		counter_for_program_3 = 0x06;
		counter_for_program_4 = 0x0C;
		counter = 0x00;
	}
}

void timer1_interrupt(void) interrupt 3{
	
	TL1 = 0x00;
	TH1 = 0xEE;

	if(++counter == counter_set) {
		status = 0x01;
		counter = 0x00;

		if(state != previous_state) {
			previous_state = state;
			state_P2 = 0x00;
			counter_for_program_3 = 0x06;
			counter_for_program_4 = 0x0C;
		}
	}	
}

void asy_interrupt(void) interrupt 4{
	EA = 0;

	if(TI) {
		TI = 0;
	}

	if(RI) {
		
		test = SBUF;
		RI = 0;
		
		if(SBUF == '(') {

			buffer_pointer = 0;
		}

		buffer[buffer_pointer++] = SBUF;
		buffer_pointer = buffer_pointer % 10;

		if(SBUF == ')') {

			parseCommand();
		}
	}
	EA = 1;			
}

void main(void) {

	init();									

	while(1){
		
		if(status) {
			status = 0x00;
			if(start) {
				diode_activate(state);
			}
		}
		if(state == 0x06) {
			state_P2 = 0xFF;
		}
		P2 = state_P2;
	}

}