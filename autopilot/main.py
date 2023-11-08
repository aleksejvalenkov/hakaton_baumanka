
import time

from pymavlink import mavutil
# from iq_pymavlink_.arm import arm
# from iq_pymavlink_.takeoff import takeoff
# from iq_pymavlink_.land import land
# from iq_pymavlink_.speed_yaw import set_speed
from iq_pymavlink_.get_autopilot_info import get_autopilot_info


# from iq_pymavlink.unittests import test_all


# def mavlink_connect(connection_str: str, baud: int):
#     connection = mavutil.mavlink_connection(connection_str, baud)
#     connection.wait_heartbeat()
#     print(
#         f"Heartbeat from system (system {connection.target_system} component {connection.target_component})"
#     )
#     return connection


# connect = mavlink_connect("COM8", 115200)  # Подключение


# test_all.arm(connect, 1)
# arm(connect, 1)
# time.sleep(4)
# set_speed(connect, speed=3)
# takeoff(connect, 1)
# time.sleep(2)
# land(connect)
# time.sleep(4)
# arm(connect, 0)

the_connection = mavutil.mavlink_connection("/dev/ttyACM0", 57600)


the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))


def arm(statys_arm):
    the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                         mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 15, statys_arm, 0, 0, 0, 0, 0, 0)

    msg = the_connection.recv_match(type="COMMAND_ACK", blocking=True)
    return print(msg)


def takeoff(speed, h):
    the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                         mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, speed, 0, 0, 0, 0, h)

    msg = the_connection.recv_match(type="COMMAND_ACK", blocking=True)
    return print(msg)


def land():
    the_connection.mav.command_long_send(the_connection.target_system, the_connection.target_component,
                                         mavutil.mavlink.MAV_CMD_NAV_LAND, 0, 0, 0, 0, 0, 0, 0, 0)

    msg = the_connection.recv_match(type="COMMAND_ACK", blocking=True, timeout=10)

    if msg is None:
        print('No acknowledgment received within the timeout period.')
        return print(None)
    return print(msg)




arm(1)
print(get_autopilot_info(connection=the_connection))
time.sleep(3)
takeoff(1, 1)
time.sleep(5)
# land()
# time.sleep(5)
# arm(0)

