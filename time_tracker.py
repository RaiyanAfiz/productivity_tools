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

date = start_dt.strftime("%d/%m/%Y")
s_time = start_dt.strftime("%I:%M %p")
e_time = end_dt.strftime("%I:%M %p")

lastDateEntry = ""

with open('time_tracker.csv', 'r', newline='') as file:
    last_line = file.readlines()[-1]
    lastDateEntry = last_line.split(",")[0]

with open('time_tracker.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',')
    if lastDateEntry != str(date):
        writer.writerow('')
    writer.writerow([date, taskName, s_time, e_time, timeSecFormat])


print("Updated.")