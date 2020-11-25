#!/bin/bash

NUM_PROCS=5

for i in $(seq $NUM_PROCS); do
	terminator -e "cd /home/riley/code/tmp && /home/riley/.pyenv/shims/python bestbuy-test.py; read" &
done
