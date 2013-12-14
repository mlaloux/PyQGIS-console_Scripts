#!/usr/bin/python
# encoding: utf-8
"""
fonction et classe permettant de créer des couches virtuelles (memory layers) Quantum GIS
Martin Laloux 2012
class and function to create memory layers from the Python Console (geometry only)
"""
from qgis.core import *

    
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
