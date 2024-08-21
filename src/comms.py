from codes import *
from enums import *
import serial
import serial.tools.list_ports
import time

def send_code(code, ser, add_receive_protocols, code_details = ''):     #code in hex string, size in bytes, serial port to be used
    ser.write(bytes.fromhex(code))      #write hex string as actual bytearray type

    print("Sent code: " + code_details + " - " + code)  #can add details of code here to debug

    if(add_receive_protocols):
        receive_code = read_from_serial(ser, RECEIVE_SIZE, False)    #check for receive code, don't sende receive code back

        if receive_code == -1:      #error when receiving code
            print("Computer encountered error reading from serial")   
            return -1
        
        elif receive_code == -2:
            print("Computer did not receive expected receive code from jig")
            return -2

        elif receive_code['id'] == Id.JIG_RECEIVE:  #got jig receive code
            print("Got receive code from jig")

        else:   #received a unexpected receive code
            print("Received a receive code that was not expected, printed below.")
            print(receive_code)     #MAKE A FUNCTION TO PRINT A CODE WELL FORMATTED?
            return -2

#LATER ALSO ADD A TIMER HERE FOR IF DON'T RECEIVE ANY CODE
def read_from_serial(ser, size, add_receive_protocols):      #constantly checks for new messages and returns the first code it finds
    start_time = time.time()  # Record the start time
    
    while True: 
        if time.time() - start_time > 10:  # Check if 1 second has passed
            print("Timeout: Did not receive any code within 4 seconds.")
            return -1

        received_msg_size = 10;  
        rx_pos = 0;     #current position in received message
        code = ''   #empty code
        code_found = False  #true once have received code

        while(ser.in_waiting > 0 and rx_pos < received_msg_size):     #retrieve the first code in waiting as a hex string
            c = ser.read(1).hex()   #populate code character by character
 
            if(rx_pos == 1):
                received_msg_size = int(c, 16)   #get size of message from first byte
  
            code += c    

            rx_pos += 1

            if(rx_pos == received_msg_size):
                code_found = True

        # Start of Selection
        if (received_msg_size == size and code_found):    #received expected code size
            print("Received expected code size, code below:")
            print(parse_code(code))

            if(add_receive_protocols):  #send a receive code back
                receive_code = create_code(id = Id.COMPUTER_RECEIVE)
                send_code(receive_code, ser, False, code_details='Computer receive code')

            return parse_code(code)     #return info from parsing code

        elif(code_found):           #did not receive expected code size
            print("Did not receive expected code size of " + str(size) + ". Received size of " + str(received_msg_size) + ".")

            print("Incorrect code that was received is below.")
            print(parse_code(code))

            return -2
             