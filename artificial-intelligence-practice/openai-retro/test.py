import os
import retro

os.system("python -m retro.import ./roms")

print('all available games:')
# list of all available envs is also here:
# https://github.com/openai/retro/tree/master/retro/data/stable
print(retro.data.list_games())

print('testing super mario bros env:')
env = retro.make(game='SuperMarioBros-Nes')
print(env)

