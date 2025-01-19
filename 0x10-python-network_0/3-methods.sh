#!/bin/bash
# Script that displays accepted HTTP methods
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
