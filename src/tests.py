from codes import *
from enums import *
from comms import *
def control_tests(ser, control_type):
    """
    Send a control tests (start or end) code and wait for a started or ended tests code back from jig.
    
    Parameters:
    ser (serial.Serial): The serial port to use for communication.
    control_type (str): A string that is either 'start' or 'end'.
    
    Returns:
    int: Returns 1 if successful and -1 if unsuccessful.
    """
    
    if control_type == 'start':
        my_id = Id.START_TESTS
        expected_id = Id.STARTED_TESTS
        test_name = "Start tests protocol"
    elif control_type == 'end':
        my_id = Id.END_TESTS
        expected_id = Id.ENDED_TESTS
        test_name = "End tests protocol"
    else:
        print("Invalid control type")
        return -1

    print("Beginning " + control_type + " tests protocol")

    this_code = create_code(id = my_id)

    if(this_code == 0):
        print("Computer failed to create " + control_type + " code")
        print("Failed " + control_type + " tests protocol")
        add_test_result(test_name, "FAILURE", "Computer failed to create " + control_type + " code")
        return -1

    code_details = "Start tests" if control_type == 'start' else "End tests"
    
    send_success = send_code(this_code, ser, True, code_details=code_details)       

    if(send_success == -1):
        print("Failed " + control_type + " tests protocol")
        add_test_result(test_name, "FAILURE", "Computer error when sending " + control_type + " code")
        return -1
    
    elif(send_success == -2):
        print("Failed " + control_type + " tests protocol")
        add_test_result(test_name, "FAILURE", "Computer did not receive expected receive code from jig")
        return -1

    received_code = read_from_serial(ser, STARTED_SIZE, True)

    if received_code == -1:
        print("Failed " + control_type + " tests protocol")
        add_test_result(test_name, "FAILURE", "Computer did not receive a code from jig within 2 seconds")
        return -1
    
    if received_code == -2:
        print("Failed " + control_type + " tests protocol")
        add_test_result(test_name, "FAILURE", "Computer did not receive expected code size from jig")
        return -1

    if received_code['id'] == expected_id:

        if received_code['action'] == Action.SUCCESS:   
            print("Completed " + control_type + " tests protocol")
            add_test_result(test_name, "SUCCESS", "")
            return 1
        elif received_code['action'] == Action.FAILURE: 
            print("Computer failed " + control_type + " tests protocol")
            print("Failed " + control_type + " tests protocol")
            add_test_result(test_name, "FAILURE", "Computer failed " + control_type + " tests protocol")
            return -1
        elif received_code['action'] == Action.HUB_FAILURE:   
            print("Hub failed " + control_type + " tests protocol")
            print("Failed " + control_type + " tests protocol")
            add_test_result(test_name, "FAILURE", "Hub failed " + control_type + " tests protocol")
            return -1
        elif received_code['action'] == Action.JIG_FAILURE:
            print("Jig failed " + control_type + " tests protocol")
            print("Failed " + control_type + " tests protocol")
            add_test_result(test_name, "FAILURE", "Jig failed " + control_type + " tests protocol")
            return -1
        elif received_code['action'] == Action.JH_COMM_FAILURE:
            print("Communication failure between jig and hub when " + control_type + "ing tests")
            print("Failed " + control_type + " tests protocol")
            add_test_result(test_name, "FAILURE", "Communication failure between jig and hub when " + control_type + "ing tests")
            return -1
        elif received_code['action'] == Action.CJ_COMM_FAILURE:
            print("Communication failure between computer and jig when " + control_type + "ing tests")
            print("Failed " + control_type + " tests protocol")
            add_test_result(test_name, "FAILURE", "Communication failure between computer and jig when " + control_type + "ing tests")
            return -1
        else:
            print("Unknown action received from jig when " + control_type + "ing tests")
            print("Failed " + control_type + " tests protocol")
            add_test_result(test_name, "FAILURE", "Unknown action received from jig when " + control_type + "ing tests")
            return -1

    else:
        print("Did not receive a " + control_type + "ed code, code displayed below")
        print(received_code)
        print("Failed " + control_type + " tests protocol")
        add_test_result(test_name, "FAILURE", "Did not receive a " + control_type + "ed code from jig")

        return -1
    
"""
state is the expected value of the pin, Value.HIGH or Value.LOW
test_name is a string
pin_name is a string
this_pin is a Pin enum
print_success is a boolean, if true print success message for test
returns 1 if successful and -1 if not
"""
def hub_set_jig_read(ser, state, test_name, pin_name, this_pin, print_success):
    print("Starting test: " + test_name)
    
    state_string = ""
    wrong_state_string = ""

    if state == Value.HIGH:
        state_string = "high"
        wrong_state_string = "low"
    elif state == Value.LOW:
        state_string = "low"
        wrong_state_string = "high"
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.HUB_SET, pin = this_pin, value = state)

    if(this_code == 0):
        print("Computer failed to create hub set request code")
        add_test_result(test_name, "FAILURE", "Computer failed to create hub set request code")
        return -1
    
    code_details_string = "Set hub " + pin_name + " pin to " + state_string

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, "FAILURE", "Computer error when reading from serial")
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, "FAILURE", "Computer did not receive expected receive code from jig")
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, "FAILURE", "Computer did not receive a code from jig within 2 seconds")
        return -1
    
    if this_code == -2:
        add_test_result(test_name, "FAILURE", "Computer did not receive expected code size from jig")
        return -1

    if this_code['action'] == Action.HUB_FAILURE:
        add_test_result(test_name, "FAILURE", "Hub failed to set hub " + pin_name + " pin to " + state_string)
        return -1
    elif this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, "FAILURE", "Jig failure when setting hub " + pin_name + " pin to " + state_string)
        return -1
    elif this_code['action'] == Action.JH_COMM_FAILURE:
        add_test_result(test_name, "FAILURE", "Communication failure between jig and hub when setting hub " + pin_name + " pin to " + state_string)
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, "FAILURE", "Communication failure between computer and jig when setting hub " + pin_name + " pin to " + state_string)
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, "FAILURE", "Computer failure when setting hub " + pin_name + " pin to " + state_string)
        return -1
    elif this_code['action'] != Action.SUCCESS:
        print("Unknown action received from jig")
        add_test_result(test_name, "FAILURE", "Unknown action received from jig when setting hub " + pin_name + " pin to " + state_string)
        return -1
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.JIG_READ, pin = this_pin, value = Value.NO_VALUE) #TEMPORARY FOR OLD JIG 

    if(this_code == 0):
        print("Computer failed to create jig read request code")
        return -1
    
    code_details_string = "Read jig " + pin_name + " pin"

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, "FAILURE", "Computer error when reading from serial")
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, "FAILURE", "Computer did not receive expected receive code from jig")
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, "FAILURE", "Computer did not receive a code from jig within 2 seconds")
        return -1
    
    if this_code == -2:
        add_test_result(test_name, "FAILURE", "Computer did not receive expected code size from jig")
        return -1
    
    if this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, "FAILURE", "Jig failure when reading jig " + pin_name + " pin")
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, "FAILURE", "Communication failure between computer and jig when reading jig " + pin_name + " pin")
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, "FAILURE", "Computer failure when reading jig " + pin_name + " pin")
        return -1
    elif this_code['action'] == Action.SUCCESS:
        if this_code['value'] == state:
            if print_success:
                add_test_result(test_name, "SUCCESS", "")
            return 1
        else:
            add_test_result(test_name, "FAILURE", "Jig read " + wrong_state_string + " on hub " + pin_name + " pin when " + state_string + " was expected")
            return -1
    else:
        print("Unexpected action received from jig")
        add_test_result(test_name, "FAILURE", "Unexpected action received from jig when reading jig " + pin_name + " pin")
        return -1
    
    return -1

"""
Function to perform a jig read test on a specified pin.

Parameters:
- ser: Serial object for communication.
- state: Value enum, either Value.HIGH or Value.LOW.
- test_name: String, name of the test.
- pin_name: String, name of the pin.
- this_pin: Pin enum, the pin to be tested.
- print_success is a boolean, if true print success message for test

Returns: 1 if successful, -1 if not
"""
def jig_read_test(ser, state, test_name, pin_name, this_pin, print_success):
    print("Starting test: " + test_name)

    state_string = ""
    wrong_state_string = ""

    if state == Value.HIGH:
        state_string = "high"
        wrong_state_string = "low"
    elif state == Value.LOW:
        state_string = "low"
        wrong_state_string = "high"
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.JIG_READ, pin = this_pin, value = Value.NO_VALUE)

    if(this_code == 0):
        print("Computer failed to create jig read request code")
        add_test_result(test_name, "FAILURE", "Computer failed to create jig read request code")
        time.sleep(2)
        return -1
    
    code_details_string = "Read jig " + pin_name + " pin"

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, "FAILURE", "Computer error when reading from serial")
        time.sleep(2)
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, "FAILURE", "Computer did not receive expected receive code from jig")
        time.sleep(2)
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, "FAILURE", "Computer did not receive a code from jig within 2 seconds")
        time.sleep(2)
        return -1
    
    if this_code == -2:
        add_test_result(test_name, "FAILURE", "Computer did not receive expected code size from jig")
        time.sleep(2)
        return -1
    
    if this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, "FAILURE", "Jig failure when reading jig " + pin_name + " pin")
        time.sleep(2)
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, "FAILURE", "Communication failure between computer and jig when reading jig " + pin_name + " pin")
        time.sleep(2)
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, "FAILURE", "Computer failure when reading jig " + pin_name + " pin")
        time.sleep(2)
        return -1
    elif this_code['action'] == Action.SUCCESS:
        if this_code['value'] == state:
            if print_success:
                add_test_result(test_name, "SUCCESS", "")
            time.sleep(2)
            return 1
        else:
            add_test_result(test_name, "FAILURE", "Jig read " + wrong_state_string + " on hub " + pin_name + " pin when " + state_string + " was expected")
            time.sleep(2)
            return -1
    else:
        print("Unexpected action received from jig")
        add_test_result(test_name, "FAILURE", "Unexpected action received from jig when reading jig " + pin_name + " pin")
        time.sleep(2)
        return -1
    
    time.sleep(2)
    return -1

def jig_set_hub_read(ser, state, test_name, pin_name, this_pin, print_success):
    print("Starting test: " + test_name)
    
    state_string = ""
    wrong_state_string = ""

    if state == Value.HIGH:
        state_string = "high"
        wrong_state_string = "low"
    elif state == Value.LOW:
        state_string = "low"
        wrong_state_string = "high"
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.JIG_SET, pin = this_pin, value = state)

    if(this_code == 0):
        print("Computer failed to create jig set request code")
        add_test_result(test_name, "FAILURE", "Computer failed to create jig set request code")
        return -1
    
    code_details_string = "Set jig " + pin_name + " pin to " + state_string

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, "FAILURE", "Computer error when reading from serial")
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, "FAILURE", "Computer did not receive expected receive code from jig")
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, "FAILURE", "Computer did not receive a code from jig within 2 seconds")
        return -1
    
    if this_code == -2:
        add_test_result(test_name, "FAILURE", "Computer did not receive expected code size from jig")
        return -1

    if this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, "FAILURE", "Jig failure when setting jig " + pin_name + " pin to " + state_string)
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, "FAILURE", "Communication failure between computer and jig when setting jig " + pin_name + " pin to " + state_string)
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, "FAILURE", "Computer failure when setting jig " + pin_name + " pin to " + state_string)
        return -1
    elif this_code['action'] != Action.SUCCESS:
        print("Unknown action received from jig")
        add_test_result(test_name, "FAILURE", "Unknown action received from jig when setting jig " + pin_name + " pin to " + state_string)
        return -1
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.HUB_READ, pin = this_pin, value = Value.NO_VALUE)

    if(this_code == 0):
        print("Computer failed to create hub read request code")
        return -1
    
    code_details_string = "Read hub " + pin_name + " pin"

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, "FAILURE", "Computer error when reading from serial")
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, "FAILURE", "Computer did not receive expected receive code from jig")
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, "FAILURE", "Computer did not receive a code from jig within 2 seconds")
        return -1
    
    if this_code == -2:
        add_test_result(test_name, "FAILURE", "Computer did not receive expected code size from jig")
        return -1
    
    if this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, "FAILURE", "Jig failure when reading hub " + pin_name + " pin")
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, "FAILURE", "Communication failure between computer and jig when reading hub " + pin_name + " pin")
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, "FAILURE", "Computer failure when reading hub " + pin_name + " pin")
        return -1
    elif this_code['action'] == Action.HUB_FAILURE:
        add_test_result(test_name, "FAILURE", "Hub failed to read hub " + pin_name + " pin")
        return -1
    elif this_code['action'] == Action.JH_COMM_FAILURE:
        add_test_result(test_name, "FAILURE", "Communication failure between jig and hub when reading hub " + pin_name + " pin")
        return -1
    elif this_code['action'] == Action.SUCCESS:
        if this_code['value'] == state:
            if print_success:
                add_test_result(test_name, "SUCCESS", "")
            return 1
        elif (this_pin == Pin.TEMP1 or this_pin == Pin.TEMP2 or this_pin == Pin.TEMP3 or this_pin == Pin.TEMP4):
            if state == Value.HIGH_TEMP:
                if this_code['value'] == Value.TEMP_35_TO_40 or this_code['value'] == Value.TEMP_40_TO_45:
                    if print_success:
                        add_test_result(test_name, "SUCCESS", "")
                    return 1
                else:
                    lowest_temp = (this_code['value'].value - Value.TEMP_0_TO_5.value) * 5
                    highest_temp = lowest_temp + 5

                    add_test_result(test_name, "FAILURE", "Hub read a temp from " + str(lowest_temp) + "-" + str(highest_temp) + " degrees on " + pin_name + " pin when high temp of 40 degrees was expected")
                    return -1
            elif state == Value.LOW_TEMP:
                if this_code['value'] == Value.TEMP_25_TO_30 or this_code['value'] == Value.TEMP_30_TO_35:
                    if print_success:
                        add_test_result(test_name, "SUCCESS", "")
                    return 1
                else:
                    lowest_temp = (this_code['value'].value - Value.TEMP_0_TO_5.value) * 5
                    highest_temp = lowest_temp + 5

                    add_test_result(test_name, "FAILURE", "Hub read a temp from " + str(lowest_temp) + "-" + str(highest_temp) + " degrees on " + pin_name + " pin when low temp of 30 degrees was expected")
                    return -1

        else:
            add_test_result(test_name, "FAILURE", "Hub read " + wrong_state_string + " on " + pin_name + " pin when " + state_string + " was expected")
            return -1
    else:
        print("Unexpected action received from hub")
        add_test_result(test_name, "FAILURE", "Unexpected action received from hub when reading hub " + pin_name + " pin")
        return -1
    
    return -1

def test_pump(ser):
    hub_set_jig_read(ser, Value.HIGH, "Set Pump High", "pump", Pin.PUMP, True)

    jig_read_test(ser, Value.HIGH, "Read Pump Current High", "pump current", Pin.PC, True)

    hub_set_jig_read(ser, Value.LOW, "Set Pump Low", "pump", Pin.PUMP, True)

    jig_read_test(ser, Value.LOW, "Read Pump Current Low", "pump current", Pin.PC, True)

#driver_type is 1 for cooling, in1 high, and 2 for heating, in2 high
def test_driver_on(ser, driver_type):
    """
    Test the functionality of the driver by setting the appropriate input pin high and verifying the output, peltier, input, disable, sleep, and fault pins on the jig.

    Parameters:
    ser (serial.Serial): The serial port to use for communication.
    driver_type (int): An integer that is either 1 for cooling or 2 for heating.

    Returns:
    None
    """
    high_out = Pin.NO_PIN
    low_out = Pin.NO_PIN
    high_peltier = Pin.NO_PIN
    low_peltier = Pin.NO_PIN
    high_in = Pin.NO_PIN
    low_in = Pin.NO_PIN
    high_out_string = ""
    low_out_string = ""
    high_peltier_string = ""
    low_peltier_string = ""
    high_in_string = ""
    low_in_string = ""
    driver_type_string = ""

    if driver_type == 1:
        high_out = Pin.OUT1
        low_out = Pin.OUT2
        high_peltier = Pin.PELTIER1
        low_peltier = Pin.PELTIER2
        high_in = Pin.IN1
        low_in = Pin.IN2
        high_out_string = "Out 1"
        low_out_string = "Out 2"
        high_peltier_string = "Peltier 1"
        low_peltier_string = "Peltier 2"
        high_in_string = "In 1"
        low_in_string = "In 2"
        driver_type_string = "Cooling"

    elif driver_type == 2:
        high_out = Pin.OUT2
        low_out = Pin.OUT1
        high_peltier = Pin.PELTIER2
        low_peltier = Pin.PELTIER1
        high_in = Pin.IN2
        low_in = Pin.IN1
        high_out_string = "Out 2"
        low_out_string = "Out 1"
        high_peltier_string = "Peltier 2"
        low_peltier_string = "Peltier 1"
        high_in_string = "In 2"
        low_in_string = "In 1"
        driver_type_string = "Heating"

    #sets the wanted driver input high and reads from jig
    hub_set_jig_read(ser, Value.HIGH, "Driver " + driver_type_string + " : Set " + high_in_string + " High", high_in_string, high_in, True)     

    jig_read_test(ser, Value.HIGH, "Driver " + driver_type_string + " : Read " + high_out_string + " High", high_out_string, high_out, True)

    jig_read_test(ser, Value.HIGH, "Driver " + driver_type_string + " : Read " + high_peltier_string + " High", high_peltier_string, high_peltier, True)

    jig_read_test(ser, Value.LOW, "Driver " + driver_type_string + " : Read " + low_in_string + " Low", low_in_string, low_in, True)

    jig_read_test(ser, Value.LOW, "Driver " + driver_type_string + " : Read " + low_out_string + " Low", low_out_string, low_out, True)

    jig_read_test(ser, Value.LOW, "Driver " + driver_type_string + " : Read " + low_peltier_string + " Low", low_peltier_string, low_peltier, True)

    jig_read_test(ser, Value.HIGH, "Driver " + driver_type_string + " : Read Fault High", "fault", Pin.FAULT, True)

    jig_read_test(ser, Value.LOW, "Driver " + driver_type_string + " : Read Disable Low", "disable", Pin.DIS, True)

    jig_read_test(ser, Value.HIGH, "Driver " + driver_type_string + " : Read Sleep High", "sleep", Pin.SLEEP, True)

    jig_read_test(ser, Value.LOW, "Driver " + driver_type_string + " : Read Iprop Low", "iprop", Pin.IPROP, True)

"""
Function to test that the driver does not run when disable is high or sleep is low.

Parameters:
- ser: Serial object for communication.
- driver_type: String, either "dis" for disable high or "sleep" for sleep low.

The function sets the appropriate pins to the specified states and verifies that the driver does not run by reading the expected low values from the relevant pins.
"""
def test_driver_off(ser, driver_type):
    sleep_value = Value.NO_VALUE
    disable_value = Value.NO_VALUE
    sleep_value_string = ""
    disable_value_string = ""
    test_name = ""

    if driver_type == "dis":
        sleep_value = Value.HIGH
        disable_value = Value.HIGH
        sleep_value_string = "High"
        disable_value_string = "High"
        test_name = "Driver Off with Disable High"

    elif driver_type == "sleep":
        sleep_value = Value.LOW
        disable_value = Value.LOW
        sleep_value_string = "Low"
        disable_value_string = "Low"
        test_name = "Driver Off with Sleep Low"
    
    hub_set_jig_read(ser, Value.HIGH, test_name + " : Set In 1 High", "in 1", Pin.IN1, True)

    hub_set_jig_read(ser, sleep_value, test_name + " : Set Sleep " + sleep_value_string, "sleep", Pin.SLEEP, True)

    hub_set_jig_read(ser, disable_value, test_name + " : Set Disable " + disable_value_string, "disable", Pin.DIS, True)

    if driver_type == "dis":
        print("Waiting 20 seconds for driver to turn off")

        time.sleep(20)
    
    elif driver_type == "sleep":
        print("Waiting 100 seconds for driver to turn off")

        time.sleep(100)

    jig_read_test(ser, Value.LOW, test_name + " : Read In 2 Low", "in 2", Pin.IN2, True)

    jig_read_test(ser, Value.LOW, test_name + " : Read Peltier 1 Low", "peltier 1", Pin.PELTIER1, True)

    jig_read_test(ser, Value.LOW, test_name + " : Read Peltier 2 Low", "peltier 2", Pin.PELTIER2, True)

    jig_read_test(ser, Value.LOW, test_name + " : Read Out 1 Low", "out 1", Pin.OUT1, True)

    jig_read_test(ser, Value.LOW, test_name + " : Read Out 2 Low", "out 2", Pin.OUT2, True)

    jig_read_test(ser, Value.HIGH, test_name + " : Read Fault High", "fault", Pin.FAULT, True)

    jig_read_test(ser, Value.LOW, test_name + " : Read Iprop Low", "iprop", Pin.IPROP, True)

def test_temp(ser, temp_number):
    pin = Pin.NO_PIN

    if temp_number == 1:
        pin = Pin.TEMP1
    elif temp_number == 2:
        pin = Pin.TEMP2
    elif temp_number == 3:
        pin = Pin.TEMP3
    elif temp_number == 4:
        pin = Pin.TEMP4
    else:
        print("Invalid temperature number")
        return -1
    
    jig_set_hub_read(ser, Value.HIGH_TEMP, "Set Temp " + str(temp_number) + " to High Temp", "temp " + str(temp_number), pin, True)

    time.sleep(5)

    jig_set_hub_read(ser, Value.LOW_TEMP, "Set Temp " + str(temp_number) + " to Low Temp", "temp " + str(temp_number), pin, True)