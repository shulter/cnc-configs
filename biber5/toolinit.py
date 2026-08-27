#!/usr/bin/python

import sys
import linuxcnc , hal
import re
import time

s = linuxcnc.stat()
c = linuxcnc.command()

h = hal.component("savetool")

varfile = "/home/cnc/share/justinbieber/linuxcnc.var"

old_tool = 0
for line in open(varfile, "r"):
    M = re.search("^5400\s([\.\d]*)", line)
    if M: old_tool =  re.search("^5400\s([\.\d]*)", line).group(1)

en = 1
try:
    while 1:
        if en:
            s.poll()
            if (not s.estop) and s.enabled and s.interp_state == linuxcnc.INTERP_IDLE:
                print "load last tool from previous session: %s" % old_tool
                c.mode(linuxcnc.MODE_MDI)
                c.wait_complete()
                c.mdi("M61 Q%s" % old_tool)
                en = 0
            time.sleep(2)
            print "waiting to be homed to load last tool..."
except KeyboardInterrupt:
    raise SystemExit
