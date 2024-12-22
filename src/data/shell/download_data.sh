#!/bin/bash

FILE_NAME=$1

s3cmd -c .s3cmd get s3://ccds-bucket/${FILE_NAME} data/raw/${FILE_NAME}
