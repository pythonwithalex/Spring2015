#!/usr/bin/env python
'''
A console-based reminder application.

usage: remind.py -[d,m,y] N

options:
-d, returns all events in the events file within the range of NUM days from toda
y
-m, same as -d but the range is calculated in months
-y, same as -y but the range is calculated in years
'''

import datetime

events_file='events.txt'

def parse_file_to_events(events_file):

  f = open(events_file)
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

parse_file_to_events(events_file)
