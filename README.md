# Singularity Containers for RL/DeepRL research

## How to build
```bash
sudo singularity build [your container].sif [your container].def
```

## Current Containers
- py38-cuda112-jax-mujoco200.def
  - Based on [nvidia:cuda](https://ngc.nvidia.com/catalog/containers/nvidia:cuda)
  - Contains Jax and some other things

- py38-torch181-cuda111-mujoco200.sif
  - Based on Ubuntu 20.04
  - Default Python version is 3.8
  - Contains OpenAI gym, PyBullet, MuJoCo 2.0, and dm_control
  - Contains PyTorch 1.8.1 built for CUDA 11.1

- py38-simple.sif
  - Based on Ubuntu 20.04
  - Contains some basic Python scientific stacks
