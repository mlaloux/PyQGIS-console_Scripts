
""" adapted from [Create a square grid polygon shapefile with python](http://gis.stackexchange.com/questions/54119/create-a-square-grid-polygon-shapefile-with-python/78030#78030)"""

from create_memory_layer import  *
from math import ceil
canvas= qgis.utils.iface.mapCanvas()
layer canvas.layer(0)

xmin,ymin,xmax,ymax = layer.extent().toRectF().getCoords()
gridWidth = 1000
gridHeight = 1000
rows = ceil((ymax-ymin)/gridHeight)
cols = ceil((xmax-xmin)/gridWidth)
ringXleftOrigin = xmin
ringXrightOrigin = xmin + gridWidth
ringYtopOrigin = ymax
ringYbottomOrigin = ymax-gridHeight
pol = Crea_couche("grille", "Polygon")
for i in range(int(cols)):
     # reset envelope for rows
     ringYtop = ringYtopOrigin
     ringYbottom =ringYbottomOrigin
     #print i, ringYtop, ringYbottom
     for j in range(int(rows)):
          poly = [QgsPoint(ringXleftOrigin, ringYtop),QgsPoint(ringXrightOrigin, ringYtop),QgsPoint(ringXrightOrigin, ringYbottom),QgsPoint(ringXleftOrigin, ringYbottom),QgsPoint(ringXleftOrigin, ringYtop)] 
          pol.create_poly(poly) 
          ringYtop = ringYtop - gridHeight
          ringYbottom = ringYbottom - gridHeight
     ringXleftOrigin = ringXleftOrigin + gridWidth
     ringXrightOrigin = ringXrightOrigin + gridWidth
     
pol.aff_couche
