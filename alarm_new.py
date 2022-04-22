import datetime
import os
import time

class Alarm:
	def __init__(self, h, m, s):
		self.h = h
		self.m = m
		self.s = s
	def set_alarm(self):
		print("alarm_time is {} : {}".format(self.h, self.m))
		now = datetime.datetime.now()
		alarm_time = datetime.datetime.combine(now.date(), datetime.time(self.h+12, self.m, self.s))
		time.sleep((alarm_time - now).total_seconds())

		os.system(r"start alarm_music/alarm.mp3")

x, y, z = int(input('Enter hour>> ')), int(input('Enter minutes>> ')), int(input('Enter seconds>> '))
ring = Alarm(x, y, z)
ring.set_alarm()