# ccds_example

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

CookieCutter example project

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         ccds_example and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── ccds_example   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes ccds_example a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

## Установка окружения

Для запуска необходим Python версии 3.8 с poetry

Для установки зависимостей перейдите в корень проекта в выполните следующую команду:

```bash
poetry install
```

Перед инициализацией get pre commit hooks проверьте актуальность версий для хуков в файле конфигурации .pre-commit-config.yaml и при необходимости обновите их.

Для инициализации git pre commit hooks необходимо выполнить следующую команду:
```bash
pre-commit install
```

## Подготовка окружения для работы с S3

Для успешного выполнения пайплайна необходимо запустить S3 с bucket ccds-bucket. В bucket должен находиться объект iris.csv. Его можно загрузить из файла iris.csv в корне проекта.

Перед запуском скриптов заполните необходимые поля в файле конфигурации s3cmd для доступа к S3 в файле .s3cmd. Создайте файл .env из файла .env.example и заполните необходимые переменные.

Установите права доступа для скриптов:
```bash
chmod +x src/data/shell/*.sh run_pipeline.sh install_s3cmd.sh
```

Для работы с S3 установите s3cmd через shell скрипт:
```bash
./install_s3cmd.sh
```

## Запуск контейнера с MlFlow

```bash
docker-compose up -d
```

## Запуск пайплайна с S3

Запустите пайплайн работы с S3:
```bash
./run_pipeline.sh
```
