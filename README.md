# Singularity Containers for (mainly deep RL) research
Most of containers are based on [NVIDIA CUDA](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda) containers.

## How to build
```bash
sudo singularity build [your container].sif [your container].def
```
You can also use [apptainer](https://apptainer.org/) instead of singularity.

## Current Containers
- py310-cuda118-jax.def
  - Ubuntu 22.04, Cuda 11.8, CUDNN8.6
  - CUDA tools and compiler
  - jax

- py38-cuda116-jax.def
  - Ubuntu 20.04, Cuda 11.6, CUDNN8.2
  - CUDA CLI tools
  - jax

- py38-cuda116-jax.def
  - Ubuntu 20.04, Cuda 11.6, CUDNN8.2
  - CUDA CLI tools
  - jax

- py38-cuda114-jax-brax.def
  - Ubuntu 20.04, Cuda 11.4, CUDNN8.2
  - jax
  - brax

- py38-cuda112-jax-tf.def
  - Ubuntu 20.04, Cuda 11.2, CUDNN8.1
  - jax
  - tensorflow

- py38-cuda114-jax-brax.def
  - Ubuntu 20.04, Cuda 11.4, CUDNN8.2
  - jax
  - brax

- py38-simple.sif
  - Based on Ubuntu 20.04
  - Contains some basic Python scientific stacks
