#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"
  exec python3 /app/flaskweb.py
else
  echo "Running Production Server"
  exec python3 /app/flaskweb.py 
             
fi
