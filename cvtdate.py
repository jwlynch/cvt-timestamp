#!/usr/bin/env python3

import sys
import pendulum

timeArg = "(none)"
numArgs = len(sys.argv)

if numArgs < 2:
    print("missing time arg")
elif numArgs > 2:
    print("too many args")
else:
    timeArg = sys.argv[1]

print("timearg %s, numArgs %s\n" % (timeArg, str(numArgs)))

tim = pendulum.parse(timeArg)

print(tim.astimezone(pendulum.local_timezone()))
