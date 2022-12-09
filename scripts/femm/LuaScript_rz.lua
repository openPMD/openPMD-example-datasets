-- This Lua script exports B field data on
-- 2D-rz coordniate grid points
-- from a 2D-RZ FEMM simulation.
-- The data is saved into txt fiels.

-- The B field describes a magnetic mirror.
-- The meaningful region of the mirror field is
-- within 0<r<1 and 0<z<5.
-- Three extra data points are taken in the two ends of
-- z and the big end of r for guard cells used in WarpX.

-- FEMM file used: `mirror.FEM`.
-- FEMM website: `https://www.femm.info/wiki/HomePage`.

-- cell sizes
dr = 0.025
dz = 0.125

-- minimum and maximum values
-- rmin should not be less than 0
rmin =  0.0
rmax =  1.15
zmin = -0.375
zmax =  5.375

-- number of cells
nr = floor( (rmax-rmin)/dr )
nz = floor( (zmax-zmin)/dz )

-- create and open data files
handle_Br = openfile("Br_rz.txt","w")
handle_Bz = openfile("Bz_rz.txt","w")

-- loop over grid points
for i = 0, nr, 1 do
  r = rmin + i*dr
  for j=0, nz, 1 do
    z = zmin + j*dz
    -- read data
    A, Br, Bz = mo_getpointvalues(r,z)
    -- write to files
    write(handle_Br,Br,"\n")
    write(handle_Bz,Bz,"\n")
  end
end

-- close files
closefile(handle_Br)
closefile(handle_Bz)
