import re
from datetime import datetime

file=r"C:\Users\ASUS\OneDrive\Desktop\Python 2025\Tasks\small.log"

# Timestamp pattern: [YYYY-MM-DD HH:MM:SS]
pattern=r"\[(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})\]"

timestamps=[]      # for time range
error_per_day={}   # normal dictionary for counting errors per day

#------------------------------------------------------------------------------
#Second Task→Time Range
with open(file,"r") as f:
    for line in f:
        match=re.search(pattern, line)
        if match:
            # combine group(1) date + group(2) time
            full_ts=match.group(1)+" "+match.group(2)
            timestamps.append(full_ts)

# Convert all timestamps→datetime list
dt_list = [datetime.strptime(t,"%Y-%m-%d %H:%M:%S") for t in timestamps]

# Find earliest and latest time
start_time=min(dt_list)
end_time=max(dt_list)

print("Start Time :",start_time)
print("End Time   :",end_time)
print("Time Range :",end_time-start_time)

#------------------------------------------------------------------------------
#Third Task→Count ERROR per day
with open(file, "r") as f:
    for line in f:
        if "ERROR" in line:              # only check error lines
            match=re.search(pattern, line)
            if match:
                date=match.group(1) # extract only date

                # Add new date and initialise as 0 to start the new count
                if date not in error_per_day:
                    error_per_day[date]=0

                # increase count if date in list
                error_per_day[date]+=1

# Print the error per days
print("\nErrors per day:")
for date in sorted(error_per_day.keys()):#keys used to give all dates to for loop and sorted used to sort the dates
    print(f"{date}:{error_per_day[date]} errors")
