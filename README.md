# Particle_Swarm_Algo

[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sandialabs/sibl#license)


[![codecov](https://codecov.io/gh/tuckluck/Assignment2/graph/badge.svg?token=TKF4CLV1G5)](https://codecov.io/gh/tuckluck/Particle_Swarm_Algo)
[![tests](https://github.com/tuckluck/Assignment2/actions/workflows/testsDS.yml/badge.svg)](https://github.com/tuckluck/Particle_Swarm_Algo/actions)



Welcome to the Particle Swarm Repo. In this repo I have written a basic particle swarm algorithm and explored a complex multi-dimensional problem. The tutorial will walk through the basics of how a particle swarm algorithm works and it will also discuss how to adjust the algorithm social, inertial, and cognitive variables which can be valuable for certain problems. Enjoy!


This project made use of several skills learned in ME 700. First, using github for opensource programing. Second, code documentation and coverage. Lastly, understanding and exploring optimization algorithms. 

To install this package, please begin by setting up a conda environment (mamba also works):
```bash
conda create --name PSO-env python=3.12
```
Once the environment has been created, activate it:

```bash
conda activate PSO-env
```
Double check that python is version 3.12 in the environment:
```bash
python --version
```
Ensure that pip is using the most up to date version of setuptools:
```bash
pip install --upgrade pip setuptools wheel
```
Create an editable install of the bisection method code (note: you must be in the correct directory):
```bash
pip install -e .
```
Test that the code is working with pytest:
```bash
pytest -v --cov=particleswarm --cov-report term-missing
```
Code coverage should be 100%. Now you are prepared to write your own code based on this method and/or run the tutorial. 


If you would like the open `ParticleSwarm_tutorial.ipynb` located in the `tutorials` folder as a Jupyter notebook in the browser, you might need to install Jupyter notebook in your conda environment as well:
```bash
pip install jupyter
```
```bash
cd tutorials/
```
```bash
jupyter notebook ParticleSwarm_tutorial.ipynb
```
---
