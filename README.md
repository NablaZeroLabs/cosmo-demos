# cosmo-demos | SPICE-Enhanced Cosmographia Tutorials
## Nabla Zero Labs, 2021

This is `cosmo-demos`, a software utility for creating advanced astrodynamics visualizations using NASA's SPICE-Enhanced Cosmographia.

![Europa Clipper arriving at Jupiter](docs/europa_clipper_arriving_jupiter.png)
![Earth rocket launch](docs/earth_rocket_launch.png)

## Dependencies
* [SPICE-Enhanced Cosmographia 4.0](https://naif.jpl.nasa.gov/naif/cosmographia.html)

# Cosmographia
SPICE-enhanced Cosmographia is an open source visualization tool used to
produce 3D animations of planets (3D models and orbits), stars, and spacecraft
(trajectories, 3D models, sensor FOVs, etc.). This repository interacts with
Cosmographia via Python scripts, SPICE kernels, JSON catalogs, and CAD models.

# Getting Started
This repository is accompanied by YouTube videos that explain how to run the existing scenes and create scenes from scratch.
* [Cosmographia Tutorials Video Series](https://www.youtube.com/playlist?list=PLinlYN8Y2w8dF_FI2baI5YXM476_7kekz)

## Setting Environment Variables
`cosmo-demos` calls Cosmographia via bash scripts that point to the Cosmographia executable, JSON catalogs, SPICE kernels, and Python scripts. In order to use this repository, one must set 2 environment variables: `COSMOGRAPHIA` and `COSMO_DEMOS`.

This is done via the `export` command, which for convenience can be placed in a .bash_profile or .bashrc file. For example:

```sh
$ export COSMOGRAPHIA=/Users/alfonso/cosmographia-4.0/Cosmographia.app/Contents/MacOS/Cosmographia
$ export COSMO_DEMOS=/Users/alfonso/pub/cosmo-demos/scenes
```

* [Video explaining how to set these environment variables](https://youtu.be/OU6bOjYOVus)

Once the environment variables are set, one can call any bash script that corresponds to a scene in this repository. For example (from the base of the repository):

```sh
$ ./scenes/ct003_py_json_spice/run_sun_synchronous_orbit.sh
```
