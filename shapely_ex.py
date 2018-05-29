#shapely part

import matplotlib.pyplot as plt
%matplotlib inline
from shapely.geometry import Polygon,Point, LineString
from descartes.patch import PolygonPatch

##linestring
A=(0,0)
B=(1,0)
C=(2,0)
D=(0,1)
E=(1,1)
F=(2,1)

AF= LineString([A,B,C,D,E,F])

##creating polygons
square=Polygon([[0,0],[1,0],[1,1],[0,1]])
Tri1=Polygon([(0,0),(1,0),(0,1)])
Tri2=Polygon([(1,1),(0,1),(1,0)])

##intersections
Tri1.intersection(Tri2)
square.intersection(Tri1)
square.intersection(Tri2)

##Unions
square.union(Tri1)
square.union(Tri2)
Tri1.union(Tri2)

##creating figure
def plot_line(ax, ob):
    x, y = ob.xy
    ax.plot(x, y, color='red', linewidth=3, solid_capstyle='round', zorder=1)
fig = plt.figure(1, figsize=(10, 4), dpi=180)


ax = fig.add_subplot(421)

plot_line(ax, AF)

ax=fig.add_subplot(422)
patch=PolygonPatch(square)
ax.add_patch(patch)

ax=fig.add_subplot(423)
patch=PolygonPatch(Tri1)
ax.add_patch(patch)

ax=fig.add_subplot(424)
patch=PolygonPatch(Tri2)
ax.add_patch(patch)

ax=fig.add_subplot(425)
plot_line(ax,Tri1.intersection(Tri2))

ax=fig.add_subplot(426)
patch=PolygonPatch(Tri1.union(Tri2))
ax.add_patch(patch)

ax=fig.add_subplot(427)
patch=PolygonPatch(Tri1.union(square))
ax.add_patch(patch)

ax=fig.add_subplot(428)
patch=PolygonPatch(Tri2.union(square))
ax.add_patch(patch)
