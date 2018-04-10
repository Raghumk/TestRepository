

#Time ticks from Jan 1st 1970

import time;

print(time.time())
print(time.localtime())

print(time.asctime(time.localtime()))

print (time.altzone)

print(time.clock())
  
time.sleep(4)			# sleeps 4 seconds
 ### Calendar 

import calendar 

cal = calendar.month(2018,1)
#print (cal)