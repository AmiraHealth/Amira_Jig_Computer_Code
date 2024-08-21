from enums import *

def create_general_code(*args):
    return ''.join(arg[2:] for arg in args)

def create_code(id = Id.NO_ID, action = Action.FAILURE, mode = Mode.NO_MODE, pin = Pin.NO_PIN, value = Value.NO_VALUE):
    if id == Id.COMPUTER_REQUEST or id == Id.JIG_REQUEST:        #create a request code
        size = 6        #size in bytes of the code (4 1 byte parameters, 1 byte for length, 1 byte for checksum)
        checksum = calculate_checksum_hex(id.hex_value, f"{size:#04x}", mode.hex_value, pin.hex_value, value.hex_value)  #calc checksum

        return create_general_code(id.hex_value, f"{size:#04x}", mode.hex_value, pin.hex_value, value.hex_value, f"{checksum:#04x}")

    elif id == Id.JIG_RESPONSE or id == Id.HUB_RESPONSE:          #create a response code
        size = 0x07     #size in bytes of the code (5 1 byte parameters, 1 byte for length, 1 byte for checksum)
        checksum = calculate_checksum_hex(id.hex_value, f"{size:#04x}", action.hex_value, mode.hex_value, pin.hex_value, value.hex_value) #calculate checksum

        return create_general_code(id.hex_value, f"{size:#04x}", action.hex_value, mode.hex_value, pin.hex_value, value.hex_value, f"{checksum:#04x}")

    elif id == Id.COMPUTER_RECEIVE or id == Id.HUB_RECEIVE or id == Id.JIG_RECEIVE or id == Id.START_TESTS or id == Id.END_TESTS:   #create a receive code or start/end
        size = 0x03    #size in bytes of the code (1 byte id, 1 byte size, 1 byte checksum)
        checksum = calculate_checksum_hex(id.hex_value, f"{size:#04x}") #calculate checksum

        return create_general_code(id.hex_value, f"{size:#04x}", f"{checksum:#04x}")

    elif id == Id.STARTED_TESTS or id == Id.ENDED_TESTS:            #create code indicating if tests started/ended
        size = 0x04         #4 bytes: id, size, action, checksum 
        checksum = calculate_checksum_hex(id.hex_value, f"{size:#04x}", action.hex_value) #calculate checksum

        return create_general_code(id.hex_value, f"{size:#04x}", action.hex_value, f"{checksum:#04x}")  

    else:
        return 0                #doesn't match any correct id type

def parse_code(code):      #get info about code by parsing, for now assuming coming in as string of hex
    codeValues = [int('0x' + code[i:i+2], 16) for i in range(0, len(code), 2)]

    checksum = calculate_checksum_int(codeValues[:-1])        #validate checksum

    if checksum != codeValues[-1]:
        print("Checksum mismatch detected - code corrupted")
        return 0

    id = get_enum_member(Id, codeValues[0])

    if id == Id.COMPUTER_REQUEST or id == Id.JIG_REQUEST:       #return parsed request type code
        return {
            'id': id,
            'size': codeValues[1],
            'mode': get_enum_member(Mode, codeValues[2]),
            'pin': get_enum_member(Pin, codeValues[3]),
            'value': get_enum_member(Value, codeValues[4]),
            'checksum': codeValues[5]
        }
    
    elif id == Id.JIG_RESPONSE or id == Id.HUB_RESPONSE:       #return parsed response type code
        return{
            'id': id,
            'size': codeValues[1],
            'action': get_enum_member(Action, codeValues[2]),
            'mode': get_enum_member(Mode, codeValues[3]),
            'pin': get_enum_member(Pin, codeValues[4]),
            'value': get_enum_member(Value, codeValues[5]),
            'checksum': codeValues[6]
        }
    
    elif id == Id.COMPUTER_RECEIVE or id == Id.HUB_RECEIVE or id == Id.JIG_RECEIVE or id == Id.START_TESTS or id == Id.END_TESTS:   #return parsed receive/start/end type code
        return{
            'id': id,
            'size': codeValues[1],
            'checksum': codeValues[2]
        }
    
    elif id == Id.STARTED_TESTS or id == Id.ENDED_TESTS:     #return parsed started/ended tests code
        return{
            'id': id,
            'size': codeValues[1],
            'action': get_enum_member(Action, codeValues[2]),
            'checksum': codeValues[3]
        }

    else:
        return 0            #code id type does not match any

def calculate_checksum_hex(*args):        #create checksum with hex arguments
    checksum = 0
    for arg in args:
        value = int(arg, 16)
        checksum ^= value

    return checksum

def calculate_checksum_int(list):         #create checksum with list of ints
    checksum = 0
    for arg in list:
        checksum ^= arg

    return checksum