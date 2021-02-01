#!/bin/bash
# requires nvidia-smi to be installed
nvidia-smi dmon >> ./data/gpu-$(date +"%Y-%m-%d_%H%M").log

