#!/usr/bin/env python3

from datetime import datetime
strptime = datetime.strptime
import pendulum

#print(strptime("2019-07-15 16:10:18Z", "%Y-%m-%d %H:%M:%S"))

tim = pendulum.parse("2019-07-15 16:10:18Z")

print(tim.astimezone(pendulum.local_timezone()))
