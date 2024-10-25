#!/bin/bash
s3cmd -c .s3cmd put data/processed/cpu_dataset.csv s3://ccds-bucket/cpu_dataset.csv
