import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import numpy as np
from omegaconf import OmegaConf
import mlflow
import json
import os
import subprocess
import sys


def load_data(input_file):
    df = pd.read_csv(input_file)

    X = df[iris.feature_names]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=11
    )
    return X_train, X_test, y_train, y_test


def train_svc(X_train, X_test, y_train, y_test, hyperparams):
    with mlflow.start_run(run_name="svc"):
        param_dist = {
            "C": np.logspace(hyperparams.C.min, hyperparams.C.max, hyperparams.C.num),
            "gamma": np.logspace(
                hyperparams.gamma.min, hyperparams.gamma.max, hyperparams.gamma.num
            ),
        }

        svc = SVC()

        random_search = RandomizedSearchCV(
            estimator=svc,
            param_distributions=param_dist,
            n_iter=10,
            cv=5,
            scoring="accuracy",
            random_state=11,
            n_jobs=-1,
        )

        random_search.fit(X_train, y_train)

        mlflow.log_metric("gamma", random_search.best_params_.get("gamma"))
        mlflow.log_metric("C", random_search.best_params_.get("C"))

        id = mlflow.active_run().info.run_id

        svc = SVC(**random_search.best_params_).fit(X_train, y_train)
        y_pred = svc.predict(X_test)
        report = classification_report(
            y_test,
            y_pred,
            target_names=np.array(["Iris-setosa", "Iris-versicolor", "Iris-virginica"]),
            output_dict=True,
        )

        script_dir = os.path.dirname(os.path.abspath(__file__))
        report_path = os.path.join(script_dir, '../../data/experiments', id, 'report.json')
        os.makedirs(os.path.dirname(report_path), exist_ok=True)
        with open(report_path, "w") as f:
            json.dump(report, f)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        upload_script_path = os.path.join(script_dir, 'shell', 'upload_data.sh')
        subprocess.run([upload_script_path, id, "report.json"])

        model_data = {
            "gamma": random_search.best_params_["gamma"],
            "C": random_search.best_params_["C"],
        }
        script_dir = os.path.dirname(os.path.abspath(__file__))
        report_path = os.path.join(script_dir, '../../data/experiments', id, 'model.json')
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        with open(model_path, "w") as f:
            json.dump(model_data, f)
        script_dir = os.path.dirname(os.path.abspath(__file__))
        upload_script_path = os.path.join(script_dir, 'shell', 'upload_data.sh')
        subprocess.run([upload_script_path, id, "model.json"])


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: python clean_cpu_data.py <input_path> <params_path>"
        )
        sys.exit(1)

    input_file = sys.argv[1]
    params_file = sys.argv[2]

    X_train, X_test, y_train, y_test = load_data(input_file)

    conf = OmegaConf.load(params_file)
    hyperparams = conf.model.svc_random_search

    mlflow.set_tracking_uri("http://localhost:5000")
    try:
        mlflow.create_experiment(
            "iris-experiment", artifact_location="s3://ccds_bucket"
        )
    except mlflow.MlflowException as e:
        print(e)
    mlflow.set_experiment("iris-experiment")

    train_svc(X_train, X_test, y_train, y_test, hyperparams)
