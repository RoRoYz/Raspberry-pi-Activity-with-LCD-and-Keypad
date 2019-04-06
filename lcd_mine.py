import RPi.GPIO as GPIO
import time

RS = 7
RW = 8
E  = 25
D4 = 24
D5 = 23
D6 = 18
D7 = 15

LCD_LINE_1 = 0x80 
LCD_LINE_2 = 0xC0 
LCD_LINE_3 = 0x94 
LCD_LINE_4 = 0xD4 

def readBF():
	# unsigned char flag;
 	# IO_DDR2.byte = 0x10; // set direction of LCD data lines to input
 	# IO_PDR2.bit.P24 = 0; // set RS to 0 (instruction register)
 	# IO_PDR5.bit.P53 = 1; // set RW to 1 (read mode)
 	# IO_PDR5.bit.P52 = 1; // set E to 1 (initial state)

	 # do {
		 # flag = IO_PDR2.bit.P23; // read bit 7 of Port 2 (busy flag)
	 # } while (flag);

	 # IO_PDR5.bit.P52 = 0; // set E to 0 (H-L: final state)
 	# IO_DDR2.byte = 0xFF; // set direction of LCD data lines back to output
	flag=1
	GPIO.output(RS,False)		#set direction of LCD data lines to input
	GPIO.output(RW,True)    	#set RS to 0 (instruction register)
	GPIO.output(E,True)     	#set RW to 1 (read mode)
	while(flag)             	#set E to 1 (initial state)
		flag=GPIO.input(D7)		#read bit 7 of Port 2 (busy flag)
	GPIO.output(E,False) 		#set E to 0 (H-L: final state)
		
	
def instCtrl(inst):
	# IO_PDR2.byte = inst >> 4; // transfer the upper 4-bit of inst to 4-bit LCD data line
	# IO_PDR2.bit.P24 = 0; // set RS to 0 (instruction register)
	# IO_PDR5.bit.P53 = 0; // set E to 0 (write mode)
	# IO_PDR5.bit.P52 = 1; // set RW to 1 (initial state)
	# delay(1); // delay for 16 us
	# IO_PDR5.bit.P52 = 0; // set E to 0 (H-L: final state)
	# IO_PDR2.byte = inst; // transfer the lower 4-bit of inst to 4-bit LCD data line
	# IO_PDR2.bit.P24 = 0;
	# IO_PDR5.bit.P53 = 0;
	# IO_PDR5.bit.P52 = 1; // set E to 1 (initial state)
	# delay(1); // delay for 16 us
	# IO_PDR5.bit.P52 = 0; // set E to 0 (H-L: final state)
	# readBF(); // read busy flag
	GPIO.output(D4,(inst>>7)&1)
	GPIO.output(D5,(inst>>6)&1)
	GPIO.output(D6,(inst>>5)&1)			#transfer the upper 4-bit of inst to 4-bit LCD data line
	GPIO.output(D7,(inst>>4)&1)
	GPIO.output(RS,False)				#set RS to 0 (instruction register)
	GPIO.output(RW,False)               #set E to 0 (write mode)
	GPIO.output(E,True)                 #set RW to 1 (initial state)
	sleep(0.000016)                     #delay for 16 us
	GPIO.output(E,False)                #set E to 0 (H-L: final state)
	GPIO.output(D4,(inst>>3)&1)         
	GPIO.output(D5,(inst>>2)&1)         
	GPIO.output(D6,(inst>>1)&1)         #transfer the lower 4-bit of inst to 4-bit LCD data line
	GPIO.output(D7,(inst&1))            
	GPIO.output(RS,False)                
	GPIO.output(RW,False)                                    
	GPIO.output(E,True)					#set E to 1 (initial state)
	sleep(0.000016)						#delay for 16 us
	GPIO.output(E,False)				#set E to 0 (H-L: final state)
	readBF()
	
	
	
def dataCtrl(inst):
	# IO_PDR2.byte = inst >> 4; // transfer the upper 4-bit of inst to 4-bit LCD data line
	# IO_PDR2.bit.P24 = 1; // set RS to 1 (data register)
	# IO_PDR5.bit.P53 = 0; // set E to 0 (write mode)
	# IO_PDR5.bit.P52 = 1; // set RW to 1 (initial state)
	# delay(1); // delay for 16 us
	# IO_PDR5.bit.P52 = 0; // set E to 0 (H-L: final state)
	# IO_PDR2.byte = inst; // transfer the lower 4-bit of inst to 4-bit LCD data line
	# IO_PDR2.bit.P24 = 1;
	# IO_PDR5.bit.P53 = 0;
	# IO_PDR5.bit.P52 = 1; // set E to 1 (initial state)
	# delay(1); // delay for 16 us
	# IO_PDR5.bit.P52 = 0; // set E to 0 (H-L: final state)
	# readBF(); // read busy flag
	GPIO.output(D4,(inst>>7)&1)
	GPIO.output(D5,(inst>>6)&1)
	GPIO.output(D6,(inst>>5)&1)			#transfer the upper 4-bit of inst to 4-bit LCD data line
	GPIO.output(D7,(inst>>4)&1)
	GPIO.output(RS,True)				#set RS to 1 (data register)
	GPIO.output(RW,False)               #set E to 0 (write mode)
	GPIO.output(E,True)                 #set RW to 1 (initial state)
	sleep(0.000016)                     #delay for 16 us
	GPIO.output(E,False)                #set E to 0 (H-L: final state)
	GPIO.output(D4,(inst>>3)&1)         
	GPIO.output(D5,(inst>>2)&1)         
	GPIO.output(D6,(inst>>1)&1)         #transfer the lower 4-bit of inst to 4-bit LCD data line
	GPIO.output(D7,(inst&1))            
	GPIO.output(RS,True)                
	GPIO.output(RW,False)                                    
	GPIO.output(E,True)					#set E to 1 (initial state)
	sleep(0.000016)						#delay for 16 us
	GPIO.output(E,False)				#set E to 0 (H-L: final state)
	readBF()
	

def instCtrl4(inst):
	#IO_PDR2.byte = inst;
	#IO_PDR2.bit.P24 = 0;
	#IO_PDR5.bit.P53 = 0;
	#IO_PDR5.bit.P52 = 1;
	#delay(1);
	#IO_PDR5.bit.P52 = 0;
	GPIO.output(D4,(inst>>3)&1)
	GPIO.output(D5,(inst>>2)&1)
	GPIO.output(D6,(inst>>1)&1)
	GPIO.output(D7,(inst&1))
	GPIO.output(RS,False)
	GPIO.output(RW,False)
	GPIO.output(E,True)
	sleep(0.001)
	GPIO.output(E,False)

def initLCD():
	# delay(1000); // 15 ms LCD startup
	# instCtrl4(0x03);
	# delay(246); // 4.1 ms delay
	# instCtrl4(0x03);
	# delay(6); // 100 us delay
	# instCtrl4(0x03);
	# delay(246); // 4.1 ms delay
	# instCtrl4(0x02);
	# delay(100); // wait for previous instruction to finish
	# instCtrl(0x28); // function set: 4-bit; dual-line
	# instCtrl(0x08); // display off
	# instCtrl(0x01); // display clear
	# instCtrl(0x06); // entry mode: increment; shift off
	# instCtrl(0x0E); // display on; cursor on; blink off 

	sleep(0.015)	#15 ms LCD startup
	instCtrl4(0x03)	
	sleep(0.0041)	#4.1 ms delay
	instCtrl4(0x03)
	sleep(0.0001)	#100 us delay
	instCtrl4(0x03)
	sleep(0.0041)	#4.1 ms delay
	instCtrl4(0x02)
	sleep(0.001)   	#wait for previous instruction to finish
	instCtrl(0x28) 	#function set: 4-bit; dual-line
	instCtrl(0x08) 	#display off
	instCtrl(0x01) 	#display clear
	instCtrl(0x06) 	#entry mode: increment; shift off
	instCtrl(0x0E) 	#display on; cursor on; blink off 

def stringDisplay(string,line)
	message = message.ljust(LCD_WIDTH," ")
	instCtrl(line)
	for x in range(len(string)):
		dataCtrl(ord(message[i])
		

def main():
	GPIO.setmode(GPIO.BCM) 
	
	initLCD()
	
	while True:
 
		# Send some centred test
		stringDisplay("--------------------",LCD_LINE_1,2)
		stringDisplay("Rasbperry Pi",LCD_LINE_2,2)
		stringDisplay("Model B",LCD_LINE_3,2)
		stringDisplay("--------------------",LCD_LINE_4,2)
	 
		sleep(3) # 3 second delay
	 
		stringDisplay("Raspberrypi-spy",LCD_LINE_1,3)
		stringDisplay(".co.uk",LCD_LINE_2,3)
		stringDisplay("",LCD_LINE_3,2)
		stringDisplay("20x4 LCD Module Test",LCD_LINE_4,2)
	 
		sleep(3) # 20 second delay
	 
		# Blank display
		lcd_byte(0x01, LCD_CMD)
	 
		sleep(3) # 3 second delay