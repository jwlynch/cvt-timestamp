#!/usr/bin/env python3

import sys
import pendulum

timeArg = sys.argv[0]
numArgs = len(sys.argv)

print("timearg %s, numArgs %s\n" % (timeArg, str(numArgs)))

tim = pendulum.parse("2019-07-15 16:10:18Z")

#print(tim.astimezone(pendulum.local_timezone()))
