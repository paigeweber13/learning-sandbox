import argparse
import datetime
import os
import pkgutil
import sys

from pathlib import Path
from importlib import import_module

import gym
from gym import wrappers, logger

# expects file containing agent to have name foo_bar.py and class inside that
# file to be named FooBar
def import_recursive(root_dir: str, package: str):
    imported_module = None
    for dir_info in os.walk(root_dir):
        if 'results' not in dir_info[0]:
            for (_, name, _) in pkgutil.iter_modules([Path(dir_info[0])]):
                if package in name:
                    name = '.' + name
                    thing_to_import = dir_info[0][2:].replace('/', '.')
                    imported_module = import_module(name, thing_to_import)
                    break

    print('imported module:', imported_module)
    class_name = ''
    for word in package.split('_'):
        class_name += word.capitalize()

    for part_of_package in dir(imported_module):
        if class_name in part_of_package:
            # found the class! Returning...
            return getattr(imported_module, part_of_package)


def main():
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('-e', '--env_id', nargs='?', default='CartPole-v0', help='Select the environment to run')
    parser.add_argument('-c', '--episode_count', nargs='?', default='100', help='Specify the number of episodes to run')
    parser.add_argument('-a', '--agent', nargs='?', default='random_agent', help='Specify the agent to use')
    args = parser.parse_args()

    logger.set_level(logger.INFO)

    env = gym.make(args.env_id)

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H%M%S')
    outdir = './results/' + args.agent + '/' + args.env_id + '/' + timestamp
    # if you want outdir to be cleared every run, make force=True
    env = wrappers.Monitor(env, directory=outdir, force=False)
    env.seed(0)

    input_class = import_recursive('.', args.agent)
    agent = input_class(env.action_space)

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
    main()
