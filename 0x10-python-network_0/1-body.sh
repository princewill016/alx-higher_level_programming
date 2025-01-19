#!/bin/bash
# Script that displays body of 200 status code response
curl -s -w "%{http_code}" "$1" | grep -A 99999 "^200" 2>/dev/null
