#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Reminder Application
A bare-bones task management application

TODAY:
0. Talk about our schema
1. set up an sqlite3 database 
2. get user's task information 
3. convert the user's date and time information into a datetime object
4. commit our formatted user input to the database
5. get the <N> most recent tasks 

NEXT WEEK:
1. Improve the interface so we have options to ...
2. Provide task modification capabilities
3. modify our program so it takes command line arguments. Args include:
 - Number of weeks out to show tasks for
4. Abstract our database into a module and import that
5. Load schema from a file with executescript method
6. Have the reminder.py script email us with upcoming events
'''

# imports
import sys

import sqlite3

# set up database connection
connection = sqlite3.connect('db.db')
cursor = connection.cursor()

# write our schema statement, e.g. CREATE TABLE reminders (id INTEGER PRIMARY KEY)
# task_description text, date text, expired boolean, location text, notes text
sql_schema = '''CREATE TABLE IF NOT EXISTS reminders(task_id INTEGER PRIMARY KEY,
task TEXT, date TEXT, location TEXT, notes TEXT, expired BOOLEAN)'''

# use the cursor to create the new table
cursor.execute(sql_schema)


def getNewEvent():
  prompt = 'Press [ENTER] to add a task or q/Q to quit'
  response = raw_input(prompt).strip()
  if response in ['q','Q']:
    sys.exit()

  else:
    task = raw_input('task: ')
    year = raw_input('year (YYYY): ')
    month = raw_input('month (MM) : ')
    day = raw_input('day (DD): ')
    hour = raw_input('hour (HH): ')
    minute = raw_input('minute (MM): ')
    am_or_pm = raw_input('am or pm: ')
    notes = raw_input('additional information: ')
    
    data = [task,year,month,day,hour,minute,notes]

    cursor.execute('INSERT INTO reminders (task)
  
  

def commitNewEvent(event):
  pass
  
def getNMostRecent(N=4):
  pass

def getUpcomingEvents(N=4):
  pass


def mainLoop():
  getNewEvent()

mainLoop()

