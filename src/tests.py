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
        add_test_result(test_name, "FAILURE", "Computer failed to create " + control_type + " code")
        print("Failed " + control_type + " tests protocol")
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
            add_test_result(test_name, "FAILURE", "Computer failed " + control_type + " tests protocol")
            print("Failed " + control_type + " tests protocol")
            return -1
        elif received_code['action'] == Action.HUB_FAILURE:   
            print("Hub failed " + control_type + " tests protocol")
            add_test_result(test_name, "FAILURE", "Hub failed " + control_type + " tests protocol")
            print("Failed " + control_type + " tests protocol")
            return -1
        elif received_code['action'] == Action.JIG_FAILURE:
            print("Jig failed " + control_type + " tests protocol")
            add_test_result(test_name, "FAILURE", "Jig failed " + control_type + " tests protocol")
            print("Failed " + control_type + " tests protocol")
            return -1
        elif received_code['action'] == Action.JH_COMM_FAILURE:
            print("Communication failure between jig and hub when " + control_type + "ing tests")
            add_test_result(test_name, "FAILURE", "Communication failure between jig and hub when " + control_type + "ing tests")
            print("Failed " + control_type + " tests protocol")
            return -1
        elif received_code['action'] == Action.CJ_COMM_FAILURE:
            print("Communication failure between computer and jig when " + control_type + "ing tests")
            add_test_result(test_name, "FAILURE", "Communication failure between computer and jig when " + control_type + "ing tests")
            print("Failed " + control_type + " tests protocol")
            return -1
        else:
            print("Unknown action received from jig when " + control_type + "ing tests")
            add_test_result(test_name, "FAILURE", "Unknown action received from jig when " + control_type + "ing tests")
            print("Failed " + control_type + " tests protocol")
            return -1

    else:
        print("Did not receive a " + control_type + "ed code, code displayed below")
        print(received_code)
        add_test_result(test_name, "FAILURE", "Did not receive a " + control_type + "ed code from jig")
        print("Failed " + control_type + " tests protocol")

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
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.JIG_READ, pin = Pin.LED3, value = Value.NO_VALUE) #TEMPORARY FOR OLD JIG 

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

    jig_read_test(ser, Value.HIGH, "Read Pump Current", "pump current", Pin.PC, True)

    hub_set_jig_read(ser, Value.LOW, "Set Pump Low", "pump", Pin.PUMP, True)

    jig_read_test(ser, Value.LOW, "Read Pump Current", "pump current", Pin.PC, True)




