#!/usr/bin/env python

import os
import sys
from time import sleep 
import types

class Monster(object):

  def __init__(self, name="Trogg"):
    self.representations = [open('characters/monster1.txt').read()]
    self.name = name
  
  def show(self):
    os.system('clear')
    print self.representations[0] 
    sleep(3)
    os.system('clear')
      
  def devour(self,food_list):
    os.system('clear')
    print '\n\n'
    for food in food_list:
      print '\t\t' + food + '... very good!'
    sleep(3)

    self.show()
    os.system('clear')
    
  def speak(self):
    os.system('clear')
    print "\n\n\t\tI am Trooooogggggg!"
    sleep(3)
    self.show() 

class Wizard(object):

  representations = [ open('characters/wizard1.txt').read(),
                      open('characters/wizard2.txt').read()]

  def __init__(self,name="Dan Galf"):
    self.name = name 
  
  def speak(self,s):
    self.show()
    print s
    
  def show(self):
    os.system('clear')
    print self.representations[0]
    sleep(3)

  def stop_monster(self,obj):

    # some flashy wizard stuff before the spell
    os.system('clear')
    print self.representations[1]   
    sleep(3)
    os.system('clear')

    def devour(self,food_list):
      prohibited = ['people','cats','dogs']
      can_eat = [food for food in food_list if food not in prohibited] 
      os.system('clear')
      print self.representations[0]
      sleep(3)
      print "\n\n\t\t\t",\
            "Noooooooo, I can't eat", ','.join(i for i in prohibited[:-1]),\
            "and", prohibited[-1]
      sleep(1)

    if hasattr(obj,'devour'):
      print 'I, {}, hereby stop you, {}, from devouring people,\
                        cats and dogs. Beer, etc. is still okay, though.'\
                        .format(self.name,obj.name)

      # this part stops the monster
      obj.devour = types.MethodType(devour,obj)
      
