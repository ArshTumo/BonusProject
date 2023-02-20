import time

inp = input("Insert time to count down (h:m:s)")
colon1,colon2,hours,minutes,seconds = 0,0,0,0,0
lst1 = list(inp)
colon1 = lst1.index(':')

if colon1 == 2:
    hours = int(lst1[0])*10+int(lst1[1])
    del lst1[0:3]
elif colon1 == 1:
    hours = int(lst1[0])
    del lst1[0:2]

colon2 = lst1.index(':')

if colon2 == 2:
    minutes = int(lst1[0])*10+int(lst1[1])
    del lst1[0:3]
elif colon2 == 1:
    minutes = int(lst1[0])
    del lst1[0:2]

if len(lst1) == 2:
    seconds = int(lst1[0])*10+int(lst1[1])
    del lst1[0:3]
elif len(lst1) == 1:
    seconds = int(lst1[0])
    del lst1[0:2]

all_minutes = int(hours) * 60 + int(minutes)
all_seconds = all_minutes * 60 + int(seconds)

for i in range(all_seconds, 0, -1):
    seconds = i % 60
    all_minutes = int(i / 60) % 60
    hours = int(i / 3600) % 24
    print(f"{hours:02}:{all_minutes:02}:{seconds:02}")
    time.sleep(1)