#   dates and time module : import a module named datetime to work with dates as date objects.
#   the date contains year,month,day,hour,minute,second,and microsecond.
#   import datetime

#   the method is called strftime(), and take one parameter, format, to specify the formate of the returned string:
#   %b  : month name, short version dec
#   %B  : - -   -   -   -   -   -   december
#   %m  : month as number 01-12     12
#   %y  : year,short version, without century  24
#   %Y  :   year full version                   2024
#   %H  :   hour 00-23                          17
#   %I  :   hour 00-12                          05
#   %p  :   AM/PM                               PM
#   %M  :   Minute  00-59                       40
#   %S  :   second                              20
import datetime
x = datetime.datetime.now()
n = x.strftime("%Y-%m-%d")
m = x.strftime("%H:%M:%S:%p")
print(n)
print(m)
print(x)

print(datetime.datetime(2020,1,3))