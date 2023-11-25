#include <at89c51rc2.h>

char* ime = "Nenad\r\n";
char *error = "Error\r\n";
char receive; 
char diode_code;

char *pokZaSlanje;
char buffer[10];
char buffer_it = 0;

void parsirajPoruku() {
	
	if(buffer[0] == '(' &&
	   buffer[1] == 'L' &&
	   buffer[2] == 'E' &&
	   buffer[3] == 'D' &&
	   buffer[4] == ':' &&
	   buffer[5] >= 48  && buffer[5] <= 55 &&
	   buffer[6] == ')') {
	   
	    diode_code = buffer[5] - 48;
	    P2 = 1 << diode_code;
	   }
	else {
		P2 = 0xFF;
	}

	buffer[0] = '\0';
	buffer_it = 0;
}

void asy_interrupt(void) interrupt 4 {
	
	// Recieve
	if(RI) {
		
		RI = 0;	
		receive = SBUF;

		if (receive == '(') {
			buffer_it = 0;
		}

		buffer[buffer_it] = receive;
		buffer_it = (buffer_it + 1) % 10;

		if(receive == ')') {
			parsirajPoruku();
		}
	}
	// Transmit
	if(TI) {
	
	 	TI = 0;	
	}
}


void main(void) {

	// Inicijalizacija
	EA = 0;
	SCON = 0x50;
	PCON = 0x80;
	BDRCON = 0x1C;
	BRL = 0xFD;
	ES = 1;
	EA = 1;

	P2 = 0x00;

	while(1) {
		
	}		
}