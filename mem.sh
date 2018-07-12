#!/bin/bash

free -m | grep -e "^Mem:" | awk '{print $2}'