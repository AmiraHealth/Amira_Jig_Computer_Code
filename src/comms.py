from codes import *
from enums import *
import serial
import serial.tools.list_ports
import time
import config

translations = {
    "error_reading_serial": {
        "en": "Computer encountered error reading from serial",
        "cn": "计算机在读取串行时遇到错误"
    },
    "not_expected_receive_code": {
        "en": "Computer did not receive expected receive code from jig",
        "cn": "计算机没有收到来自夹具的预期接收代码"
    },
    "got_receive_code": {
        "en": "Got receive code from jig",
        "cn": "收到来自夹具的接收代码"
    },
    "unexpected_receive_code": {
        "en": "Received a receive code that was not expected, printed below:",
        "cn": "收到意外的接收代码，打印如下："
    },
    "timeout": {
        "en": "Timeout: Did not receive any code within 20 seconds.",
        "cn": "超时：在20秒内未收到任何代码。"
    },
    "expected_code_size": {
        "en": "Received code of expected size below:",
        "cn": "收到预期大小的代码如下："
    },
    "unexpected_code_size": {
        "en": "Did not receive expected code size of {size}. Received size of {received_msg_size}.",
        "cn": "未收到预期大小为 {size} 的代码。收到的大小为 {received_msg_size}。"
    },
    "incorrect_code": {
        "en": "Incorrect code that was received is below.",
        "cn": "收到的错误代码如下。"
    },
    "sent_code": {
        "en": "Sent code: {code_details} - {code}",
        "cn": "发送代码：{code_details} - {code}"
    },
    "computer_receive_code": {
        "en": "Computer receive code",
        "cn": "计算机接收代码"
    }
}

def send_code(code, ser, add_receive_protocols, code_details = ''):     #code in hex string, size in bytes, serial port to be used
    ser.write(bytes.fromhex(code))      #write hex string as actual bytearray type

    print(translations["sent_code"][config.lang].format(code_details=code_details, code=code))  #can add details of code here to debug

    if(add_receive_protocols):
        receive_code = read_from_serial(ser, RECEIVE_SIZE, False)    #check for receive code, don't sende receive code back

        if receive_code == -1:      #error when receiving code
            print(translations["error_reading_serial"][config.lang])
            return -1
        
        elif receive_code == -2:
            print(translations["not_expected_receive_code"][config.lang])
            return -2

        elif receive_code['id'] == Id.JIG_RECEIVE:  #got jig receive code
            print(translations["got_receive_code"][config.lang])

        else:   #received a unexpected receive code
            print(translations["unexpected_receive_code"][config.lang])
            print(receive_code)     
            return -2

#LATER ALSO ADD A TIMER HERE FOR IF DON'T RECEIVE ANY CODE
def read_from_serial(ser, size, add_receive_protocols):      #constantly checks for new messages and returns the first code it finds
    start_time = time.time()  # Record the start time
    
    while True: 
        if time.time() - start_time > 20:  # Check if 1 second has passed
            print(translations["timeout"][config.lang])
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
            print(translations["expected_code_size"][config.lang])
            print(parse_code(code))

            if(add_receive_protocols):  #send a receive code back
                receive_code = create_code(id = Id.COMPUTER_RECEIVE)
                send_code(receive_code, ser, False, code_details=translations["computer_receive_code"][config.lang])

            return parse_code(code)     #return info from parsing code

        elif(code_found):           #did not receive expected code size
            print(translations["unexpected_code_size"][config.lang].format(size=size, received_msg_size=received_msg_size))
            print(translations["incorrect_code"][config.lang])
            print(parse_code(code))

            return -2
             