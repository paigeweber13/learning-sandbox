#!/bin/bash

NUM_PROCS=5

for i in $(seq $NUM_PROCS); do
	terminator -e "cd /home/riley/code/learning-sandbox/data-science/bestbuy-ratelimiting-test && /home/riley/.pyenv/shims/python bestbuy-test.py; read" &
done
