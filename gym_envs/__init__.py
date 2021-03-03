from gym.envs.registration import register

#*********************************************

register(
    id='foo-v0',
    entry_point='gym_envs.0_minimal_working_example.foo_env:FooEnv',
)

#*********************************************

register(
    id='tictac-v0',
    entry_point='gym_envs.1_tictactoe.tictac_env:TicTacEnv',
)

#*********************************************

register(
    id='balancebot-v0',
    entry_point='gym_envs.2_balance_bot.balancebot_env:BalancebotEnv',
    kwargs={'render': True}
)

register(
    id='balancebot-noise-v0',
    entry_point='gym_envs.2_balance_bot.balancebot_env_noise:BalancebotEnvNoise',
)

#*********************************************

register(
    id='particle-v0',
    entry_point='gym_envs.3_particle_goal_oriented.continuous_goal_oriented_particle:ParticleEnv',
    max_episode_steps=250,
	reward_threshold=1,)

#*********************************************

register(
	id='Reacher1Dof-v0',
	entry_point='gym_envs.reacher2D.envs.reacher_env:ReacherBulletEnv1',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher2Dof-v0',
	entry_point='gym_envs.reacher2D.envs.reacher_env:ReacherBulletEnv2',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher3Dof-v0',
	entry_point='gym_envs.reacher2D.envs.reacher_env:ReacherBulletEnv3',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher4Dof-v0',
	entry_point='gym_envs.reacher2D.envs.reacher_env:ReacherBulletEnv4',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher5Dof-v0',
	entry_point='gym_envs.reacher2D.envs.reacher_env:ReacherBulletEnv5',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher6Dof-v0',
	entry_point='gym_envs.reacher2D.envs.reacher_env:ReacherBulletEnv6',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

#*********************************************

register(
	id='Reacher1Dof-v1',
	entry_point='gym_envs.reacher2D.goal_envs.reacher_env:ReacherBulletEnv1',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher2Dof-v1',
	entry_point='gym_envs.reacher2D.goal_envs.reacher_env:ReacherBulletEnv2',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher3Dof-v1',
	entry_point='gym_envs.reacher2D.goal_envs.reacher_env:ReacherBulletEnv3',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher4Dof-v1',
	entry_point='gym_envs.reacher2D.goal_envs.reacher_env:ReacherBulletEnv4',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher5Dof-v1',
	entry_point='gym_envs.reacher2D.goal_envs.reacher_env:ReacherBulletEnv5',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

register(
	id='Reacher6Dof-v1',
	entry_point='gym_envs.reacher2D.goal_envs.reacher_env:ReacherBulletEnv6',
	max_episode_steps=150,
	reward_threshold=18.0,
	)

#*********************************************

# environment for both the physical arm and the Pybullet simulation
register(id='widowx_reacher-v0',
         entry_point='gym_envs.5_widowx.v0_widowx_original:WidowxEnv',
         max_episode_steps=100
         )

# environment for the physical arm only         
register(id='widowx_reacher-v1',
         entry_point='gym_envs.5_widowx.v1_widowx_physical_only:WidowxEnv',
         max_episode_steps=100
         )

# environment for the physical arm only + no start_rospy method 
register(id='widowx_reacher-v2',
         entry_point='gym_envs.5_widowx.v2_widowx_physical_env_fixedGoal:WidowxEnv',
         max_episode_steps=100
         )

# FOR SOME STRANGE REASON, I CAN'T SPECIFY max_episode_steps for GoalEnv (solved)
# environment for the physical arm only + no start_rospy method + goal oriented
register(id='widowx_reacher-v3',
         entry_point='gym_envs.5_widowx.v3_widowx_physical_goalEnv_fixedGoal:WidowxEnv',
         max_episode_steps=100
         )

# environment for the Pybullet simulation only. ROS install not required
register(id='widowx_reacher-v4',
         entry_point='gym_envs.5_widowx.v4_widowx_pybullet_only:WidowxEnv',
         max_episode_steps=100
         )

# environment for the Pybullet simulation + no start_sim required + fixed goal
register(id='widowx_reacher-v5',
         entry_point='gym_envs.5_widowx.v5_widowx_pybullet_env_fixedGoal:WidowxEnv',
         max_episode_steps=100
         )

# FOR SOME STRANGE REASON, I CAN'T SPECIFY max_episode_steps for GoalEnv
# environment for the Pybullet simulation + no start_sim required + goal_oriented + fixed goal
register(id='widowx_reacher-v6',
         entry_point='gym_envs.5_widowx.v6_widowx_pybullet_goalEnv_fixedGoal:WidowxEnv',
         max_episode_steps=100
         )

# environment for the Pybullet simulation + no start_sim required + random goal
register(id='widowx_reacher-v7',
         entry_point='gym_envs.5_widowx.v7_widowx_pybullet_env_randomGoal:WidowxEnv',
         max_episode_steps=100
         )

# FOR SOME STRANGE REASON, I CAN'T SPECIFY max_episode_steps for GoalEnv (solved)
# environment for the Pybullet simulation + no start_sim required + goal_oriented + random goal
register(id='widowx_reacher-v8',
         entry_point='gym_envs.5_widowx.v8_widowx_pybullet_goalEnv_randomGoal:WidowxEnv',
         max_episode_steps=100
         )

# environment for the physical arm only + no start_rospy method + random goal
register(id='widowx_reacher-v12',
         entry_point='gym_envs.5_widowx.v12_widowx_physical_env_randomGoal:WidowxEnv',
         max_episode_steps=100
         )
         
# environment for the physical arm only + no start_rospy method + goal environment + random goal
register(id='widowx_reacher-v13',
         entry_point='gym_envs.5_widowx.v13_widowx_physical_goalEnv_randomGoal:WidowxEnv',
         max_episode_steps=100
         )

#*********************************************

# test gym.GoalEnv
register(id='my_goal_env-v0',
         entry_point='gym_envs.6_minimal_goalEnv.my_goal_env:MyGoalEnv'
         )

#*********************************************

register(
    id='ReachingJaco-v1',
    entry_point='gym_envs.7_reaching_jaco.reaching:ReachingEnv',
    max_episode_steps=100,
)

#*********************************************


# environment using the ROS Topics to move the arm in Gazebo
register(
    id='JacoReachGazebo-v0',
    entry_point='gym_envs.reaching_jaco_ROS.jaco_gazebo_topic_env:JacoEnv',
    max_episode_steps=50
)

# environment using ROS Action client to move the arm in Gazebo
register(
    id='JacoReachGazebo-v1',
    entry_point='gym_envs.reaching_jaco_ROS.jaco_gazebo_action_env:JacoEnv',
    max_episode_steps=50
)

# environment using ROS Action client to move the arm in Gazebo + fixed goal + 1 joint moving only
register(
    id='JacoReachGazebo-v2',
    entry_point='gym_envs.reaching_jaco_ROS.jaco_gazebo_actionlib_fixedGoal_1jointOnly:JacoEnv',
    max_episode_steps=50
)

# environment to move the real arm
register(
    id='JacoReachReal-v0',
    entry_point='gym_envs.reaching_jaco_ROS.jaco_real_env:JacoEnv',
    max_episode_steps=50
)



register(
    id='KukaButtonGymEnv-v0',
    entry_point='gym_envs.kuka_gym.kuka_button_gym_env:KukaButtonGymEnv',
    max_episode_steps=None,
    reward_threshold=None
    )


register(
    id='Kuka2ButtonGymEnv-v0',
    entry_point='gym_envs.kuka_gym.kuka_2button_gym_env:Kuka2ButtonGymEnv',
    max_episode_steps=None,
    reward_threshold=None
    )

register(
    id='KukaMovingButtonGymEnv-v0',
    entry_point='gym_envs.kuka_gym.kuka_moving_button_gym_env:KukaMovingButtonGymEnv',
    max_episode_steps=None,
    reward_threshold=None
    )

register(
    id='KukaRandButtonGymEnv-v0',
    entry_point='gym_envs.kuka_gym.kuka_rand_button_gym_env:KukaRandButtonGymEnv',
    max_episode_steps=None,
    reward_threshold=None
    )

