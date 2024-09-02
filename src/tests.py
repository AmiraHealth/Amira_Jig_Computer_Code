from codes import *
from enums import *
from comms import *
import config

translations = {
    "invalid_control_type": {
        "en": "Invalid control type",
        "cn": "无效的控制类型"
    },
    "beginning_tests_protocol": {
        "en": "Beginning {} tests protocol",
        "cn": "开始{}测试协议"
    },
    "failed_to_create_code": {
        "en": "Computer failed to create {} code",
        "cn": "计算机未能创建{}代码"
    },
    "failed_tests_protocol": {
        "en": "Failed {} tests protocol",
        "cn": "测试协议失败"
    },
    "computer_error_sending_code": {
        "en": "Computer error when sending {} code",
        "cn": "发送{}代码时计算机错误"
    },
    "did_not_receive_expected_code": {
        "en": "Computer did not receive expected receive code from jig",
        "cn": "计算机未收到来自夹具的预期接收代码"
    },
    "did_not_receive_code_within_2_seconds": {
        "en": "Computer did not receive a code from jig within 2 seconds",
        "cn": "计算机在2秒内未收到来自夹具的代码"
    },
    "did_not_receive_expected_code_size": {
        "en": "Computer did not receive expected code size from jig",
        "cn": "计算机未收到来自夹具的预期代码大小"
    },
    "completed_tests_protocol": {
        "en": "Completed {} tests protocol",
        "cn": "完成{}测试协议"
    },
    "computer_failed_tests_protocol": {
        "en": "Computer failed {} tests protocol",
        "cn": "计算机未能完成{}测试协议"
    },
    "hub_failed_tests_protocol": {
        "en": "Hub failed {} tests protocol",
        "cn": "集线器未能完成{}测试协议"
    },
    "jig_failed_tests_protocol": {
        "en": "Jig failed {} tests protocol",
        "cn": "夹具未能完成{}测试协议"
    },
    "jh_comm_failure": {
        "en": "Communication failure between jig and hub when {}ing tests",
        "cn": "夹具和集线器之间的通信失败，{}测试时"
    },
    "cj_comm_failure": {
        "en": "Communication failure between computer and jig when {}ing tests",
        "cn": "计算机和夹具之间的通信失败，{}测试时"
    },
    "unknown_action_received": {
        "en": "Unknown action received from jig when {}ing tests",
        "cn": "从夹具收到未知操作，{}测试时"
    },
    "did_not_receive_code": {
        "en": "Did not receive a {}ed code, code displayed below",
        "cn": "未收到{}代码，代码如下"
    },
    "start_tests": {
        "en": "Start tests",
        "cn": "开始测试"
    },
    "end_tests": {
        "en": "End tests",
        "cn": "结束测试"
    },
    "start_tests_protocol": {
        "en": "Start tests protocol",
        "cn": "开始测试协议"
    },
    "end_tests_protocol": {
        "en": "End tests protocol",
        "cn": "结束测试协议"
    },
    "starting_test": {
        "en": "Starting test: {}",
        "cn": "开始测试：{}"
    },
    "failed_to_create_hub_set_code": {
        "en": "Computer failed to create hub set request code",
        "cn": "计算机未能创建集线器设置请求代码"
    },
    "computer_error_reading_serial": {
        "en": "Computer error when reading from serial",
        "cn": "计算机读取串行时出错"
    },
    "hub_failed_to_set_pin": {
        "en": "Hub failed to set hub {} pin to {}",
        "cn": "集线器未能将集线器{}引脚设置为{}"
    },
    "jig_failure_setting_pin": {
        "en": "Jig failure when setting hub {} pin to {}",
        "cn": "设置集线器{}引脚时夹具失败"
    },
    "jh_comm_failure_setting_pin": {
        "en": "Communication failure between jig and hub when setting hub {} pin to {}",
        "cn": "设置集线器{}引脚时夹具和集线器之间的通信失败"
    },
    "cj_comm_failure_setting_pin": {
        "en": "Communication failure between computer and jig when setting hub {} pin to {}",
        "cn": "设置集线器{}引脚时计算机和夹具之间的通信失败"
    },
    "computer_failure_setting_pin": {
        "en": "Computer failure when setting hub {} pin to {}",
        "cn": "设置集线器{}引脚时计算机失败"
    },
    "unknown_action_received_setting_pin": {
        "en": "Unknown action received from jig when setting hub {} pin to {}",
        "cn": "设置集线器{}引脚时从夹具收到未知操作"
    },
    "failed_to_create_jig_read_code": {
        "en": "Computer failed to create jig read request code",
        "cn": "计算机未能创建夹具读取请求代码"
    },
    "jig_failure_reading_pin": {
        "en": "Jig failure when reading jig {} pin",
        "cn": "读取夹具{}引脚时夹具失败"
    },
    "cj_comm_failure_reading_pin": {
        "en": "Communication failure between computer and jig when reading jig {} pin",
        "cn": "读取夹具{}引脚时计算机和夹具之间的通信失败"
    },
    "computer_failure_reading_pin": {
        "en": "Computer failure when reading jig {} pin",
        "cn": "读取夹具{}引脚时计算机失败"
    },
    "jig_read_wrong_state": {
        "en": "Jig read {} on hub {} pin when {} was expected",
        "cn": "夹具读取集线器{}引脚上的{}，预期为{}"
    },
    "unexpected_action_received_reading_pin": {
        "en": "Unexpected action received from jig when reading jig {} pin",
        "cn": "读取夹具{}引脚时从夹具收到意外操作"
    },
    "high": {
        "en": "high",
        "cn": "高"
    },
    "low": {
        "en": "low",
        "cn": "低"
    },
    "set_hub_pin": {
        "en": "Set hub {} pin to {}",
        "cn": "将集线器{}引脚设置为{}"
    },
    "read_jig_pin": {
        "en": "Read jig {} pin",
        "cn": "读取夹具{}引脚"
    },
    "success": {
        "en": "SUCCESS",
        "cn": "成功"
    },
    "failure": {
        "en": "FAILURE",
        "cn": "失败"
    },
    "failed_to_create_jig_set_code": {
        "en": "Computer failed to create jig set request code",
        "cn": "计算机未能创建夹具设置请求代码"
    },
    "set_jig_pin": {
        "en": "Set jig {} pin to {}",
        "cn": "将夹具{}引脚设置为{}"
    },
    "failed_to_create_hub_read_code": {
        "en": "Computer failed to create hub read request code",
        "cn": "计算机未能创建集线器读取请求代码"
    },
    "read_hub_pin": {
        "en": "Read hub {} pin",
        "cn": "读取集线器{}引脚"
    },
    "hub_failed_to_read_pin": {
        "en": "Hub failed to read hub {} pin",
        "cn": "集线器未能读取集线器{}引脚"
    },
    "jh_comm_failure_reading_pin": {
        "en": "Communication failure between jig and hub when reading hub {} pin",
        "cn": "读取集线器{}引脚时夹具和集线器之间的通信失败"
    },
    "high_temp_expected": {
        "en": "Hub read a temp from {}-{} degrees on {} pin when high temp of 40 degrees was expected",
        "cn": "集线器读取{}引脚上的温度为{}-{}度，预期为40度的高温"
    },
    "low_temp_expected": {
        "en": "Hub read a temp from {}-{} degrees on {} pin when low temp of 30 degrees was expected",
        "cn": "集线器读取{}引脚上的温度为{}-{}度，预期为30度的低温"
    },
    "unknown_action_received_reading_pin": {
        "en": "Unexpected action received from hub when reading hub {} pin",
        "cn": "读取集线器{}引脚时从集线器收到意外操作"
    },
    "jig_failure_setting_jig_pin": {
        "en": "Jig failure when setting jig {} pin to {}",
        "cn": "设置夹具{}引脚时夹具失败"
    },
    "cj_comm_failure_setting_jig_pin": {
        "en": "Communication failure between computer and jig when setting jig {} pin to {}",
        "cn": "设置夹具{}引脚时计算机和夹具之间的通信失败"
    },
    "computer_failure_setting_jig_pin": {
        "en": "Computer failure when setting jig {} pin to {}",
        "cn": "设置夹具{}引脚时计算机失败"
    },
    "unknown_action_received_setting_jig_pin": {
        "en": "Unknown action received from jig when setting jig {} pin to {}",
        "cn": "设置夹具{}引脚时从夹具收到未知操作"
    },
    "jig_failure_reading_hub_pin": {
        "en": "Jig failure when reading hub {} pin",
        "cn": "读取集线器{}引脚时夹具失败"
    },
    "cj_comm_failure_reading_hub_pin": {
        "en": "Communication failure between computer and jig when reading hub {} pin",
        "cn": "读取集线器{}引脚时计算机和夹具之间的通信失败"
    },
    "computer_failure_reading_hub_pin": {
        "en": "Computer failure when reading hub {} pin",
        "cn": "读取集线器{}引脚时计算机失败"
    },"set_pump_high": { 
        "en": "Set Pump High",
        "cn": "设置泵高"
    },
    "read_pump_current_high": {
        "en": "Read Pump Current High",
        "cn": "读取泵电流高"
    },
    "set_pump_low": {
        "en": "Set Pump Low",
        "cn": "设置泵低"
    },
    "read_pump_current_low": {
        "en": "Read Pump Current Low",
        "cn": "读取泵电流低"
    },
    "pump": {
        "en": "pump",
        "cn": "泵"
    },
    "pump_current": {
        "en": "pump current",
        "cn": "泵电流"
    },
    "out_1": {
        "en": "Out 1",
        "cn": "输出1"
    },
    "out_2": {
        "en": "Out 2",
        "cn": "输出2"
    },
    "peltier_1": {
        "en": "Peltier 1",
        "cn": "佩尔帖1"
    },
    "peltier_2": {
        "en": "Peltier 2",
        "cn": "佩尔帖2"
    },
    "in_1": {
        "en": "In 1",
        "cn": "输入1"
    },
    "in_2": {
        "en": "In 2",
        "cn": "输入2"
    },
    "cooling": {
        "en": "Cooling",
        "cn": "冷却"
    },
    "heating": {
        "en": "Heating",
        "cn": "加热"
    },
    "driver_set_high": {
        "en": "Driver {} : Set {} High",
        "cn": "驱动器{}：设置{}高"
    },
    "driver_read_high": {
        "en": "Driver {} : Read {} High",
        "cn": "驱动器{}：读取{}高"
    },
    "driver_read_low": {
        "en": "Driver {} : Read {} Low",
        "cn": "驱动器{}：读取{}低"
    },
    "driver_read_fault_high": {
        "en": "Driver {} : Read Fault High",
        "cn": "驱动器{}：读取故障高"
    },
    "driver_read_disable_low": {
        "en": "Driver {} : Read Disable Low",
        "cn": "驱动器{}：读取禁用低"
    },
    "driver_read_sleep_high": {
        "en": "Driver {} : Read Sleep High",
        "cn": "驱动器{}：读取睡眠高"
    },
    "driver_read_iprop_low": {
        "en": "Driver {} : Read Iprop Low",
        "cn": "驱动器{}：读取Iprop低"
    },
    "fault": {
        "en": "fault",
        "cn": "故障"
    },
    "disable": {
        "en": "disable",
        "cn": "禁用"
    },
    "sleep": {
        "en": "sleep",
        "cn": "睡眠"
    },
    "iprop": {
        "en": "iprop",
        "cn": "电流"
    },
    "driver_off_with_disable_high": {
        "en": "Driver Off with Disable High",
        "cn": "驱动器关闭，禁用高"
    },
    "driver_off_with_sleep_low": {
        "en": "Driver Off with Sleep Low",
        "cn": "驱动器关闭，睡眠低"
    },
    "waiting_20_seconds": {
        "en": "Waiting 20 seconds for driver to turn off",
        "cn": "等待20秒以关闭驱动器"
    },
    "waiting_100_seconds": {
        "en": "Waiting 100 seconds for driver to turn off",
        "cn": "等待100秒以关闭驱动器"
    },
    "set_in_1_high": {
        "en": "{} : Set In 1 High",
        "cn": "{} : 设置输入1高"
    },
    "set_sleep": {
        "en": "{} : Set Sleep {}",
        "cn": "{} : 设置睡眠{}"
    },
    "set_disable": {
        "en": "{} : Set Disable {}",
        "cn": "{} : 设置禁用{}"
    },
    "read_in_2_low": {
        "en": "{} : Read In 2 Low",
        "cn": "{} : 读取输入2低"
    },
    "read_peltier_1_low": {
        "en": "{} : Read Peltier 1 Low",
        "cn": "{} : 读取佩尔帖1低"
    },
    "read_peltier_2_low": {
        "en": "{} : Read Peltier 2 Low",
        "cn": "{} : 读取佩尔帖2低"
    },
    "read_out_1_low": {
        "en": "{} : Read Out 1 Low",
        "cn": "{} : 读取输出1低"
    },
    "read_out_2_low": {
        "en": "{} : Read Out 2 Low",
        "cn": "{} : 读取输出2低"
    },
    "read_fault_high": {
        "en": "{} : Read Fault High",
        "cn": "{} : 读取故障高"
    },
    "read_iprop_low": {
        "en": "{} : Read Iprop Low",
        "cn": "{} : 读取Iprop低"
    },
    "invalid_temperature_number": {
        "en": "Invalid temperature number",
        "cn": "无效的温度编号"
    },
    "set_temp_to_high": {
        "en": "Set Temp {} to High Temp",
        "cn": "将温度{}设置为高温"
    },
    "set_temp_to_low": {
        "en": "Set Temp {} to Low Temp",
        "cn": "将温度{}设置为低温"
    },
    "temp": {
        "en": "temp",
        "cn": "温度"
    }
}

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
        test_name = translations["start_tests_protocol"][config.lang]
    elif control_type == 'end':
        my_id = Id.END_TESTS
        expected_id = Id.ENDED_TESTS
        test_name = translations["end_tests_protocol"][config.lang]
    else:
        print(translations["invalid_control_type"][config.lang])
        return -1

    translated_control_type = translations[control_type + "_tests"][config.lang]
    print(translations["beginning_tests_protocol"][config.lang].format(translated_control_type))

    this_code = create_code(id = my_id)

    if(this_code == 0):
        print(translations["failed_to_create_code"][config.lang].format(translated_control_type))
        print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
        add_test_result(test_name, translations["failure"][config.lang], translations["failed_to_create_code"][config.lang].format(translated_control_type))
        return -1

    code_details = translations[control_type + "_tests"][config.lang]
    
    send_success = send_code(this_code, ser, True, code_details=code_details)       

    if(send_success == -1):
        print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_error_sending_code"][config.lang].format(translated_control_type))
        return -1
    
    elif(send_success == -2):
        print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code"][config.lang])
        return -1

    received_code = read_from_serial(ser, STARTED_SIZE, True)

    if received_code == -1:
        print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_code_within_2_seconds"][config.lang])
        return -1
    
    if received_code == -2:
        print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code_size"][config.lang])
        return -1

    if received_code['id'] == expected_id:

        if received_code['action'] == Action.SUCCESS:   
            print(translations["completed_tests_protocol"][config.lang].format(translated_control_type))
            add_test_result(test_name, translations["success"][config.lang], "")
            return 1
        elif received_code['action'] == Action.FAILURE: 
            print(translations["computer_failed_tests_protocol"][config.lang].format(translated_control_type))
            print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
            add_test_result(test_name, translations["failure"][config.lang], translations["computer_failed_tests_protocol"][config.lang].format(translated_control_type))
            return -1
        elif received_code['action'] == Action.HUB_FAILURE:   
            print(translations["hub_failed_tests_protocol"][config.lang].format(translated_control_type))
            print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
            add_test_result(test_name, translations["failure"][config.lang], translations["hub_failed_tests_protocol"][config.lang].format(translated_control_type))
            return -1
        elif received_code['action'] == Action.JIG_FAILURE:
            print(translations["jig_failed_tests_protocol"][config.lang].format(translated_control_type))
            print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
            add_test_result(test_name, translations["failure"][config.lang], translations["jig_failed_tests_protocol"][config.lang].format(translated_control_type))
            return -1
        elif received_code['action'] == Action.JH_COMM_FAILURE:
            print(translations["jh_comm_failure"][config.lang].format(control_type))
            print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
            add_test_result(test_name, translations["failure"][config.lang], translations["jh_comm_failure"][config.lang].format(control_type))
            return -1
        elif received_code['action'] == Action.CJ_COMM_FAILURE:
            print(translations["cj_comm_failure"][config.lang].format(control_type))
            print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
            add_test_result(test_name, translations["failure"][config.lang], translations["cj_comm_failure"][config.lang].format(control_type))
            return -1
        else:
            print(translations["unknown_action_received"][config.lang].format(control_type))
            print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
            add_test_result(test_name, translations["failure"][config.lang], translations["unknown_action_received"][config.lang].format(control_type))
            return -1

    else:
        print(translations["did_not_receive_code"][config.lang].format(control_type))
        print(received_code)
        print(translations["failed_tests_protocol"][config.lang].format(translated_control_type))
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_code"][config.lang].format(control_type))

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
        state_string = translations["high"][config.lang]
        wrong_state_string = translations["low"][config.lang]
    elif state == Value.LOW:
        state_string = translations["low"][config.lang]
        wrong_state_string = translations["high"][config.lang]
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.HUB_SET, pin = this_pin, value = state)

    if(this_code == 0):
        print(translations["failed_to_create_hub_set_code"][config.lang])
        add_test_result(test_name, translations["failure"][config.lang], translations["failed_to_create_hub_set_code"][config.lang])
        return -1
    
    code_details_string = translations["set_hub_pin"][config.lang].format(pin_name, state_string)

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_error_reading_serial"][config.lang])
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code"][config.lang])
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_code_within_2_seconds"][config.lang])
        return -1
    
    if this_code == -2:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code_size"][config.lang])
        return -1

    elif this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["jig_failure_setting_pin"][config.lang].format(pin_name, state_string))
        return -1
    elif this_code['action'] == Action.JH_COMM_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["jh_comm_failure_setting_pin"][config.lang].format(pin_name, state_string))
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["cj_comm_failure_setting_pin"][config.lang].format(pin_name, state_string))
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_failure_setting_pin"][config.lang].format(pin_name, state_string))
        return -1
    elif this_code['action'] != Action.SUCCESS:
        print(translations["unknown_action_received_setting_pin"][config.lang].format(pin_name, state_string))
        add_test_result(test_name, translations["failure"][config.lang], translations["unknown_action_received_setting_pin"][config.lang].format(pin_name, state_string))
        return -1
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.JIG_READ, pin = this_pin, value = Value.NO_VALUE) #TEMPORARY FOR OLD JIG 

    if(this_code == 0):
        print(translations["failed_to_create_jig_read_code"][config.lang])
        return -1
    
    code_details_string = translations["read_jig_pin"][config.lang].format(pin_name)

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_error_reading_serial"][config.lang])
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code"][config.lang])
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_code_within_2_seconds"][config.lang])
        return -1
    
    if this_code == -2:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code_size"][config.lang])
        return -1
    
    if this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["jig_failure_reading_pin"][config.lang].format(pin_name))
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["cj_comm_failure_reading_pin"][config.lang].format(pin_name))
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_failure_reading_pin"][config.lang].format(pin_name))
        return -1
    elif this_code['action'] == Action.SUCCESS:
        if this_code['value'] == state:
            if print_success:
                add_test_result(test_name, translations["success"][config.lang], "")
            return 1
        else:
            add_test_result(test_name, translations["failure"][config.lang], translations["jig_read_wrong_state"][config.lang].format(wrong_state_string, pin_name, state_string))
            return -1
    else:
        print(translations["unexpected_action_received_reading_pin"][config.lang].format(pin_name))
        add_test_result(test_name, translations["failure"][config.lang], translations["unexpected_action_received_reading_pin"][config.lang].format(pin_name))
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
    print(translations["starting_test"][config.lang].format(test_name))

    state_string = ""
    wrong_state_string = ""

    if state == Value.HIGH:
        state_string = translations["high"][config.lang]
        wrong_state_string = translations["low"][config.lang]
    elif state == Value.LOW:
        state_string = translations["low"][config.lang]
        wrong_state_string = translations["high"][config.lang]
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.JIG_READ, pin = this_pin, value = Value.NO_VALUE)

    if(this_code == 0):
        print(translations["failed_to_create_jig_read_code"][config.lang])
        add_test_result(test_name, translations["failure"][config.lang], translations["failed_to_create_jig_read_code"][config.lang])
        time.sleep(2)
        return -1
    
    code_details_string = translations["read_jig_pin"][config.lang].format(pin_name)

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_error_reading_serial"][config.lang])
        time.sleep(2)
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code"][config.lang])
        time.sleep(2)
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_code_within_2_seconds"][config.lang])
        time.sleep(2)
        return -1
    
    if this_code == -2:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code_size"][config.lang])
        time.sleep(2)
        return -1
    
    if this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["jig_failure_reading_pin"][config.lang].format(pin_name))
        time.sleep(2)
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["cj_comm_failure_reading_pin"][config.lang].format(pin_name))
        time.sleep(2)
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_failure_reading_pin"][config.lang].format(pin_name))
        time.sleep(2)
        return -1
    elif this_code['action'] == Action.SUCCESS:
        if this_code['value'] == state:
            if print_success:
                add_test_result(test_name, translations["success"][config.lang], "")
            time.sleep(2)
            return 1
        else:
            add_test_result(test_name, translations["failure"][config.lang], translations["jig_read_wrong_state"][config.lang].format(wrong_state_string, pin_name, state_string))
            time.sleep(2)
            return -1
    else:
        print(translations["unexpected_action_received_reading_pin"][config.lang].format(pin_name))
        add_test_result(test_name, translations["failure"][config.lang], translations["unexpected_action_received_reading_pin"][config.lang].format(pin_name))
        time.sleep(2)
        return -1
    
    time.sleep(2)
    return -1

def jig_set_hub_read(ser, state, test_name, pin_name, this_pin, print_success):
    print(translations["starting_test"][config.lang].format(test_name))
    
    state_string = ""
    wrong_state_string = ""

    if state == Value.HIGH:
        state_string = translations["high"][config.lang]
        wrong_state_string = translations["low"][config.lang]
    elif state == Value.LOW:
        state_string = translations["low"][config.lang]
        wrong_state_string = translations["high"][config.lang]
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.JIG_SET, pin = this_pin, value = state)

    if(this_code == 0):
        print(translations["failed_to_create_jig_set_code"][config.lang])
        add_test_result(test_name, translations["failure"][config.lang], translations["failed_to_create_jig_set_code"][config.lang])
        return -1
    
    code_details_string = translations["set_jig_pin"][config.lang].format(pin_name, state_string)

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_error_reading_serial"][config.lang])
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code"][config.lang])
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_code_within_2_seconds"][config.lang])
        return -1
    
    if this_code == -2:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code_size"][config.lang])
        return -1

    if this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["jig_failure_setting_jig_pin"][config.lang].format(pin_name, state_string))
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["cj_comm_failure_setting_jig_pin"][config.lang].format(pin_name, state_string))
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_failure_setting_jig_pin"][config.lang].format(pin_name, state_string))
        return -1
    elif this_code['action'] != Action.SUCCESS:
        print(translations["unknown_action_received_setting_jig_pin"][config.lang].format(pin_name, state_string))
        add_test_result(test_name, translations["failure"][config.lang], translations["unknown_action_received_setting_jig_pin"][config.lang].format(pin_name, state_string))
        return -1
    
    this_code = create_code(id = Id.COMPUTER_REQUEST, mode = Mode.HUB_READ, pin = this_pin, value = Value.NO_VALUE)

    if(this_code == 0):
        print(translations["failed_to_create_hub_read_code"][config.lang])
        return -1
    
    code_details_string = translations["read_hub_pin"][config.lang].format(pin_name)

    ret = send_code(this_code, ser, True, code_details_string)

    if(ret == -1):
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_error_reading_serial"][config.lang])
        return -1
    
    elif(ret == -2):
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code"][config.lang])
        return -1
    
    this_code = read_from_serial(ser, RESPONSE_SIZE, True)

    if this_code == -1:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_code_within_2_seconds"][config.lang])
        return -1
    
    if this_code == -2:
        add_test_result(test_name, translations["failure"][config.lang], translations["did_not_receive_expected_code_size"][config.lang])
        return -1
    
    if this_code['action'] == Action.JIG_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["jig_failure_reading_hub_pin"][config.lang].format(pin_name))
        return -1
    elif this_code['action'] == Action.CJ_COMM_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["cj_comm_failure_reading_hub_pin"][config.lang].format(pin_name))
        return -1
    elif this_code['action'] == Action.FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["computer_failure_reading_hub_pin"][config.lang].format(pin_name))
        return -1
    elif this_code['action'] == Action.HUB_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["hub_failed_to_read_pin"][config.lang].format(pin_name))
        return -1
    elif this_code['action'] == Action.JH_COMM_FAILURE:
        add_test_result(test_name, translations["failure"][config.lang], translations["jh_comm_failure_reading_pin"][config.lang].format(pin_name))
        return -1
    elif this_code['action'] == Action.SUCCESS:
        if this_code['value'] == state:
            if print_success:
                add_test_result(test_name, translations["success"][config.lang], "")
            return 1
        elif (this_pin == Pin.TEMP1 or this_pin == Pin.TEMP2 or this_pin == Pin.TEMP3 or this_pin == Pin.TEMP4):
            if state == Value.HIGH_TEMP:
                if this_code['value'] == Value.TEMP_35_TO_40 or this_code['value'] == Value.TEMP_40_TO_45:
                    if print_success:
                        add_test_result(test_name, translations["success"][config.lang], "")
                    return 1
                else:
                    lowest_temp = (this_code['value'].value - Value.TEMP_0_TO_5.value) * 5
                    highest_temp = lowest_temp + 5

                    add_test_result(test_name, translations["failure"][config.lang], translations["high_temp_expected"][config.lang].format(lowest_temp, highest_temp, pin_name))
                    return -1
            elif state == Value.LOW_TEMP:
                if this_code['value'] == Value.TEMP_25_TO_30 or this_code['value'] == Value.TEMP_30_TO_35:
                    if print_success:
                        add_test_result(test_name, translations["success"][config.lang], "")
                    return 1
                else:
                    lowest_temp = (this_code['value'].value - Value.TEMP_0_TO_5.value) * 5
                    highest_temp = lowest_temp + 5

                    add_test_result(test_name, translations["failure"][config.lang], translations["low_temp_expected"][config.lang].format(lowest_temp, highest_temp, pin_name))
                    return -1

        else:
            add_test_result(test_name, translations["failure"][config.lang], translations["jig_read_wrong_state"][config.lang].format(wrong_state_string, pin_name, state_string))
            return -1
    else:
        print(translations["unknown_action_received_reading_pin"][config.lang].format(pin_name))
        add_test_result(test_name, translations["failure"][config.lang], translations["unknown_action_received_reading_pin"][config.lang].format(pin_name))
        return -1
    
    return -1

def test_pump(ser):
    hub_set_jig_read(ser, Value.HIGH, translations["set_pump_high"][config.lang], translations["pump"][config.lang], Pin.PUMP, True)

    jig_read_test(ser, Value.HIGH, translations["read_pump_current_high"][config.lang], translations["pump_current"][config.lang], Pin.PC, True)

    hub_set_jig_read(ser, Value.LOW, translations["set_pump_low"][config.lang], translations["pump"][config.lang], Pin.PUMP, True)

    jig_read_test(ser, Value.LOW, translations["read_pump_current_low"][config.lang], translations["pump_current"][config.lang], Pin.PC, True)

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
        high_out_string = translations["out_1"][config.lang]
        low_out_string = translations["out_2"][config.lang]
        high_peltier_string = translations["peltier_1"][config.lang]
        low_peltier_string = translations["peltier_2"][config.lang]
        high_in_string = translations["in_1"][config.lang]
        low_in_string = translations["in_2"][config.lang]
        driver_type_string = translations["cooling"][config.lang]

    elif driver_type == 2:
        high_out = Pin.OUT2
        low_out = Pin.OUT1
        high_peltier = Pin.PELTIER2
        low_peltier = Pin.PELTIER1
        high_in = Pin.IN2
        low_in = Pin.IN1
        high_out_string = translations["out_2"][config.lang]
        low_out_string = translations["out_1"][config.lang]
        high_peltier_string = translations["peltier_2"][config.lang]
        low_peltier_string = translations["peltier_1"][config.lang]
        high_in_string = translations["in_2"][config.lang]
        low_in_string = translations["in_1"][config.lang]
        driver_type_string = translations["heating"][config.lang]

    #sets the wanted driver input high and reads from jig
    hub_set_jig_read(ser, Value.HIGH, translations["driver_set_high"][config.lang].format(driver_type_string, high_in_string), translations[high_in_string.lower().replace(' ', '_')][config.lang], high_in, True)     

    jig_read_test(ser, Value.HIGH, translations["driver_read_high"][config.lang].format(driver_type_string, high_out_string), translations[high_out_string.lower().replace(' ', '_')][config.lang], high_out, True)

    jig_read_test(ser, Value.HIGH, translations["driver_read_high"][config.lang].format(driver_type_string, high_peltier_string), translations[high_peltier_string.lower().replace(' ', '_')][config.lang], high_peltier, True)

    jig_read_test(ser, Value.LOW, translations["driver_read_low"][config.lang].format(driver_type_string, low_in_string), translations[low_in_string.lower().replace(' ', '_')][config.lang], low_in, True)

    jig_read_test(ser, Value.LOW, translations["driver_read_low"][config.lang].format(driver_type_string, low_out_string), translations[low_out_string.lower().replace(' ', '_')][config.lang], low_out, True)

    jig_read_test(ser, Value.LOW, translations["driver_read_low"][config.lang].format(driver_type_string, low_peltier_string), translations[low_peltier_string.lower().replace(' ', '_')][config.lang], low_peltier, True)

    jig_read_test(ser, Value.HIGH, translations["driver_read_fault_high"][config.lang].format(driver_type_string), translations["fault"][config.lang], Pin.FAULT, True)

    jig_read_test(ser, Value.LOW, translations["driver_read_disable_low"][config.lang].format(driver_type_string), translations["disable"][config.lang], Pin.DIS, True)

    jig_read_test(ser, Value.HIGH, translations["driver_read_sleep_high"][config.lang].format(driver_type_string), translations["sleep"][config.lang], Pin.SLEEP, True)

    jig_read_test(ser, Value.LOW, translations["driver_read_iprop_low"][config.lang].format(driver_type_string), translations["iprop"][config.lang], Pin.IPROP, True)
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
        sleep_value_string = translations["high"][config.lang]
        disable_value_string = translations["high"][config.lang]
        test_name = translations["driver_off_with_disable_high"][config.lang]

    elif driver_type == "sleep":
        sleep_value = Value.LOW
        disable_value = Value.LOW
        sleep_value_string = translations["low"][config.lang]
        disable_value_string = translations["low"][config.lang]
        test_name = translations["driver_off_with_sleep_low"][config.lang]

    else:
        print("Invalid driver type")
        return -1
    
    hub_set_jig_read(ser, Value.HIGH, translations["set_in_1_high"][config.lang].format(test_name), translations["in_1"][config.lang], Pin.IN1, True)

    hub_set_jig_read(ser, sleep_value, translations["set_sleep"][config.lang].format(test_name, sleep_value_string), translations["sleep"][config.lang], Pin.SLEEP, True)

    hub_set_jig_read(ser, disable_value, translations["set_disable"][config.lang].format(test_name, disable_value_string), translations["disable"][config.lang], Pin.DIS, True)

    if driver_type == "dis":
        print(translations["waiting_20_seconds_for_driver"][config.lang])
        time.sleep(20)

    elif driver_type == "sleep":
        print(translations["waiting_100_seconds_for_driver"][config.lang])
        time.sleep(100)

    jig_read_test(ser, Value.LOW, translations["read_in_2_low"][config.lang].format(test_name), translations["in_2"][config.lang], Pin.IN2, True)

    jig_read_test(ser, Value.LOW, translations["read_peltier_1_low"][config.lang].format(test_name), translations["peltier_1"][config.lang], Pin.PELTIER1, True)

    jig_read_test(ser, Value.LOW, translations["read_peltier_2_low"][config.lang].format(test_name), translations["peltier_2"][config.lang], Pin.PELTIER2, True)

    jig_read_test(ser, Value.LOW, translations["read_out_1_low"][config.lang].format(test_name), translations["out_1"][config.lang], Pin.OUT1, True)

    jig_read_test(ser, Value.LOW, translations["read_out_2_low"][config.lang].format(test_name), translations["out_2"][config.lang], Pin.OUT2, True)

    jig_read_test(ser, Value.HIGH, translations["read_fault_high"][config.lang].format(test_name), translations["fault"][config.lang], Pin.FAULT, True)

    jig_read_test(ser, Value.LOW, translations["read_iprop_low"][config.lang].format(test_name), translations["iprop"][config.lang], Pin.IPROP, True)

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
        print(translations["invalid_temperature_number"][config.lang])
        return -1
        
    jig_set_hub_read(ser, Value.HIGH_TEMP, translations["set_temp_to_high"][config.lang].format(temp_number), translations["temp"][config.lang] + " " + str(temp_number), pin, True)

    time.sleep(5)

    jig_set_hub_read(ser, Value.LOW_TEMP, translations["set_temp_to_low"][config.lang].format(temp_number), translations["temp"][config.lang] + " " + str(temp_number), pin, True)