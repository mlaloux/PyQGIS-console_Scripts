PyQGIS-Scripts
==============

1) utilisation de (use of) create_memory_layer.py

```python
from create_memory_layer import Crea_couche
# création d'une couche point
pt = Crea_couche("points", "Point")
# ajout d'un point à la couche
line_start = QgsPoint(50,50)
pt.create_point(line_start)
# ajout d'un autre point à la couche
line_end = QgsPoint(100,150)
pt.create_point(line_end)
# fin de l'édition et affichage de la couche
pt.aff_couche
# création d'une couche ligne
li = Crea_couche("ligne", "LineString")
# ajout d'une ligne à la couche
li.create_ligne(line_start,line_end)
# fin de l'édition et affichage de la couche 
li.aff_couche
# création d'une couche polygones
pol = Crea_couche("poly", "Polygon") 
points = [QgsPoint(60,60),QgsPoint(60,80),QgsPoint(80,80),QgsPoint(80,60),QgsPoint(60,60)] 
pol.create_poly(points) 
# fin de l'édition et affichage de la couche 
pol.aff_couche
```
