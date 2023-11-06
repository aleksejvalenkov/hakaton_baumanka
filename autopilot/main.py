import time

from pymavlink import mavutil
from iq_pymavlink.arm import arm
from iq_pymavlink.takeoff import takeoff
from iq_pymavlink.land import land
from iq_pymavlink.speed_yaw import set_speed
from iq_pymavlink.get_autopilot_info import get_autopilot_info


# from iq_pymavlink.unittests import test_all


def mavlink_connect(connection_str: str, baud: int):
    connection = mavutil.mavlink_connection(connection_str, baud)
    connection.wait_heartbeat()
    print(
        f"Heartbeat from system (system {connection.target_system} component {connection.target_component})"
    )
    return connection


connect = mavlink_connect("/dev/ttyACM0", 57600)  # Подключение

# test_all.arm(connect, 1)
arm(connect, 1)
time.sleep(4)
set_speed(connect, speed=3)
takeoff(connect, 1)
time.sleep(2)
land(connect)
time.sleep(4)
arm(connect, 0)
