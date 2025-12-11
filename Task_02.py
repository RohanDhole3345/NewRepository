import re
from datetime import datetime

file = r"C:\Users\ASUS\OneDrive\Desktop\Python 2025\Tasks\small.log"

# define timestamp pattern-[YYYY-MM-DD HH:MM:SS]
pattern = r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\]"

timestamps = []

with open(file, "r") as f:
    for line in f:
        match = re.search(pattern,line)
        if match:
            timestamps.append(match.group(1))

# Convert to datetime
dt_list=[datetime.strptime(t,"%Y-%m-%d %H:%M:%S") for t in timestamps]

#find min and max
starttime = min(dt_list)
endtime = max(dt_list)

print("Start Time :",starttime)
print("End Time :",endtime)
print("Time Range :",endtime-starttime)
