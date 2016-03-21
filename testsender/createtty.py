import os, pty, serial, time

master, slave = pty.openpty()
s_name = os.ttyname(slave)

ser = serial.Serial(s_name)

print("Writing to "+s_name)

# To Write to the device
while (True):
    ser.write(time.strftime("%Y-%m-%d %H:%M:%S - Felix war hier"))
    time.sleep(1)
    print(os.read(master,1000))

print("Wrote to serial device; Sleeping for 30 seconds")

# To read from the device

