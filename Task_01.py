file = r"C:\Users\ASUS\OneDrive\Desktop\Python 2025\Tasks\task-1\small" \
".log"

InfoCount = 0
WarnCount = 0
ErrorCount = 0
Total = 0

with open(file, "r") as f:
    for line in f:
        Total += 1
        line = line.upper()

        if "INFO" in line:
            InfoCount += 1
        if "WARN" in line:
            WarnCount += 1
        if "ERROR" in line:
            ErrorCount += 1

print("Total entries:", Total)
print("INFO:", InfoCount)
print("WARN:", WarnCount)
print("ERROR:", ErrorCount)
