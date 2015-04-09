#!/usr/bin/env python

# In progress

# problem taken from Skiena's Algorithm Design Manual
# This is an incorrect way to calculate the most optimal route for a robot
# arm to hit each contact point in a set of contact points
# and return to the original 

import math
import random
import sys

# setup for skiena's robot tour problem
# attempt #1, the closest neighbor heuristic

# generate N coordinates in a single-quadrant coord system 
# of MAX_X width, MAX_Y height
# 0,0 is top left

def generate_points(N,MAX_X=10,MAX_Y=10):
  points = set()
  while len(points) < N:
    point = (random.randrange(MAX_X),random.randrange(MAX_Y))
    points.add(point)
  return list(points)

def pair_distance(p1,p2):
  a = p1[0] - p2[0]
  b = p1[1] - p2[1]
  c = math.sqrt( (a*a) + (b*b) )
  return c

def get_next_point(this_point,remaining_points):
  # returns index of next closest point
  distances = [ pair_distance(this_point,i) for i in remaining_points ]
  return distances.index(min(distances))


points = generate_points(5)
this_point = points[0]
remaining_points = [p for p in points if p is not this_point]
next_point = get_next_point(this_point,remaining_points)

print 'points: ',points
print 'this_point: ',this_point
print 'next_point: ',remaining_points[next_point]
