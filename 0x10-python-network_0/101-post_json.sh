#!/bin/bash
# POTS to JSON file
curl -X POST -H "Content-Type: application/json" -d @$2 $1
