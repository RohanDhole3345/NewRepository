#Find the keyword on whole dataset
import re
file=r"C:\Users\ASUS\OneDrive\Desktop\Python 2025\Tasks\small.log"

keyword=input("Enter a keyword to search you in File:").upper()
count=0

with open(file,"r") as f:
    for line in f:
        if keyword in line.upper(): #check keyword in line
            count += 1 #increase the ccount

print(f"\nThe word'{keyword}'occurred {count} times in File.")
