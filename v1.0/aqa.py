#!/usr/bin/python3
# author: Jens Fuchs
# git: https://github.com/eleven6/

import serial
import time
import requests

# Serial connection

# define serial port (serial port speed  19200 baud, 8 databits, 1 stopbit, no parity)
# serial.Serial parameter: port=None, baudrate=9600, bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, write_timeout=None, dsrdtr=False, inter_byte_timeout=None
port = "/dev/ttyACM0"
speed = 19200
ser = serial.Serial(port, speed, timeout=0.5)
print(ser.name + ' is open.') # REMOVE LATER

# BWT_AQA_PERLA_S CMD_SAEULE1_SOLLKAPAZITAET            0x02 = 2    // Sollkapazität Säule 1
# BWT_AQA_PERLA_S CMD_SAEULE2_SOLLKAPAZITAET            0x03 = 3   	// Sollkapazität Säule 2
# BWT_AQA_PERLA_S CMD_MAX_DURCHFLUSS_HEUTE_LITER        0x05 = 5   	// Spitzendurchfluss heute
# BWT_AQA_PERLA_S CMD_MAX_DURCHFLUSS_GESTERN_LITER      0x06 = 6   	// Spitzendurchfluss gestern
# BWT_AQA_PERLA_S CMD_MAX_DURCHFLUSS_SEIT_IBN_LITER     0x07 = 7   	// Spitzendurchfluss seit IBN
# BWT_AQA_PERLA_S CMD_Wasser_Vebrauch_24h			    0x08 = 8   	// Verbrauch letzte 24h
# BWT_AQA_PERLA_S CMD_VERBRAUCH_SEIT_IBN                0x10 = 16	// Verbrauchdaten seit IBN Verbrauch
# BWT_AQA_PERLA_S CMD_REGENERATIONEN_SEIT_IBN           0x11 = 17   // Regenerationen seit IBN
# BWT_AQA_PERLA_S CMD_SALZVERBRAUCH_GRAMM_SEIT_IBN      0x13 = 19  	// Salztverbrauch seit IBN
# BWT_AQA_PERLA_S CMD_Wasser_Kapazität Säule 1          0x25 = 37   // Kapa Säule 1
# BWT_AQA_PERLA_S CMD_Wasser\Kapazität Säule 2          0x26 = 38  	// Kapa Säule 2
# BWT_AQA_PERLA_S CMD_ALARM                             0x20 = 32   // Alarm --> do not read now

command_set = [0x02, 0x03, 0x05, 0x06, 0x07, 0x08, 0x10, 0x11, 0x13, 0x25, 0x26, 0x12, 0x19, 0x15, 0x21, 0x24] # list of all commands to execute
command_name = ["SAEULE1_SOLLKAPAZITAET", "SAEULE2_SOLLKAPAZITAET", "MAX_DURCHFLUSS_HEUTE_LITER", "MAX_DURCHFLUSS_GESTERN_LITER","MAX_DURCHFLUSS_SEIT_IBN_LITER", "Wasser_Vebrauch_24h", "VERBRAUCH_SEIT_IBN", "REGENERATIONEN_SEIT_IBN", "SALZVERBRAUCH_GRAMM_SEIT_IBN", "SAEULE1_RESTKAPAZITAET", "SAEULE2_RESTKAPAZITAET", "REGENERATIONEN_SEIT_SERVICE", "SOFTWARE_VERSION", "IBN_DATUM", "LOG", "KW"]
result_set = [] # will hold the results

# Execute all commands in command_set and save results in result_set
j = 0
for cmd in command_set:
  ser.flushInput()  #flush input buffer, discarding all its contents
  ser.flushOutput() #flush output buffer, aborting current output and discard all that is in buffer

  start_byte = 0x0D
  stop_byte = 0x0A
  command = cmd
  parameter = 0 # except for reading alarms
  crc = 0 # start_byte + cmd + parameter

  # build the command: bytearray and CRC
  crc = start_byte + command + parameter
  arr = bytearray([start_byte, command, parameter, crc, stop_byte])

  # send command
  ser.write(arr)

  # read results
  res = ser.read(size=256)

  # calculate integer result
  x = res[3] + res[4]*256
  print (command_name[j] + " = " + str(x))
  j += 1

# close connection
ser.close()
