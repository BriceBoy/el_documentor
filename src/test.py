from sections import *

SAMPLES_ROBOT_DIR = "C:/Users/Brice Piqueux/OneDrive - MCA MANAGEMENT/Documents/Git/El Documentor/samples_robot/"
robot_file = SAMPLES_ROBOT_DIR + "full_sample.robot"

robot = Robot(robot_file)
print("\n\n===================== LINES =====================")
robot.print_lines()
robot.refactor_multi_lines_instructions()
print("\n\n===================== REFACTORED LINES =====================")
robot.print_lines()
