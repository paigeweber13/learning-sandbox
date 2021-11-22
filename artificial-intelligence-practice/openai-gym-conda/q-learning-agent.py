import numpy as np


class QLearningAgent(object):
    def __init__(self, env, num_buckets):
        """
        :param env: environment variable provided by `gym.make`
        :param num_buckets: ndarray with the same shape as
        `env.observation_space`. This provides the number of buckets used to
        discretize the observation space.
        """
        x = env.action_space.n
        y = 1
        self.bucket_sizes = (env.observation_space.high -
                             env.observation_space.low) / num_buckets

        for n in num_buckets:
            y *= n

        self.q_table = np.ndarray(x, y)
