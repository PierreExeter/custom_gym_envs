# Custom Gym Environments
Some custom Gym environments for reinforcement learning.

## Installation and environment registration

```bash
git clone https://github.com/PierreExeter/custom_gym_envs.git
conda env create -f environment.yml
conda activate gym_envs
pip install -e .   # local install the Gym environmnents
```

## Test the environments

Execute scripts in the test_envs folder. For example:

```
python test_envs/4_test_reacher2D.py
```

## Environments description

| Name          | Action space                               | Observation space                                                     | Rewards                              |
| balancebot-v0 | Discrete(9) - define wheel target velocity | Box(3,) - [cube orientation , cube angular velocity , wheel velocity] | 0.1 - abs(self.vt - self.vd) * 0.005 |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |
| ---------| -------------------| -----------------------| ------------- |


## Requirements

conda 4.8.3
