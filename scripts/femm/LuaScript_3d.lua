-- This Lua script exports B field data on
-- 3D-xyz coordniate grid points
-- from a 2D-RZ FEMM simulation.
-- The data is saved into txt fiels.

-- The B field describes a magnetic mirror.
-- The meaningful region of the mirror field is
-- within 0<r<1 and 0<z<5.
-- Three extra data points are taken in the two ends of
-- r and z respectively for guard cells used in WarpX.

-- FEMM file used: `mirror.FEM`.
-- FEMM website: `https://www.femm.info/wiki/HomePage`.

-- cell sizes
dx = 0.05
dy = 0.05
dz = 0.125

-- minimum and maximum values
xmin = -1.15
xmax =  1.15
ymin = -1.15
ymax =  1.15
zmin = -0.375
zmax =  5.375

-- number of cells
nx = floor( (xmax-xmin)/dx )
ny = floor( (ymax-ymin)/dy )
nz = floor( (zmax-zmin)/dz )

-- create and open data files
handle_Bx = openfile("Bx_3d.txt","w")
handle_By = openfile("By_3d.txt","w")
handle_Bz = openfile("Bz_3d.txt","w")

-- loop over grid points
for i = 0, nx, 1 do
  x = xmin + i*dx
  for j = 0, ny, 1 do
    y = ymin + j*dy
    r = sqrt(x*x + y*y)
    t = atan2(y,x)
    for k = 0, nz, 1 do
      z = zmin + k*dz
      -- read data
      A, Br, Bz = mo_getpointvalues(r,z)
      -- write to files
      write(handle_Bx,Br*cos(t),"\n")
      write(handle_By,Br*sin(t),"\n")
      write(handle_Bz,Bz,"\n")
    end
  end
end

-- close files
closefile(handle_Bx)
closefile(handle_By)
closefile(handle_Bz)
