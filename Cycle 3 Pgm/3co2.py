import time
print("Current time in sec",time.time())
print("Current time ",time.ctime())
print("Current time after 30 sec",time.ctime(time.time()+30))
print()
t=time.localtime()
print("Time t:",t)
print("Current year",t.tm_year)
print("Current month",t.tm_mon)
print("Current day",t.tm_mday)
print("Current hour",t.tm_hour)
print("Current minute",t.tm_min)
print("Current weekday",t.tm_wday)
