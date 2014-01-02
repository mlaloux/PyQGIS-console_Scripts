#!/usr/bin/python
# encoding: utf-8
"""
fonctions et classe permettant de créer des couches virtuelles (memory layers) Quantum GIS
Martin Laloux 2012
functions and class for creating memory layers in Quantum GIS

"""
from qgis.core import *

def point(x,y):
	# par paresse, pour ne pas taper QgsPoint(x,y) à chaque fois...
    return QgsPoint(x,y)
    
class Crea_couche(object):
    """création d'une couche virtuelle (memory layer) de type Point, LineString ou Polygon,
     ajout des géométries et affichage"""
    # création de la virtuelle à partir du nom et du type géométrique
    def __init__(self,nom,type):
         self.type=type
         self.name = nom
         self.layer =  QgsVectorLayer(self.type, self.name , "memory")
         self.pr =self.layer.dataProvider() 
    def create_point(self,geometry):
	    #ajout d'un point
        self.seg = QgsFeature()
        self.seg.setGeometry(QgsGeometry.fromPoint(geometry))
        self.pr.addFeatures([self.seg])
        self.layer.updateExtents()
    def create_ligne(self, point1,point2):
	    #ajout d'une ligne
        self.seg = QgsFeature()
        self.seg.setGeometry(QgsGeometry.fromPolyline([point1,point2]))
        self.pr.addFeatures( [self.seg] )
        self.layer.updateExtents()
    def create_poly(self,points):
	    #ajout d'un polygone
        self.seg = QgsFeature()  
        self.seg.setGeometry(QgsGeometry.fromPolygon([points]))
        self.pr.addFeatures( [self.seg] )
        self.layer.updateExtents()
    @property
    def aff_couche(self):
	    #fin de l'édition et affichage  de la couche
        QgsMapLayerRegistry.instance().addMapLayers([self.layer])
        
