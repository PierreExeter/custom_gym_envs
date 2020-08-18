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

| Name     | Action space       | Observation space      | Rewards       |
| ---------| -------------------| -----------------------| ------------- |
| balancebot-v0 | Discrete(9): define wheel target velocity | Box(3,): [cube orientation , cube angular velocity , wheel velocity] | 0.1 - abs(self.vt - self.vd) * 0.005 |
| particle-v0 | Box(2,): [force_x, force_y] | Dict("achieved_goal": [coord_x, coord_y], "desired_goal": [coord_x, coord_y], "observation": [pos_x, pos_y, vel_x, vel_y])   | -dist (dense) or (dist <= distance_threshold) (sparse) |
| Reacher2Dof-v0 | Box(2,): [0.05 * torque_1, 0.05 * torque_2] | Box(8,): [target_x, target_y, dist_to_target_x, dist_to_target_y, joint0_angle, joint0_vel, joint1_angle, joint1_vel | [change in dist to target, electricity_cost, stuck_joint_cost] |
| Reacher2Dof-v1 | Box(2,): [0.05 * torque_1, 0.05 * torque_2] | Dict("achieved_goal": [tip_x, tip_y], "desired_goal": [target_x, target_y], "observation": *same as above* ) | -dist_to_target |
| widowx_reacher-v5 | Box(6,): [angle_change_joint1, angle_change_joint2, angle_change_joint3, angle_change_joint4, angle_change_joint5, angle_change_joint6] | Box(9,): [target_x, target_y, target_z, joint_angle1, joint_angle2, joint_angle3, joint_angle4, joint_angle5, joint_angle6] | - dist ^ 2) |
| widowx_reacher-v7 | Box(6,): [angle_change_joint1, angle_change_joint2, angle_change_joint3, angle_change_joint4, angle_change_joint5, angle_change_joint6] | Dict("achieved_goal": [tip_x, tip_y, tip_z], "desired_goal": [target_x, target_y, target_z], "observation": *same as above* ) | - dist ^ 2) |
| ReachingJaco-v1 | Box(7,): [joint1_angle + 0.05 * action1, joint2_angle + 0.05 * action2, joint3_angle + 0.05 * action3, joint4_angle + 0.05 * action4, joint5_angle + 0.05 * action5, joint6_angle + 0.05 * action6, joint7_angle + 0.05 * action7]  | Box(17,): [gripper_x - torso_x, gripper_y - torso_y, gripper_z - torso_z, gripper_x - target_x, gripper_y - target_y, gripper_z - target_z, joint_angle1, joint_angle2, joint_angle3, joint_angle4, joint_angle5, joint_angle6, joint_angle7, gripper_orient_x, gripper_orient_y, , gripper_orient_w]  | -dist |



## Requirements

conda 4.8.3
