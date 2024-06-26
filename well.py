import numpy as np
import shapely as sh

class ZoneDefinition:
    def __init__(self,name,average_porosity,net_thickness) -> None:
        self.name=name
        self.average_porosity=average_porosity
        self.net_thickness=net_thickness

class Well:
    def __init__(self,location,*zones:ZoneDefinition):
        self.location:sh.Point=location
        self.zones:ZoneDefinition=[]
        if len(zones)>0:
            for zone in zones:
                self.zones.append(zone)

