#!/bin/bash
set -e

if [ "$ENV" = 'DEV' ]; then
  echo "Running Development Server"
  exec python3 /app/identidock.py
else
  echo "Running Production Server"
  exec python3 /app/identidock.py 
             
fi
