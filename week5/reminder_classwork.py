#!/usr/bin/env python
# -*- coding: utf-8 -*-


import datetime
import sys
import sqlite3

# set up database connection
connection = sqlite3.connect('db.db')
cursor = connection.cursor()

sql_schema = '''CREATE TABLE IF NOT EXISTS \
				reminders(task_id INTEGER PRIMARY KEY,
				task TEXT, date TEXT, notes TEXT, \
				expired BOOLEAN)'''

cursor.execute(sql_schema)


def getNewEvent():

	prompt = 'Press [ENTER] to add a task or q/Q to quit'
	response = raw_input(prompt).strip()
  
	if response in ['q','Q']:
		sys.exit()

	else:

		task = raw_input('task: ').strip()
		year = raw_input('year (YYYY): ').strip()
		month = raw_input('month (MM) : ').strip()
		day = raw_input('day (DD): ').strip()
		hour = raw_input('hour (HH): ').strip()
		minute = raw_input('minute (MM): ').strip()
		am_or_pm = raw_input('am or pm: ').strip()
		notes = raw_input('additional information: ').strip()

		time_string = datetime.datetime(int(year),int(month),int(day),int(hour),int(minute))

		data = [task,time_string,notes,False]


	# task TEXT, date TEXT, location TEXT, notes TEXT, expired BOOLEAN
	cursor.execute('INSERT INTO reminders (task, date, notes, expired) VALUES (?,?,?,?)', data )

	connection.commit()
	
	rows = cursor.execute('SELECT * FROM reminders')
	
	# ROW == RECORD
	for row in rows: # 0, dentist, 124 main, n/a, False
		for field in row:
			print field
		print '####'

def commitNewEvent(event):
	pass
  
def getNMostRecent(N=4):
	pass

def getUpcomingEvents(N=4):
	pass

def mainLoop():
	getNewEvent() # take user input

mainLoop() # program starts here
