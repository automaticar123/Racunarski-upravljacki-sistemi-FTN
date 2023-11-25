#include "display.h"
#include <intrins.h>

void initP1P3(void) {			//inicijalizacija portova koji se koriste za LCD !

	P1=0xE0;
	P3=0xF9;
}

void wait1s(void) {			  	//posle inicijalizacije portova se ceka 1 sekund
		   
	unsigned char i;

	TMOD = (TMOD&0xF0)|0x01; 	//TMOD TIMER0 U 16 BITNOM REZIMU
	
	for(i=0;i<200;i++) {

		TH0=0xEE;		   		//5ms
		TL0=0x00;				//2 razlicita timera
		TR0=1;				  	//jedan se koristi za lcd - za njega nisu omoguceni prekidi
		while(!TF0) {}		  
			TF0=0;				 
	}						  
}

void wait50micro(void) {

	 TH0=0x0FF;
	 TL0=0xD2;
	 TR0=1;					   //isto kao prethodna samo sto brojis samo 50 mikrosekundi i to samo jednom!
	 	while(!TF0) {}
			TF0=0;	 
}

void wait2ms(void) {
	
	
	TH0=0x0F8;				//isto kao prethodno samo se broji do 2ms
	TL0=0xCD;
	TR0=1;
	while(!TF0) {}
			TF0=0;
			
}

void initDisplay(void) {	 //ovo je inicijalizacija displeja na cetvorobitni rezim rada. 
				 
	initP1P3();	

	wait1s();

	LCD_RS=0;		   			//functionset
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;				 	//kada se inicijalizuje lcd i kada mu se salju naredbe to se radi ovako:
	LCD_D5=1;
	LCD_D4=0;				  	//postavlja se RS na nulu. (RS=1 SAMO KADA SE SALJU PODACI ZA ISPIS NA LCD) 
	LCD_EN=0;				    //posalju se gornja 4 bita naredbe, svaki put kad se salju 4 bita ide EN=1; pa se postave podaci na pinove porta P1; pa EN=0;
							    // ceka se _nop_() - to je funkcija za cekanje- i onda se salju donja 4 bita na isti nacin.
	wait50micro();
		
	LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;
	LCD_D5=1;
	LCD_D4=0;
	LCD_EN=0;
  	
	_nop_();

	LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=1;		
	LCD_D6=0;
	LCD_D5=0;
	LCD_D4=0;
	LCD_EN=0;

	wait50micro();

	//display on, cursor on, blink on
	LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;
	LCD_D5=0;
	LCD_D4=0;
	LCD_EN=0;
  	
	_nop_();

	LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=1;
	LCD_D6=1;
	LCD_D5=1;
	LCD_D4=1;
	LCD_EN=0;

	wait50micro();	

	//display clear

	LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;
	LCD_D5=0;
	LCD_D4=0;
	LCD_EN=0;
  	
	_nop_();

	LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;
	LCD_D5=0;
	LCD_D4=1;
	LCD_EN=0;

	wait2ms();
	wait2ms();

    LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;
	LCD_D5=0;
	LCD_D4=0;
	LCD_EN=0;
  	
	_nop_();

	LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=1;
	LCD_D5=1;
	LCD_D4=0;
	LCD_EN=0;
	wait50micro();	
		   
	wait2ms();
	LCD_BL=1;
}

void clearDisplay(void) {  				//funkcija koja brise sve sto pise na displeju
    LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;
	LCD_D5=0;
	LCD_D4=0;
	LCD_EN=0;
  	
	_nop_();

	LCD_RS=0;		  
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;
	LCD_D5=0;
	LCD_D4=1;
	LCD_EN=0;
	wait2ms();
	wait2ms();

}
	
bit getbit(unsigned char n, unsigned char k){		   //funkcija koja vraca bit koji se nalazi na poziciji n
	unsigned char mask =  1 << k;					   //ova funkcija se koristi za ispisivanje karaktera na lcd
	unsigned char masked_n = n & mask;				   //za svaki karakter se cita svih 8 bita i salju se na lcd u funkciji writeChar
	bit thebit = masked_n >> k;
	return thebit;
}

void writeChar(unsigned char karakter) {   //funkcija koja pise 1 karakter na displej- uzima bite iz karaktera i salje ih na displej
	LCD_RS=1;
	LCD_EN=1;					  
	LCD_D7=getbit(karakter,7);
	LCD_D6=getbit(karakter,6);
	LCD_D5=getbit(karakter,5);
	LCD_D4=getbit(karakter,4);
	LCD_EN=0;
	_nop_();
	LCD_EN=1;
	LCD_D7=getbit(karakter,3);
	LCD_D6=getbit(karakter,2);
	LCD_D5=getbit(karakter,1);
	LCD_D4=getbit(karakter,0);
	LCD_EN=0;
	wait50micro();
}

void writeLine(unsigned char* message) { 	//funkcija koja pise jedan string na displej - iterira kroz string i poziva funkciju writeChar za svako slovo
	unsigned char n=0;
	while(message[n]!='\0') {
		writeChar(message[n]);
		n++;
		}
}

void newLine(void) {		 				//funkcija za prelazak u novi red na lcdu
	LCD_RS=0;
	LCD_EN=1;	
	LCD_D7=1;
	LCD_D6=1;
	LCD_D5=0;
	LCD_D4=0;
	LCD_EN=0;
	_nop_();
	LCD_EN=1;
	LCD_D7=0;
	LCD_D6=0;
	LCD_D5=0;
	LCD_D4=0;
	LCD_EN=0;
	wait2ms();
	wait2ms();
}	