#!/usr/bin/env python
# encoding: utf-8
"""
PyQGIS_vect_algebra.py

Created by martin Laloux on 2013-05-15.
Copyright (c) 2013 __MyCompanyName__. All rights reserved.
"""

import math
from qgis.core import *

def mag(point):
     #magnitude d'un vecteur
     return math.sqrt(point.x()**2 + point.y()**2)

def dist(point1,point2):
    #PyQGIS: distance euclidienne entre 2 points#
    return math.sqrt(point1.sqrDist(point2))

def diff(point2, point1):
     # soustraction de 2 vecteurs
     return QgsPoint(point2.x()-point1.x(), point2.y() - point1.y())

def som(point2,point1):
     # addition entre 2 vecteurs
     return QgsPoint(point2.x()+point1.x(), point2.y()+point1.y())

def som_k(point, dx,dy):
    # translation d'un vecteur de dx, dy unités
	return QgsPoint(point.x()+dx, point.y()+dy)

def vecxscal(point,k):
     # multiplication d'un vecteur par un scalaire
     return QgsPoint(point.x()*k, point.y()*k)

def norm(point1, point2):
    # normalisation d'un vecteur
    point = diff(point2,point1)
    m = mag(point)
    return QgsPoint(point.x()/m, point.y()/m)

def normpt(point):
    # normalisation d'un vecteur point    
    m = mag(point)
    return QgsPoint(point.x()/m, point.y()/m)

def dot_product(point1, point2):
    # produit scalaire de 2 vecteurs 
    return (point1.x()*point2.x() + point1.y()*point2.y())

def det(point1, point2):
      # déterminant de 2 vecteurs
      return (point1.x*point2.y) - (point1.y*point2.x)

def car_pol(point):
	# cordonnées cartésiennes -> coordonnées polaires
    return mag(point),90 - azimut_pt(point)

def pol_car(dist, angle):
	# coordonnées polaire -> coordonnées polaires
    return QgsPoint(dist * math.cos(math.radians(angle)),dist * math.sin(math.radians(angle)))

def cosdir(point):
   # cosinus directeurs d'un vecteur point(x,y)
   cosa = point.x() / mag(point)
   cosb = point.y()/ mag(point)
   return cosa,cosb

def cosdir_azim(azim):
	# cosinus directeurs d'un azimut en degrés
    az = math.radians(azim)
    cosa = math.sin(az)
    cosb = math.cos(az)
    return cosa,cosb

