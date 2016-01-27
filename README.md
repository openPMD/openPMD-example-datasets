# openPMD example datasets

These are example of [openPMD](http://www.openpmd.org/#/start) datasets, in three different geometries:
- 2D Cartesian
- 3D Cartesian
- Cylindrical with azimuthal decomposition ("thetaMode")

In order to obtain these datasets:
- Clone this repository
```
git clone https://github.com/openPMD/openPMD-example-datasets.git
```
- Uncrompress the files
```
cd openPMD-example-datasets
tar -zxvf example-2d.tar.gz
tar -zxvf example-3d.tar.gz
tar -zxvf example-thetaMode.tar.gz
```

Note: The datasets were produced with the Particle-In-Cell code
[Warp](https://bitbucket.org/berkeleylab/warp), from the scripts in
`scripts/`. The resolution is intentionally very low, so as to produce
data of manageable size.
