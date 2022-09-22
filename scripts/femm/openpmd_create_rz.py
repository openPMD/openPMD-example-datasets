import openpmd_api as io
import numpy as np

# number of grid points
# nr*nz = the number of lines in B*_rz.txt
nr = 47
nz = 47

# create openpmd file
series = io.Series("example-femm-thetaMode.h5",io.Access.create)

# only 1 iteratiion needed
it = series.iterations[1]

# read data
fr = open("Br_rz.txt", "r+")
fz = open("Bz_rz.txt", "r+")
Br_lines = fr.readlines()
Bz_lines = fz.readlines()
fr.close()
fz.close()

# create arrays
r_data = np.arange(nr*nz,dtype=np.float64).reshape(nr,nz)
z_data = np.arange(nr*nz,dtype=np.float64).reshape(nr,nz)

c = 0
for i in range(nr):
    for j in range(nz):
        r_data[i,j] = float(Br_lines[c])
        z_data[i,j] = float(Bz_lines[c])
        c += 1

# set information
B = it.meshes["B"]
# cell size
B.grid_spacing = [0.025, 0.125]
# physical minimum values
B.grid_global_offset = [0.0, -0.375]
# set geometry
B.geometry = io.Geometry.cylindrical

# label
B_r = B["0"]
B_t = B["1"]
B_z = B["2"]

dataset = io.Dataset(r_data.dtype,r_data.shape)
B_r.reset_dataset(dataset)
B_t.reset_dataset(dataset)
B_z.reset_dataset(dataset)

B_r.store_chunk(r_data)
B_t.make_constant(0.0)
B_z.store_chunk(z_data)

# If warpx.E_ext_grid_init_style = "read_from_file" is not set
# in thee WarpX input file, the following E field data
# is not needed, i.e., the block below can be removed.
##################################################
E = it.meshes["E"]
E.grid_spacing = [0.025, 0.125]
E.grid_global_offset = [0.0, -0.375]
E.geometry = io.Geometry.cylindrical

E_r = E["0"]
E_t = E["1"]
E_z = E["2"]

dataset = io.Dataset(r_data.dtype,r_data.shape)
E_r.reset_dataset(dataset)
E_t.reset_dataset(dataset)
E_z.reset_dataset(dataset)

# E is zero in this example
E_r.make_constant(0.0)
E_t.make_constant(0.0)
E_z.make_constant(0.0)
##################################################

series.flush()

del series
