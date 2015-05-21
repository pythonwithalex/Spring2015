#!/usr/bin/env python

import os
import Queue
import sys
from threading import Thread
from time import sleep 
import types


class Projector(object):

  def __init__(self,queue):
    self.queue = queue 

  def build_scene(self,text):
    pass

  def _clear(self):
    os.system('clear')

  def _process_queue(self):
    while 1:
      if self.queue.not_empty:
        text,art = self.queue.get()
        if text:
          self._clear()
          print text
          sleep(2)
        if art:
          self._clear()
          print art
          sleep(2)
        if text in 'Fin...':
          sys.exit(0)

  def start_film(self):
    loop = Thread(target=self._process_queue,args=())
    loop.start()

class Narrator(object):

  def __init__(self,queue):
    self.queue = queue

  def speak(self,s):
    self.queue.put( (s,None) )

class Monster(object):
  representations = [ open('characters/monster1.txt').read(),
                      open('characters/monster2.txt').read()]

  def __init__(self,queue,name="Trogg"):

    self.name = name or "Trogg"
    self.queue = queue
  
  def devour(self,food_list):
    statements = ["{} ... very good!".format(item) for item in food_list]
    joined_statements = "\n\n".join(s for s in statements)
    self.queue.put((joined_statements,
                    self.representations[0]) 
                  )

  def speak(self):
    self.queue.put(("I am Trooooogggggg!", self.representations[0]))
    
class Wizard(object):

  representations = [ open('characters/wizard1.txt').read(),
                      open('characters/wizard2.txt').read()]

  def __init__(self,queue,name="Dan Galf"):
    self.name = name 
    self.queue = queue
  
  def speak(self,s):
    self.queue.put((s,self.representations[0]))

  def stop_monster(self,obj):
       
    def devour(self,food_list):
      self.queue.put(('I can\'t devour humans any more!',
                      self.representations[0]))

    if hasattr(obj,'devour'):
      self.queue.put( ('I, {}, hereby stop you, {}, from devouring people,\
                      cats and dogs. Beer, etc. is still okay, though.'\
                      .format(self.name,m.name),
                      self.representations[0]))

      obj.devour = types.MethodType(devour,obj)   

os.system('clear')
q = Queue.Queue()

p = Projector(q)
p.start_film()

m = Monster(q)
w = Wizard(q)
n = Narrator(q)

n.speak('A Long Time Ago, A Monster Was Born')
m.speak()
n.speak('Here is the monster now, devouring all things in his path ...')
m.devour(['birds','beer','ice','rocks','metal','a cat','people'])
n.speak('And then a wizard named {}, who had previously found {} on\
         wizardnet and decided that he needed to be stopped'.format(
                                                             w.name,m.name))
w.stop_monster(m)
n.speak('After the wizard cast his spell, the monster tried to devour people')
m.devour(['people','cats','dogs'])
n.speak('Fin...')
