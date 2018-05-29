
If you are using Anaconda you should have no problems in installing all the libraries required by this lab. You will need:

- matplotlib (install it via Anaconda)
- shapely (install it via Anaconda)
- descartes, open the Anaconda prompt and type

  ```
  conda install -c conda-forge descartes
  ```


# Matplotlib

For this part use the file matplotlib_ex.py

In this part of the lab we will focus on creating subplots for your data. Specific methods for visualizing different kind of data can always be found in the online documentation ([https://matplotlib.org](https://matplotlib.org))


- Start by importing matplotlib

  ```
  import matplotlib.pyplot as plt
  ```

- Draw the following points in a scatterplot

  ```
  [(0,0),(1,0),(0,1),(1,1)]
  ```

  (search for 'scatter' in the documentation). Set the size of the points to 30 and their color to red. Notice that your function 'scatter' requires two distinct list of values (one for the x coordinates and one for the y coordinates) so you will have to modify the following list.


- Draw a line segment (starting from the very same set of points) by using the function plot

- Create a subplot (1 row, 2 columns). In the first column put the scatterplot and in the second column put the plot of the line segment.


# Shapely

For this part use file shapely_ex.py

#### Points and Lines
- Construct a list of 6 point objects with x-coordinates [0, 1, 2, 0, 1, 2] and y-coordinates [0, 0, 0, 1, 1, 1].

- Construct a LineString from all the points.

#### Points and Lines

Create a square and two triangles using the points from the previous section as vertices.

1. Calculate the intersection of the two triangles?

2. Test whether the square intersects each of the triangles.

3. Calculate the union of all the shapes.
(The answers will depend on how you arrange your polygons).

4. Create a single figure for these results organized in multiple subplots. You will have to show, the line string, the three polygons independently, the results of points 1, 3.


Recall that for drawing a polygon you will have to

  - import the descartes library
  ```
  from descartes.patch import PolygonPatch
  ```

  - create a patch from the polygon (function `PolygonPatch`)
  - add the patch to the plot

Also look at the method `.xy` that you can call on a Geometry object. This returns two list of coordinates (x and y coordiantes for each point of a point collection,line string, polygon) quite useful for matplotlib.
