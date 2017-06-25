#!/usr/bin/env python

import subprocess
import time
import os

dir = os.path.dirname(os.path.realpath(__file__))
sanity_count = 0 #stop making the sound so no one goes crazy
grace_period = 6 #give wifi some time to get back on

print 'ctrl+z to stop'

while True:
  cmd = subprocess.Popen('iwconfig wlan0', shell=True, stdout=subprocess.PIPE)
  for line in cmd.stdout:
    if not 'Signal level' in line and 'Not-Associated' in line:
      grace_period -= 1
      if grace_period < 0:
        if sanity_count < 6:
          os.system("aplay " + dir + "/fail.wav")
          sanity_count += 1

    elif 'Signal level' in line:
      sanity_count = 0
      grace_period = 0

  time.sleep(10)

