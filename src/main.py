import serial
import serial.tools.list_ports
from enums import *
from codes import *
from codes import create_code
from comms import *
from tests import *
import time
import pandas as pd
import sys  # Add this import to handle exiting the program

print("Select language (1 for English, 2 for Chinese): 选择语言（1为英语，2为中文）：")
language = input()

translations = {
    "available_ports": {
        "en": "The following ports are available:",
        "cn": "以下端口可用："
    },
    "select_port": {
        "en": "Select a port by index: ",
        "cn": "选择一个端口索引："
    },
    "selected_port": {
        "en": "Selected port {}: {}",
        "cn": "选择的端口 {}: {}"
    }
}

lang_code = "cn" if language == "2" else "en"

#port selection and set up
ports = list(serial.tools.list_ports.comports())    #get available ports

print(translations["available_ports"][lang_code])   #list all available ports
for i,p in enumerate(ports):   
    print(i, end=": ")
    print(p)

port_index = int(input(translations["select_port"][lang_code]))     #prompt to select port

port = str(ports[port_index].device)
print(translations["selected_port"][lang_code].format(port_index, port))

test_results = test_results.iloc[0:0]   #clear test results dataframe

ser1 = serial.Serial(port, 115200, timeout=1)    #open serial port

print("")

attempts = 3
for attempt in range(attempts):
    result = control_tests(ser1, "start")
    if result != -1:
        break  #Successful
    else:
        print(f"Attempt {attempt + 1} to start tests failed.")
        print("")
        if attempt == attempts - 1:
            print("All attempts to start tests failed")
            print_test_results()
            print("Unplug and replug the USB cable for the device to restart the devices and try again")
            print("If issue persists due to jig to hub communication, there may be a fault in the B1, B2, L1, or L2 pins on the hub or on the jig")
            print("If issue persists due to computer to jig communication, there may be a fault in the RXD or TXD pins on the jig")
            print("Exiting program")
            sys.exit(1) 

time.sleep(3)

# hub_set_jig_read(ser1, Value.HIGH, "Set LED 3 High", "led 3", Pin.LED3, True)

# hub_set_jig_read(ser1, Value.LOW, "Set LED 3 Low", "led 3", Pin.LED3, True)
 
# jig_read_test(ser1, Value.LOW, "Led 3 Read Only", "led 3", Pin.LED3, True)

# hub_set_jig_read(ser1, Value.HIGH, "Set Fan High", "fan", Pin.FAN, True)

# hub_set_jig_read(ser1, Value.LOW, "Set Fan Low", "fan", Pin.FAN, True)

# hub_set_jig_read(ser1, Value.HIGH, "Set Pump High", "pump", Pin.PUMP, True)

# hub_set_jig_read(ser1, Value.LOW, "Set Pump Low", "pump", Pin.PUMP, True)

# jig_set_hub_read(ser1, Value.HIGH, "Set Float1 High", "float 1", Pin.FLOAT1, True)

# jig_set_hub_read(ser1, Value.LOW, "Set Float1 Low", "float 1", Pin.FLOAT1, True)

# hub_set_jig_read(ser1, Value.HIGH, "Driver Cooling : Set In1 High", "in 1", Pin.IN1, True)

# hub_set_jig_read(ser1, Value.HIGH, "Driver Heating : Set In2 High", "in 1", Pin.IN2, True)

# test_driver_on(ser1, 1) #test cooling driver

# test_driver_on(ser1, 2) #test heating driver

# test_driver_off(ser1, "dis")

# hub_set_jig_read(ser1, Value.HIGH, "Reset Sleep High", "sleep", Pin.SLEEP, True)

# hub_set_jig_read(ser1, Value.LOW, "Reset Disable Low", "disable", Pin.DIS, True)

# hub_set_jig_read(ser1, Value.HIGH, "Reset In1 High", "in 1", Pin.IN1, True)

# test_driver_off(ser1, "sleep")

# test_temp(ser1, 1)

# test_temp(ser1, 2)

# test_temp(ser1, 3)

# test_temp(ser1, 4)

control_tests(ser1, "end")

print_test_results()