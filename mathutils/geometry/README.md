# Geometry
This module covers most aspects related to geometry, such as vectors an 3D analytic geometry itself.

## Vectors
There is a utility for pure vector calculations. It currently has vector **dot** ($`\vec{u} \cdot \vec{v}`$) and **crossed** ($`\vec{u} \wedge \vec{v}`$) product. When $`\vec{u} = (2,-1,3)`$ it will be introduced in the tool as `(2,-1,3)`.

For example, having $`\vec{u} = (2,-1,0)`$ and $`\vec{v} = (1,1,-2)`$, we can **store** those vectors assigning them to a variable (`u = (2,-1,0)` and `v = (1,1,-2)`)
### Dot Product
To get the dot product of $`\vec{u}`$ and $`\vec{v}`$ ($`\vec{u} \cdot \vec{v}`$) you just need to type in `u*v` or `u·v`. Raw vectors are also accepted `(2,-1,0)*(1,1,-2)`
### Cross product
Cross product works in a similar way, but only wedge (^) is allowed, so to get the cross product you type `u^v` or `(2,-1,0)^(1,1,-2)`

## Geometry
Math Utils can also work with geometric entities, such as points, lines and planes. To define a point, input the name of the point followed by its coordinates: `A(0,2,1)`

To define a plane, you must use its implicit equation and the equation must be preceded with a colon `:`. `pi: -2x+y-z=0`

A line is defined the same way, but 2 equations are needed: `r: 3x-y+z-1=0,y+z=-2`

To perform any operation any geometric entities involved **must be defined first**, unlike with vectors.

### Relative positions
Possible positions are:

| | Points | Line | Plane |
:-: |:-: | :-: | :-:
|Point| Alligned, coplanar or none | Point in Line or not | Point in Plane or not
|Line|❌|Concurrent, parallel, secant or they cross|Line in Plane, parallel or secant
|Plane|❌|Line in Plane, parallel or secant|(2 planes) Concurrent, parallel or secant

#### 3 Planes
3 planes have a total of 8 possible relative positions, which are described below:
<table>
    <thead>
        <tr>
            <th style="text-align:center"></th>
            <th style="text-align:center">RgA = RgA* = 3</th>
            <th style="text-align:center">RgA = 2, RgA* = 3</th>
            <th style="text-align:center">RgA = RgA* = 2</th>
            <th style="text-align:center">RgA = 1, RgA* = 2</th>
            <th style="text-align:center">RgA = RgA* = 1</th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td style="text-align:center">No coincident planes</td>
        <td rowspan=2><img width="384px" src="../../assets/RG3.png"/></td>
        <td><img width="256px" src="../../assets/RG23-Ind.png"/></td>
        <td><img width="256px" src="../../assets/RG2-Ind.png"/></td>
        <td><img width="256px" src="../../assets/RG12-Ind.png"/></td>
        <td rowspan=2><img width="384px" src="../../assets/RG1.png"/></td>
    </tr>
        <td style="text-align:center">There are coincident planes</td>
        <td><img width="256px" src="../../assets/RG23-Dep.png"/></td>
        <td><img width="256px" src="../../assets/RG2-Dep.png"/></td>
        <td><img width="256px" src="../../assets/RG12-Dep.png"/></td>
    <tr>
    </tr>
    </tbody>
</table>

### Distances
To get the distance between 2 elements you just type `d element1,element2` and you will get the distance and, if it is not a number by itself, it will be also expressed numerically. For example, `d r,pi` returns $`3`$ and `d P,r` gives back $`\sqrt{2}\hspace{2mm}(1.414213)`$

### Angles
Angles between 2 elements is requested with `< r,pi` and it will be given in **radians**. **Only lines and planes** can be introduced, and any point will give an error.