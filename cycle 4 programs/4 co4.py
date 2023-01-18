class Time:
    def __init__(self):
        self.__h=int(input("Enter the time in hour"))
        self.__m=int(input("Enter the time in minutes"))
        self.__s=int(input("Enter the time in seconds"))
        
    def __add__(self,tob2):
        hours=self.__h+tob2.__h
        print("sum of hours",hours)
        minutes=self.__m+tob2.__m
        print("sum of minutes",minutes)
        seconds=self.__s+tob2.__s
        print("sum of seconds",seconds)
        
        if hours>=24:
            hours=hours%24
       
        if minutes>=60:
            hours=hours+minutes//60
            minutes=minutes%60
            
        if seconds>=60:
            minutes=minutes+seconds//60
            seconds=seconds%60
            
        return hours,minutes,seconds
    
print("Enter the time of first object")
tob1=Time()   
print("Enter the time of second object")
tob2=Time()    
print("sum of two time is:(Hours,minute,second)",tob1+tob2)