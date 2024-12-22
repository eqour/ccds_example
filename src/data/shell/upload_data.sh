#!/bin/bash

EXPERIMENT_ID=$1
FILE_NAME=$2

s3cmd -c .s3cmd put data/experiments/${EXPERIMENT_ID}/${FILE_NAME} s3://ccds-bucket/experiments/${EXPERIMENT_ID}/${FILE_NAME}
