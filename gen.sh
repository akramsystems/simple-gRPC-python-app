#!/bin/bash

CURDIR=`pwd`

python -m grpc_tools.protoc \
    -I ${CURDIR} \
    --python_out=. \
    --grpc_python_out=. \
    rides.proto