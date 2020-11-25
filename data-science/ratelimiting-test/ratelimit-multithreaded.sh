#!/bin/bash

NUM_PROCS=100

for i in $(seq $NUM_PROCS); do
	terminator -e "cd /home/riley/code/learning-sandbox/data-science/ratelimiting-test && /home/riley/.pyenv/shims/python ratelimit-test.py; read" &
done
