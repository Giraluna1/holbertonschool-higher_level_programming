#!/bin/bash
# Display only the status code of the response
curl -o /dev/null -s -w "%{http_code}" $1
