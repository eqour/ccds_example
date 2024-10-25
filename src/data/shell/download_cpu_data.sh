#!/bin/bash
s3cmd -c .s3cmd get s3://ccds-bucket/cpu_dataset.csv data/raw/cpu_dataset.csv
