from kukavarproxy import *
from time import sleep
import json 
robot = KUKA('10.10.105.200')

def wait_for_move():
    while int(robot.read("COM_ACTION")) > 0:
        sleep(0.001)

# robot.write("$OV_PRO",33)

measurement_s = robot.read("$POS_ACT_MES")
# measurement = json.loads(measurement_s)
print(measurement_s)
# measurement = robot.read("$POS_ACT")
# print(measurement)

robot.write("COM_E6POS", "{E6POS: X 953.497620, Y 2735.96082, Z 2678.79980, A 0.0, B 90, C 0.0, E1 -2850.0}")
robot.write("COM_ACTION", 3)
wait_for_move()
robot.write("COM_E6POS", "{E6POS: X 953.497620, Y 1135.96082, Z 2678.79980, A 0.0, B 90, C 0.0, E1 -1850.0}")
robot.write("COM_ACTION", 3)
wait_for_move()

# #Testing moves

# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2000.00, Z 2200.00, A 0.0, B 90, C 0.0, E1 -2500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2500.00, Z 2200.00, A 0.0, B 90, C 0.0, E1 -3000.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2000.00, Z 2200.00, A 0.0, B 90, C 0.0, E1 -2500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 1800.00, Y 1500.00, Z 1800.00, A 0.0, B 90, C 0.0, E1 -2500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2000.00, Z 2200.00, A 0.0, B 90, C 0.0, E1 -2500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2000.00, Z 2200.00, A 0.0, B 90, C 0.0, E1 -1500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2000.00, Z 2200.00, A 0.0, B 90, C 0.0, E1 -2500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2000.00, Z 2200.00, A 0.0, B 90, C 30.0, E1 -2500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2000.00, Z 2200.00, A 0.0, B 90, C -30.0, E1 -2500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# robot.write("COM_E6POS", "{E6POS: X 2100.00, Y 2000.00, Z 2200.00, A 0.0, B 90, C 0.0, E1 -2500.0}")
# robot.write("COM_ACTION", 3)
# wait_for_move()
# # # robot.write("COM_E6AXIS", "{E6AXIS: E1 -2000.0}")