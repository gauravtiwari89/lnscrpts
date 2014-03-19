#!/bin/zsh
# takes the names of the input and the output files as an argument
python pathslogcrawler.py $1 | sort > $2
