#!/usr/bin/env python

f = open('events.txt')
lines = f.readlines()
f.close()

filtered_lines = []
dates = []
events = []

for line in lines:
    line = line.strip()
    if len(line):
        filtered_lines.append(line)
        
for line in filtered_lines:
    date,event = line.split(',')
    dates.append(date.strip())
    events.append(event.strip())
    
reminder_items = zip(dates,events)
print reminder_items
