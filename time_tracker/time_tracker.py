import datetime as dt
import csv

taskName = input("Task Name: ")

start_dt = dt.datetime.now()

while(True):
    finish = input("Enter 'y' to finish: ")
    if finish == 'y':
        break

end_dt = dt.datetime.now()

# Time Delta Formatting
timeDelta = end_dt - start_dt
timeSec = timeDelta.seconds
hours, remainder = divmod(timeSec, 3600)
minutes, seconds = divmod(remainder, 60)
timeSecFormat = '{:02}h {:02}m'.format(int(hours), int(minutes))

#Converting to 12 hour format 
date = start_dt.strftime("%d/%m/%Y")
s_time = start_dt.strftime("%I:%M %p")
e_time = end_dt.strftime("%I:%M %p")

lastDateEntry = ""

# !!!!! Reading file. Fix this later !!!!! 
try:
    with open('time_tracker.csv', 'r', newline='') as file:
        try:
            last_line = file.readlines()[-1]
            lastDateEntry = last_line.split(",")[0]
        except:
            print('New file or formatting error detected.')
except FileNotFoundError:
    print('File not found. Creating new file.')

# Update file with new task
with open('time_tracker.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    if lastDateEntry != str(date) and lastDateEntry != "":
        writer.writerow('')
    writer.writerow([date, taskName, s_time, e_time, timeSecFormat])

# User message
print(f"You have worked on task {taskName} for {timeSecFormat}.")
print("CSV Updated.")
input("Press enter to close program.")