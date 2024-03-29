`mirror.FEM` can be loaded by the FEMM software
(https://www.femm.info/wiki/HomePage)
to produce an example of magnetic mirror B field,
as shown in `field.png`.

`LuaScript_3d.lua` and `LuaScript_rz.lua` are two Lua scripts
used to output the B field data from FEMM
to txt files (`B*_3d.txt` and `B*_rz.txt`).

`openpmd_create_3d.py` and `openpmd_create_rz.py`
are python scripts to convert `B*_3d.txt` and `B*_rz.txt`
to openPMD data files, named `example-femm-3d.h5` and
`example-femm-thetaMode.h5`, respectively.

`example-femm-3d.h5` is used in WarpX example `LoadExternalField3D`;
`example-femm-thetaMode.h5` is used in WarpX example `LoadExternalFieldRZ`.

The WarpX input files of these two example tests are in
`Examples/Tests/LoadExternalField/`.
