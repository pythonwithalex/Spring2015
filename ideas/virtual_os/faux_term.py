#!/usr/bin/env python

'''
  Fauxterm is a humble Virtual Operating System meant for teaching Python and Unix/BSD!

PLAN:

1. make a list of features:
  accounts
  date
  filesystem and file management tools 
  network

'''

import os
import re 
import sys

from shell_functions import ls
shell_functions_dict = {
  'ls' : ls,
}

os.system('clear')

prompt = 'student@mac [~/Student]$ '

accounts = {}
filesystem = {}


def understand(response):
  ''' parses entered line into command and arguments '''
  if response.strip():
    return response.strip().split() 
  else:
    return None

def evaluate(response_list):
  ''' checks first item in understood response against shell_funcs dict '''
  command = response_list[0]
  if command.strip().lower() in ['exit']:
    sys.exit(0)
  shell_functions_dict['ls']()

def main():

  while True:
    response = raw_input(prompt)
    understood_response = understand(response)
    if understood_response: 
      evaluate(understood_response)

main()
