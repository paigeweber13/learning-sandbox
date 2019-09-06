import argparse
import datetime
import os
import pkgutil
import sys

from pathlib import Path
from importlib import import_module

import gym
from gym import wrappers, logger

from examples.agents import random_agent

def import_recursive(root_dir: str, package: str):
    for dir_info in os.walk(root_dir):
        if 'results' not in dir_info[0]:
            for (_, name, _) in pkgutil.iter_modules([Path(dir_info[0])]):
                if package in name:
                    package = dir_info[0][2:].replace('/', '.')
                    print('attempting import: import_module(' + name + ', ' + package +')')
                    imported_module = import_module(name, package)
                    print('imported module:', imported_module)
                    return
                # print(name)

    # for (_, name, _) in pkgutil.iter_modules([Path(__file__).parent]):
    # for (_, name, _) in pkgutil.iter_modules([os.path.dirname(__file__)]):
    #     print(name)

def main():
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('env_id', nargs='?', default='CartPole-v0', help='Select the environment to run')
    parser.add_argument('episode_count', nargs='?', default='100', help='Specify the number of episodes to run')
    parser.add_argument('agent', nargs='?', default='random_agent', help='Specify the agent to use')
    args = parser.parse_args()

    logger.set_level(logger.INFO)

    env = gym.make(args.env_id)

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    outdir = './results/' + args.agent + '/' + args.env_id + '/' + timestamp
    # if you want outdir to be cleared every run, make force=True
    env = wrappers.Monitor(env, directory=outdir, force=False)
    env.seed(0)
    # TODO: replace programatically
    agent = random_agent.RandomAgent(env.action_space)

    episode_count = int(args.episode_count)
    reward = 0
    done = False

    for _ in range(episode_count):
        ob = env.reset()
        while not done:
            action = agent.act(ob, reward, done)
            ob, reward, done, _ = env.step(action)
            # Note there's no env.render() here. But the environment still can open window and
            # render if asked by env.monitor: it calls env.render('rgb_array') to record video.
            # Video is not recorded every episode, see capped_cubic_video_schedule for details.

    # Close the env and write monitor result info to disk
    env.close()

if __name__ == '__main__':
    import_recursive('.', 'random_agent')
    # main()
