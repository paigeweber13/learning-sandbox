#!/bin/bash
# requires lm-sensors to be installed and configured by running 
# `sensors-detect`
while sleep 1 ; do
  sensors | grep CPUTIN >> ./data/cpu-$(date +"%Y-%m-%d_%H%M").log
done

