#!/bin/bash

grep -e "\[\^.*\]:" -h **/*.md | sed -r "s/^.*\]: (.*)/\1/g" | sort | uniq 
