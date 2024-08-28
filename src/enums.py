from enum import Enum
import pandas as pd

#Global variables
REQUEST_SIZE = 6
RECEIVE_SIZE = 3    #also used for start/end tests codes
START_SIZE = 3
END_SIZE = 3
RESPONSE_SIZE = 7
STARTED_SIZE = 4        #used for started/ended tests codes
ENDED_SIZE = 4

columns = ['test name', 'result', 'reason']
test_results = pd.DataFrame(columns=columns)            #dataframe to store test name, result, reason

class HexEnum(Enum):
    @property
    def hex_value(self):
        return f"{self.value:#04x}"

class Id(HexEnum):         #type of code
    NO_ID = 0
    COMPUTER_REQUEST = 1
    JIG_REQUEST = 2
    COMPUTER_RECEIVE = 3
    HUB_RECEIVE = 4
    JIG_RECEIVE = 5
    HUB_RESPONSE = 6
    JIG_RESPONSE = 7
    START_TESTS = 8
    END_TESTS = 9
    STARTED_TESTS = 10
    ENDED_TESTS = 11

class Action(HexEnum):         #action completed success/failure
    FAILURE = 0
    SUCCESS = 1
    HUB_FAILURE = 2
    JIG_FAILURE = 3
    JH_COMM_FAILURE = 4
    CJ_COMM_FAILURE = 5

class Mode(HexEnum):       #type of action to be completed
    NO_MODE = 0
    JIG_SET = 1
    JIG_READ = 2
    HUB_SET = 3
    HUB_READ = 4

class Pin(HexEnum):        #universal pin corresponding to target component of test
    NO_PIN = 0
    PUMP = 1
    FAN = 2
    PC = 3
    OUT1 = 4
    OUT2 = 5
    TEMP4 = 6
    TEMP3 = 7
    TEMP2 = 8
    TEMP1 = 9
    FAULT = 10
    IN1 = 11
    IN2 = 12
    DIS = 13
    SLEEP = 14
    IPROP = 15
    LED3 = 16
    LED2 = 17
    LED1 = 18
    FLOAT2 = 19
    FLOAT1 = 20
    VOLT5 = 21
    VOLT3V3 = 22
    GND = 23
    PELTIER1 = 24
    PELTIER2 = 25
    BUTTON1 = 26
    BUTTON2 = 27

class Value(HexEnum):  #value needed for this code
    NO_VALUE = 0
    HIGH = 1
    LOW = 2
    HIGH_TEMP = 3
    LOW_TEMP = 4
    TEMP_0_TO_5 = 5
    TEMP_5_TO_10 = 6
    TEMP_10_TO_15 = 7
    TEMP_15_TO_20 = 8
    TEMP_20_TO_25 = 9
    TEMP_25_TO_30 = 10
    TEMP_30_TO_35 = 11
    TEMP_35_TO_40 = 12
    TEMP_40_TO_45 = 13
    TEMP_45_TO_50 = 14
    TEMP_50_TO_55 = 15
    TEMP_55_TO_60 = 16
    TEMP_60_TO_65 = 17
    TEMP_65_TO_70 = 18
    TEMP_70_TO_75 = 19
    TEMP_75_TO_80 = 20
    TEMP_80_TO_85 = 21
    TEMP_85_TO_90 = 22
    TEMP_90_TO_95 = 23
    TEMP_95_TO_100 = 24
    UNKNOWN_TEMP = 25

def get_enum_member(enum_class, value): #return specific enum's member by integer value
    """
    Get the enum member corresponding to the integer value.

    Parameters:
    enum_class (Enum): The enum class to search in.
    value (int): The integer value corresponding to the enum member.

    Returns:
    Enum: The enum member with the given value.
    """
    
    for member in enum_class:
        if member.value == value:
            return member
    raise ValueError(f"No enum member found for value {value}")

def print_test_results():
    """
    Print the test results in the specified format.

    Parameters:
    test_results (DataFrame): The dataframe containing the test results.
    """
    for index, row in test_results.iterrows():
        if row['Result'] == 'SUCCESS':
            print(f"Test: {row['Test']}, Result: {row['Result']}")
        else:
            print(f"Test: {row['Test']}, Result: {row['Result']}, Reason: {row['Reason']}")

def add_test_result(this_name, this_result, this_reason):
    """
    Add a row to the test_results dataframe.

    Parameters:
    this_name (str): The name of the test.
    this_result (str): The result of the test.
    this_reason (str): The reason for the result.
    """
    global test_results

    new_row = pd.DataFrame([{'Test': this_name, 'Result': this_result, 'Reason': this_reason}])
    test_results = pd.concat([test_results, new_row], ignore_index=True)

    print("Test Completed - Test: " + this_name + ", Result: " + this_result + ", Reason: " + this_reason)
    print("")