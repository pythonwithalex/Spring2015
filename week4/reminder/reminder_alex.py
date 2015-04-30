#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Reminder Application

Command-Line utility that lets you add tasks to a local database
and look them up 

Problems we need to solve 

TODAY
1. setting up a database with sqlite3
2. getting user input
3. converting the date and time information into a robust format
4. committing our formatted user input to our database
5. retrieving tasks

NEXT WEEK:


'''

import datetime
import os

import sqlite3

# for testing
#if os.path.isfile('db.db'):
#  os.remove('db.db')

# setup the database connection

connection = sqlite3.connect('db.db')
connection.text_factory = str
cursor = connection.cursor()

sql_create_statement = 'CREATE TABLE if not exists reminders(id INTEGER PRIMARY KEY, time TEXT, task TEXT, expired BOOLEAN)'
cursor.execute(sql_create_statement)

def getNewEvent():
  # this could be refactored into a for loop
  year = raw_input('year (yyyy): ').strip()
  month = raw_input('month (mm): ').strip()
  day = raw_input('day (dd): ').strip()
  hr = raw_input('hour (hh): ').strip()
  minute = raw_input('minute (mm): ').strip()
  task = raw_input('reminder task: ').strip()

  time_string = "{}-{}-{} {}:{}:01".format(year,month,day,hr,minute)
  time_string = datetime.datetime.strptime(time_string,"%Y-%m-%d %H:%M:%S") 
  return dict(time=time_string,task=task)

def commitNewEvent(event):
  cursor.execute('INSERT INTO reminders(time,task,expired) VALUES(?,?,?)',\
  (event['time'],event['task'],False))
  connection.commit()
  
def showEvents():
  row = cursor.execute('SELECT * FROM reminders')
  for entry in row:
    print entry

def getUpcomingEvents(N=4):
  sql_query='select time, task from reminders order by time DESC LIMIT {};'.format(N)
  for row in cursor.execute(sql_query):
    print row
  

def mainLoop():
  prompt = 'Hit [Return] to Add a new Task or q/Q to Quit'
  while raw_input(prompt).strip() not in ['q','Q']:
    new_event = getNewEvent()
    commitNewEvent(new_event)

  print 'getting last 4 events...'
  getUpcomingEvents()

if __name__ == '__main__':
  mainLoop()
