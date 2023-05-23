#!/usr/bin/env python3
import openpmd_api as io
import numpy as np

# number of grid points
# nr*nz = the number of lines in B*_rz.txt
num_nodes = 1
nr = 47
nz = 47
# read data
Br_data = np.loadtxt('Br_rz.txt').reshape(num_nodes, nr, nz)
Bz_data = np.loadtxt('Bz_rz.txt').reshape(num_nodes, nr, nz)

# create openpmd file
series = io.Series("example-femm-thetaMode.h5",io.Access.create)
# only 1 iteratiion needed
it = series.iterations[1]

# set meta information
B = it.meshes["B"]
B.grid_spacing = np.array([0.025, 0.125])
B.grid_global_offset = [0.0, -0.375]
B.axis_labels = ['r', 'z']
B.geometry = io.Geometry.thetaMode
B.geometry_parameters = "m=" + str(num_nodes) + ";imag=+"

B.unit_dimension = {
    io.Unit_Dimension.M:  1,
    io.Unit_Dimension.I: -1,
    io.Unit_Dimension.T: -2
}

# label
B_r = B["r"]
B_r.position = [0,0,0]
B_t = B["t"]
B_t.position = [0,0,0]
B_z = B["z"]
B_z.position = [0,0,0]

dataset = io.Dataset(Br_data.dtype,Br_data.shape)
B_r.reset_dataset(dataset)
B_t.reset_dataset(dataset)
B_z.reset_dataset(dataset)

B_r.store_chunk(Br_data)
B_t.make_constant(0.0)
B_z.store_chunk(Bz_data)

# set meta information
E = it.meshes["E"]
E.grid_spacing = np.array([0.025, 0.125])
E.grid_global_offset = [0.0, -0.375]
E.axis_labels = ['r', 'z']
E.geometry = io.Geometry.thetaMode
E.geometry_parameters = "m=" + str(num_nodes) + ";imag=+"
E.unit_dimension = {
    io.Unit_Dimension.M:  1,
    io.Unit_Dimension.L:  1,
    io.Unit_Dimension.I: -1,
    io.Unit_Dimension.T: -3
}

# label
E_r = E["r"]
E_r.position = [0,0,0]
E_t = E["t"]
E_t.position = [0,0,0]
E_z = E["z"]
E_z.position = [0,0,0]

dataset = io.Dataset(Br_data.dtype,Br_data.shape)
E_r.reset_dataset(dataset)
E_t.reset_dataset(dataset)
E_z.reset_dataset(dataset)

E_r.make_constant(0.0)
E_t.make_constant(0.0)
E_z.make_constant(0.0)

series.flush()

del series
