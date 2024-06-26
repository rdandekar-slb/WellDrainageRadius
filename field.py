import shapely as sh
import shapefile as sf
import numpy as np

class Field:
    # name:str = ""
    # map:sh.Polygon = sh.Polygon
    # sthiip:float = 0.0

    def __init__(self,name):
        self.map:sh.Polygon=None
        self.faults:sh.MultiLineString=None
        self.name:str=name
        self.sthiip:float=0.0

    def get_map_from_shapefile(self,shapefilename):
        shape=sf.Reader(shapefilename)
        return shape.shapeTypeName
    
    def get_map_from_cps3(self,filename):
        points=[]
        f=open(file=filename,mode='r')
        lines=f.readlines()
        for line in lines:
            if (line.strip()[0]).isnumeric():
                p=line.split()
                points.append(np.array([float(p[0]),float(p[1])]))
        self.map=sh.Polygon(points)
        # return np.array(points)
        return
    
    def get_faults_from_cps3(self,*filenames):
        if len(filenames)==0:
            self.faults=None
            return
        linestrings=[]
        for filename in filenames:
            f=open(file=filename,mode='r')
            lines=f.readlines()
            points=[]

            for line in lines:
                if (line.strip()[0]).isnumeric():
                    p=line.split()
                    points.append(np.array([float(p[0]), float(p[1])]))
            linestrings.append(sh.LineString(points))
        self.faults=sh.MultiLineString(linestrings)
        return



if __name__=="__main__":
    myfield = Field("Rashmin")
    # shapetype=myfield.get_map_from_shapefile(shapefilename=r"C:\Users\rdandekar\Desktop\Brillig_8080_shp.shp")
    # print(shapetype)

    points=myfield.get_map_from_cps3(r"C:\Users\rdandekar\Desktop\Brillig_8080")
    print(points)



