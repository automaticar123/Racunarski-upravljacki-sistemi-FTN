#include <at89c51rc2.h>
#include <intrins.h>

#define LCD_EN  P3_2
#define LCD_RS  P3_3

#define LCD_DB7 P1_0
#define LCD_DB6 P1_1
#define LCD_DB5 P1_2
#define LCD_DB4 P1_3

#define LDC_BL  P1_4

void waitSec(void) {
	
	int i;
	TH0 = 0x4B;
	TL0 = 0xFD;
	TMOD = (TMOD & 0xF0) | 0x01;
	TR0 = 1;

	for(i = 0; i < 20; i++) {
		while(!TF0) {}
		TF0 = 0;
		TH0 = 0x4B;
		TL0 = 0xFD;
	}

	TF0 = 0;
	TR0 = 0;
}

void wait50us(void) {
	
	TH0 = 0xFF;
	TL0 = 0xD2;
	TR0 = 1;

	while(!TF0) {}

	TF0 = 0;
	TR0 = 0;
}

void wait2ms(void) {

	TH0 = 0xF8;
	TL0 = 0xCD;
	TR0 = 1;
	
	while(!TF0) {}
	
	TF0 = 0;
	TR0 = 0;	
}

void initializeDisplay(void) {
	
	waitSec();

	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 0;
	LCD_DB6 = 0;
	LCD_DB5 = 1;
	LCD_DB4 = 0;
	LCD_EN = 0;

	wait50us();

	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 0;
	LCD_DB6 = 0;
	LCD_DB5 = 1;
	LCD_DB4 = 0;
	LCD_EN = 0;

	_nop_();

	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 1;
	LCD_DB6 = 0;
	LCD_DB5 = 0;
	LCD_DB4 = 0;
	LCD_EN = 0;

	wait50us();

	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 0;
	LCD_DB6 = 0;
	LCD_DB5 = 0;
	LCD_DB4 = 0;
	LCD_EN = 0;

	_nop_();

   	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 1;
	LCD_DB6 = 1;
	LCD_DB5 = 1;
	LCD_DB4 = 1;
	LCD_EN = 0;

	wait50us();

	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 0;
	LCD_DB6 = 0;
	LCD_DB5 = 0;
	LCD_DB4 = 0;
	LCD_EN = 0;

	_nop_();

	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 0;
	LCD_DB6 = 0;
	LCD_DB5 = 0;
	LCD_DB4 = 1;
	LCD_EN = 0;

	wait2ms();
	wait2ms();

	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 0;
	LCD_DB6 = 0;
	LCD_DB5 = 0;
	LCD_DB4 = 0;
	LCD_EN = 0;

	_nop_();

	LCD_EN = 1;
	LCD_RS = 0;
	LCD_DB7 = 0;
	LCD_DB6 = 1;
	LCD_DB5 = 1;
	LCD_DB4 = 0;
	LCD_EN = 0;

	wait50us();
	
	wait2ms();

	LDC_BL = 1;
}

bit getBit(unsigned char character, unsigned char shift) {
		
	return (character & (1 << shift)) >> shift;
}

void writeChar(unsigned char character) {
	
	LCD_EN = 1;
	LCD_RS = 1;
	LCD_DB7 = getBit(character, 7);
	LCD_DB6 = getBit(character, 6);
	LCD_DB5 = getBit(character, 5);
	LCD_DB4 = getBit(character, 4);
	LCD_EN = 0;	

	_nop_();

	LCD_EN = 1;
	LCD_RS = 1;
	LCD_DB7 = getBit(character, 3);
	LCD_DB6 = getBit(character, 2);
	LCD_DB5 = getBit(character, 1);
	LCD_DB4 = getBit(character, 0);
	LCD_EN = 0;
								   
	wait50us();
}

void writeLine(unsigned char* str) {

	char i = 0;

	while(*(str+i) != '\0') {
		writeChar(*(str + i));
		i++;		
	}
}

void main(void) {

	initializeDisplay();
	
	writeLine("Nenad\0");

	while(1) {}
}