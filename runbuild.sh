#!/bin/sh

if [ -z "$1" ]
then
  scale=""
else
  scale="--scale web=$1"
fi

echo "[runbuild.sh] scaling \`web\` to $1 instances"

docker-compose up --build $scale
