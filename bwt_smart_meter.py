#!/usr/bin/python3
import serial

# define serial interface
serial_port = "/dev/ttyACM0"
serial_speed = "19200"

# define send string



start_byte = 0x0D
stop_byte = 0x0A
command = 0x10 # Verbrauchsdaten seit Inbetriebnahme
parameter = 0
crc = 0


print ("start_byte = " + chr(start_byte))
print ("comment = " + chr(command))
print ("stop_byte = " + chr(stop_byte))

# sendstring = START_Byte + COMMAND + ANZAHL PARAMETER (Immer 0, ausser bei Alarm, dann  + PARAMETER = 1) + CRC + STOP_BYTE
# CRC = Summe aller gesendeten bytes incl. Start_Byte

sendstring = chr(start_byte) + chr(command) + str(parameter) + chr(crc) + chr(stop_byte)
print ("Sendstring = " + sendstring)

print ("We are just at the beginning")
