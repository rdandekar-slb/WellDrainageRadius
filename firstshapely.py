
# from shapely import Polygon
import shapely as sh
import numpy as np
import shapely.plotting as shplt
import matplotlib.pyplot as plt
import field as fm


from figures import SIZE, BLACK, BLUE, GRAY, YELLOW, set_limits


def get_map_bounds(input_poly:sh.Polygon):
    ret_val=[]
    for bound in np.concatenate((np.floor(np.array(input_poly.bounds[:2])),np.ceil(np.array(input_poly.bounds[2:])))):
        ret_val.append(int(bound))
    return ret_val



myfield:fm.Field = fm.Field("Brillig")
# myfield.name="Brillig"

myfield.map=sh.Polygon((sh.Point(0,0),sh.Point(0,50),sh.Point(50,50),sh.Point(50,0),sh.Point(0,0)))
myfield.get_map_from_cps3(r"C:\Users\rdandekar\Desktop\DLs\Data\Brillig_8080")
# myfield.get_faults_from_cps3(r"C:\Users\rdandekar\Desktop\DLs\Data\Fault10.cps",r"C:\Users\rdandekar\Desktop\DLs\Data\Fault20.cps")

# mygeom=sh.union(myfield.map,myfield.faults)
# print(sh.get_type_id(mygeom))
map_bounds=get_map_bounds(myfield.map)
# print(map_bounds)
fig,ax=plt.subplots()
fig.set_dpi(90)
fig.set_figheight(8)
fig.set_figwidth(8)
ax.set_title(myfield.name)
shplt.plot_polygon(myfield.map,ax=ax,add_points=False)
# shplt.plot_line(myfield.faults,ax=ax,add_points=False)
set_limits(ax,map_bounds[0]-1,map_bounds[2]+1,map_bounds[1]-1,map_bounds[3]+1)
# plt.show()



# print(r)
# print(p.x, p.y)
# p=sh.Polygon([[0,0],[1,0],[1,1],[0,1],[0,0]])
# print(p.geom_type)
