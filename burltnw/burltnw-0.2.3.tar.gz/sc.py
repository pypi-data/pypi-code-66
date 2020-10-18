from burltnw import apollo

robot = apollo()
print(robot.get_status())

robot.walk(1,1)

robot.rotate(0)

robot.home()

print(robot.get_battery())