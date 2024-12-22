#!/bin/bash

# 1. Загрузка исходного файла из S3
bash src/data/shell/download_data.sh iris.csv

# 2. Проведение эксперимента с помощью Python и MLFlow
python3 src/data/train_iris.py data/raw/iris.csv data/processed/cpu_dataset.csv iris-svc-parameters.yaml
