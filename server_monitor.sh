#!/bin/bash

while true
do
  ./server & wait
  sleep 2
  echo "Restarting Script"
done

