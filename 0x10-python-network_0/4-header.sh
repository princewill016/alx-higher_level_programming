#!/bin/bash
# Script that sends GET request with custom header
curl -s -H "X-School-User-Id: 98" "$1"
