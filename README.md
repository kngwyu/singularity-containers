# Some random singularity containers definitions
Here I put some apptainer/singularity container definition files that I'm using or I used before.

CUDA contaienrs are based on [NVIDIA CUDA](https://catalog.ngc.nvidia.com/orgs/nvidia/containers/cuda) Docker containers.

## How to build
```bash
sudo singularity build [your container].sif [your container].def
```
You can also use [apptainer](https://apptainer.org/)[^1] instead of singularity.

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

- py38-cuda112-tf-dlc.def
  - Ubuntu 20.04, Cuda 11.2, CUDNN8.1
  - tensorflow and [deeplabcut](https://deeplabcut.github.io/DeepLabCut/)

- py38-cuda114-jax-brax.def
  - Ubuntu 20.04, Cuda 11.4, CUDNN8.2
  - jax
  - brax

- py38-simple.def
  - Based on Ubuntu 20.04
  - Contains some basic Python scientific stacks

- alpine-emacs.def
  - Based on Alpine Linux
  - Emacs and other utilities

- alpine-emacs.def
  - Based on [silex/emacs](https://hub.docker.com/r/silex/emacs)
  - Emacs and other utilities

[^1]: Successor of open source singularity, from which Singularity PRO is forked.
