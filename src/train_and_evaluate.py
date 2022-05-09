import os
import argparse
import pandas as pd
import joblib
import json
import numpy as np
from urllib.parse import urlparse
from sklearn.linear_model import ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
from get_data import read_params
import mlflow


def eval_matrics(actual,prediction):
    mse=mean_squared_error(actual,prediction)
    rmse=np.sqrt(mse)
    r2=r2_score(actual,prediction)
    return (mse,rmse,r2)


def train_and_evaluate(config_path):
    config=read_params(config_path)
    test_data_path=config["split_data"]["test_path"]
    train_data_path=config["split_data"]["train_path"]
    random_state=config["base"]["random_state"]
    model_dir=config["model_dir"]

    alpha=config["estimator"]["ElasticNet"]["params"]["alphas"]
    l1_ratio=config["estimator"]["ElasticNet"]["params"]["l1_ratio"]

    target=config["base"]["target_col"]

    train=pd.read_csv(train_data_path,sep=",")
    test=pd.read_csv(test_data_path,sep=",")

    train_x=train.drop(target,axis=1)
    test_x=test.drop(target,axis=1)

    train_y=train[target]
    test_y=test[target]

################ MLFLOW RUN ################### 

    mlflow_config=config["mlflow_config"]
    remote_server_uri=mlflow_config["remote_server_uri"]

    mlflow.set_tracking_uri(remote_server_uri)
    mlflow.set_experiment(mlflow_config["experiment_name"])   


    with mlflow.start_run(run_name=mlflow_config["run_name"]) as mlops_run:
        lr=ElasticNet(alpha=alpha,
                    l1_ratio=l1_ratio,
                    random_state=random_state)
        lr.fit(train_x,train_y)
        predicted_qualities=lr.predict(test_x)
        (mse,rmse,r2)=eval_matrics(test_y,predicted_qualities)

        mlflow.log_param("alpha",alpha)
        mlflow.log_param("l1_ratio",l1_ratio)
        mlflow.log_metric("mse",mse)
        mlflow.log_metric("rmse",rmse)
        mlflow.log_metric("r2",r2)

        tracking_url_type_sore=urlparse(mlflow.get_artifact_uri()).scheme

        if tracking_url_type_sore != "file":
            mlflow.sklearn.log_model(lr,
                                    "model",
                                    registered_model_name=mlflow_config["registered_model_name"])

        else:
            mlflow.sklearn.load_model(lr,"model")



        # print(f"value of mse:{mse} ,rmse:{rmse},r2:{r2}")

        # param_file=config["reports"]["params"]
        # score_file=config["reports"]["scores"]
        
        # with open(score_file,"w") as f:
        #     score={
        #         "mse":mse,
        #         "rmse":rmse,
        #         "r2":r2
        #     }
        #     json.dump(score, f, indent=4)
        
        # with open(param_file,"w") as f:
        #     params={
        #         "alpha":alpha,
        #         "l1_ratio":l1_ratio
        #     }
        #     json.dump(params, f, indent=4)

        # os.makedirs(model_dir, exist_ok=True)
        # model_path = os.path.join(model_dir, "model.joblib")

        # joblib.dump(lr, model_path)



if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)