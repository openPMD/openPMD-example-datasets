# openPMD example datasets

This repository contains examples of [openPMD](http://www.openpmd.org/#/start) datasets, in three different geometries:
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
...
```

# How were these files created?

## Files created with the Particle-In-Cell code Warp

The files `example-2d.tar.gz`, `example-3d.tar.gz` and `example-thetaMode.tar.gz` were produced with the Particle-In-Cell code
[Warp](https://bitbucket.org/berkeleylab/warp). The resolution is intentionally very low, so as to produce data of manageable size.

The scripts that were used in order to produce these openPMD files from Warp can be found in the directory `scripts/warp`.

## Examples created with the finite-element code FEMM

The files `example-femm-3d.h5` and `example-femm-thetaMode.h5` were produced using the finite-element code [FEMM](https://www.femm.info/wiki/HomePage).

The scripts that were used in order to produce these openPMD files can be found in the directory `scripts/femm`.

## Examples created with the Particle-In-Cell code PIConGPU

The files `legacy_datasets.tar.gz` were produced with the Particle-In-Cell code [PIConGPU](https://picongpu.readthedocs.io).
