#include "parseCommand.h"

unsigned char buffer[10];
unsigned char buffer_pointer = 0x00;
unsigned char receive_buffer;

unsigned char status = 0x00;
unsigned char start = 0x00;
unsigned char state = 0x00;
unsigned char previous_state = 0x00;
unsigned char speed = 0x01;
unsigned char state_P2 = 0x00;

unsigned char counter = 0x00;
unsigned char counter_set = 0xC8;

unsigned char counter_for_program_3 = 0x06;
unsigned char counter_for_program_4 = 0x0C;

void initController(void) {

	P2 = 0x00;

	EA = 0;

	// ----- Inicijalizacija 8-bit UART komunikacije ----- //

	SCON = 0x50;   // SM0 = 1, SM1 = 0, REN = 1
	PCON = 0x80;   // SMOD1 = 1, SMOD0 = 0
	BDRCON = 0x1C; // BRR = 1, TBCK = 1, RBCK = 1
	BRL = 0xFD;	
	ES = 1;        // Enable serial interrupt
	
	// ----- Inicijalizacija tajmera 1 u 16-bit modu rada ----- //
	
	TMOD = 0x10; // T1M1 = 0, T1M0 = 1
	ET1 = 1;     // Enable timer interrupt	
	TL1 = 0x00;
	TH1 = 0xEE;
	TR1 = 1;     // Timer run

	EA = 1;

	initDisplay();
	clearDisplay();
}

void timer_1_interrupt(void) interrupt 3 {

	TL1 = 0x00;
	TH1 = 0xEE;

	if(++counter == counter_set) {
		
		status = 0x01;
		counter = 0x00;
	}

	if(state != previous_state) {
		
		previous_state = state;
		state_P2 = 0x00;
		counter_for_program_3 = 0x06;
		counter_for_program_4 = 0x0C;
	}
}

void uart_interrupt(void) interrupt 4 {

	EA = 0;

	if(RI) {
		
		RI = 0;
		receive_buffer = SBUF;

		if(receive_buffer == '(') {
			buffer_pointer = 0x00;
		}

		buffer[buffer_pointer++] = receive_buffer;
		buffer_pointer = buffer_pointer % 10;

		if(receive_buffer == ')') {
			
			parseCommand();	
		}
	}

	if(TI) {
		
		TI = 0;
	}
	
	EA = 1;
}

void main(void) {

	initController();
	
	while(1) {
	
		if(status) {
			status = 0x00;
			if(start) {
				diode_activate();
			}
		}

		if(state == 0x06) {
			state_P2 = 0xFF;
		}
		
		P2 = state_P2;
	}	
}