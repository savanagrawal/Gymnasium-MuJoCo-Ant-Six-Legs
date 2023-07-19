from gymnasium.envs.registration import register

register(
     id="gym_mujoco_ant_six_legs/AntSixLegs-v0",
     entry_point="gym_mujoco_ant_six_legs.envs:AntSixLegs",
     max_episode_steps=1000,
    reward_threshold=6000.0,
)
