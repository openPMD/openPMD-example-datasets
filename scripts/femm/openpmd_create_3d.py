import openpmd_api as io
import numpy as np

# number of grid points
# nx*ny*nz = the number of lines in B*_3d.txt
nx = 47
ny = 47
nz = 47
# read data
Bx_data = np.loadtxt('Bx_3d.txt').reshape(nx, ny, nz)
By_data = np.loadtxt('By_3d.txt').reshape(nx, ny, nz)
Bz_data = np.loadtxt('Bz_3d.txt').reshape(nx, ny, nz)

# create openpmd file
series = io.Series("example-femm-3d.h5",io.Access.create)
# only 1 iteratiion needed
it = series.iterations[1]            
# set meta information
B = it.meshes["B"]
B.grid_spacing = [0.05, 0.05, 0.125]
B.grid_global_offset = [-1.15, -1.15, -0.375]
B.axis_labels = ['x', 'y', 'z']
B.geometry = io.Geometry.cartesian
# unit system agnostic dimension
B.unit_dimension = {
    io.Unit_Dimension.M:  1,
    io.Unit_Dimension.I: -1,
    io.Unit_Dimension.T: -2
}

# label
B_x = B["x"]
B_x.position = [0,0,0]
B_y = B["y"]
B_y.position = [0,0,0]
B_z = B["z"]
B_z.position = [0,0,0]

dataset = io.Dataset(Bx_data.dtype, Bx_data.shape)
B_x.reset_dataset(dataset)
B_y.reset_dataset(dataset)
B_z.reset_dataset(dataset)

B_x.store_chunk(Bx_data)
B_y.store_chunk(By_data)
B_z.store_chunk(Bz_data)

E = it.meshes["E"]
# set meta information
E.grid_spacing = np.array([0.05, 0.05, 0.125])
E.grid_global_offset = np.array([-1.15, -1.15, -0.375])
E.axis_labels = ['x', 'y', 'z']
E.geometry = io.Geometry.cartesian
# unit system agnostic dimension
E.unit_dimension = {
    io.Unit_Dimension.M:  1,
    io.Unit_Dimension.L:  1,
    io.Unit_Dimension.I: -1,
    io.Unit_Dimension.T: -3
}

# label
E_x = E["x"]
E_x.position = [0,0,0]
E_y = E["y"]
E_y.position = [0,0,0]
E_z = E["z"]
E_z.position = [0,0,0]

dataset = io.Dataset(Bx_data.dtype,Bx_data.shape)
E_x.reset_dataset(dataset)
E_y.reset_dataset(dataset)
E_z.reset_dataset(dataset)

# E is zero in this example
E_x.make_constant(0.0)
E_y.make_constant(0.0)
E_z.make_constant(0.0)

series.flush()

del series
