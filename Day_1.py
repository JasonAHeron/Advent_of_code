floor = 0
basement = False
for index, instruction in enumerate(open('Day_1.txt').readline()):
    floor += 1 if instruction == "(" else -1
    if floor < 0 and not basement:
        print "Basement on floor: {}".format(index+1)
        basement = True

print "Ended on floor: {}".format(floor+1)
