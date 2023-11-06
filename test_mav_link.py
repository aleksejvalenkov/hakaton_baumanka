# Import mavutil
from pymavlink import mavutil

# Create the connection
# Need to provide the serial port and baudrate
# master = mavutil.mavlink_connection("COM8", baud=115200)

# Restart the ArduSub board !

the_connection = mavutil.mavlink_connection("/dev/ttyACM0", baud=115200)


the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

print("hhh")