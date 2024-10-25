#!/bin/bash

# 1. Загрузка исходного файла из S3
bash src/data/shell/download_cpu_data.sh

# 2. Обработка данных с помощью Python скрипта
bash src/data/shell/process_cpu_data.sh

# 3. Загрузка обработанного файла обратно в S3
bash src/data/shell/upload_cpu_data.sh
