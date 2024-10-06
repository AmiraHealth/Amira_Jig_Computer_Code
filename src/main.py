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
import config

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
    },
    "attempt_failed": {
        "en": "Attempt {} to start tests failed.",
        "cn": "尝试 {} 启动测试失败。"
    },
    "all_attempts_failed": {
        "en": "All attempts to start tests failed",
        "cn": "所有启动测试的尝试均失败"
    },
    "unplug_replug": {
        "en": "Unplug and replug the USB cable for the device to restart the devices and try again",
        "cn": "拔下并重新插入设备的 USB 电缆以重新启动设备并重试"
    },
    "jig_hub_fault": {
        "en": "If issue persists due to jig to hub communication, there may be a fault in the B1, B2, L1, or L2 pins on the hub or on the jig",
        "cn": "如果问题由于夹具到集线器通信而持续存在，则集线器或夹具上的 B1、B2、L1 或 L2 引脚可能存在故障"
    },
    "computer_jig_fault": {
        "en": "If issue persists due to computer to jig communication, there may be a fault in the RXD or TXD pins on the jig",
        "cn": "如果问题由于计算机到夹具通信而持续存在，则夹具上的 RXD 或 TXD 引脚可能存在故障"
    },
    "exiting_program": {
        "en": "Exiting program",
        "cn": "退出程序"
    },
    "read_5v": {
        "en": "Read 5V",
        "cn": "读取 5V"
    },
    "read_3v3": {
        "en": "Read 3V3",
        "cn": "读取 3V3"
    },
    "read_gnd": {
        "en": "Read GND",
        "cn": "读取 GND"
    },
    "set_led3_high": {
        "en": "Set LED 3 High",
        "cn": "设置 LED 3 高"
    },
    "set_led3_low": {
        "en": "Set LED 3 Low",
        "cn": "设置 LED 3 低"
    },
    "set_fan_high": {
        "en": "Set Fan High",
        "cn": "设置风扇高"
    },
    "set_fan_low": {
        "en": "Set Fan Low",
        "cn": "设置风扇低"
    },
    "set_float1_high": {
        "en": "Set Float1 High",
        "cn": "设置浮子1高"
    },
    "set_float1_low": {
        "en": "Set Float1 Low",
        "cn": "设置浮子1低"
    },
    "set_float2_high": {
        "en": "Set Float2 High",
        "cn": "设置浮子2高"
    },
    "set_float2_low": {
        "en": "Set Float2 Low",
        "cn": "设置浮子2低"
    },
    "test_cooling_driver": {
        "en": "Test cooling driver",
        "cn": "测试冷却驱动程序"
    },
    "test_heating_driver": {
        "en": "Test heating driver",
        "cn": "测试加热驱动程序"
    },
    "test_driver_no_output_disable_high": {
        "en": "Test driver has no output when disable high",
        "cn": "禁用高时测试驱动程序无输出"
    },
    "reset_sleep_high": {
        "en": "Reset Sleep High",
        "cn": "重置睡眠高"
    },
    "reset_disable_low": {
        "en": "Reset Disable Low",
        "cn": "重置禁用低"
    },
    "reset_in1_high": {
        "en": "Reset In1 High",
        "cn": "重置 In1 高"
    },
    "test_driver_no_output_sleep_low": {
        "en": "Test driver has no output when sleep low",
        "cn": "睡眠低时测试驱动程序无输出"
    },
    "start": {
        "en": "start",
        "cn": "开始"
    },
    "end": {
        "en": "end",
        "cn": "结束"
    },
    "5_volts": {
        "en": "5 volts",
        "cn": "5 伏"
    },
    "3.3_volts": {
        "en": "3.3 volts",
        "cn": "3.3 伏"
    },
    "ground": {
        "en": "ground",
        "cn": "地"
    },
    "led_3": {
        "en": "led 3",
        "cn": "LED 3"
    },
    "fan": {
        "en": "fan",
        "cn": "风扇"
    },
    "float_1": {
        "en": "float 1",
        "cn": "浮子 1"
    },
    "float_2": {
        "en": "float 2",
        "cn": "浮子 2"
    },
    "disable": {
        "en": "disable",
        "cn": "禁用"
    },
    "sleep": {
        "en": "sleep",
        "cn": "睡眠"
    },
    "in_1": {
        "en": "in 1",
        "cn": "输入 1"
    }
}

config.lang = "cn" if language == "2" else "en"
lang_code = config.lang

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
        print(translations["attempt_failed"][lang_code].format(attempt + 1))
        print("")
        if attempt == attempts - 1:
            print(translations["all_attempts_failed"][lang_code])
            print_test_results()
            print(translations["unplug_replug"][lang_code])
            print(translations["jig_hub_fault"][lang_code])
            print(translations["computer_jig_fault"][lang_code])
            print(translations["exiting_program"][lang_code])
            sys.exit(1) 

time.sleep(3)

jig_read_test(ser1, Value.HIGH, translations["read_5v"][lang_code], translations["5_volts"][lang_code], Pin.VOLT5, True)

jig_read_test(ser1, Value.HIGH, translations["read_3v3"][lang_code], translations["3.3_volts"][lang_code], Pin.VOLT3V3, True)

jig_read_test(ser1, Value.LOW, translations["read_gnd"][lang_code], translations["ground"][lang_code], Pin.GND, True)

hub_set_jig_read(ser1, Value.HIGH, translations["set_led3_high"][lang_code], translations["led_3"][lang_code], Pin.LED3, True)

hub_set_jig_read(ser1, Value.LOW, translations["set_led3_low"][lang_code], translations["led_3"][lang_code], Pin.LED3, True)

hub_set_jig_read(ser1, Value.HIGH, translations["set_fan_high"][lang_code], translations["fan"][lang_code], Pin.FAN, True)

hub_set_jig_read(ser1, Value.LOW, translations["set_fan_low"][lang_code], translations["fan"][lang_code], Pin.FAN, True)

test_pump(ser1)

jig_set_hub_read(ser1, Value.HIGH, translations["set_float1_high"][lang_code], translations["float_1"][lang_code], Pin.FLOAT1, True)

jig_set_hub_read(ser1, Value.LOW, translations["set_float1_low"][lang_code], translations["float_1"][lang_code], Pin.FLOAT1, True)

jig_set_hub_read(ser1, Value.HIGH, translations["set_float2_high"][lang_code], translations["float_2"][lang_code], Pin.FLOAT2, True)

jig_set_hub_read(ser1, Value.LOW, translations["set_float2_low"][lang_code], translations["float_2"][lang_code], Pin.FLOAT2, True)

test_driver_on(ser1, 1)  # test cooling driver

test_driver_on(ser1, 2)  # test heating driver

test_driver_off(ser1, "dis")    #test driver has no output when disable high

hub_set_jig_read(ser1, Value.HIGH, translations["reset_sleep_high"][lang_code], translations["sleep"][lang_code], Pin.SLEEP, True)  # reset driver to be working and cooling

hub_set_jig_read(ser1, Value.LOW, translations["reset_disable_low"][lang_code], translations["disable"][lang_code], Pin.DIS, True)

hub_set_jig_read(ser1, Value.HIGH, translations["reset_in1_high"][lang_code], translations["in_1"][lang_code], Pin.IN1, True)

test_driver_off(ser1, "sleep")  #test driver has no output when sleep low

test_temp(ser1, 1)

test_temp(ser1, 2)

test_temp(ser1, 3)

test_temp(ser1, 4)

control_tests(ser1, translations["end"][lang_code])

print_test_results()