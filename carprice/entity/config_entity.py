import os, sys
from datetime import datetime
from carprice.exception import CarpriceException

FILE_NAME = "Car_details.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"

class TrainigPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}")
        except Exception as e:
            raise CarpriceException(e, sys)
class DataInjestionConfig:
    def __init__(self,training_pipeline_config: TrainigPipelineConfig):
        try:
            self.database_name = "Cars"
            self.collection_name = "Cars Database"
            self.data_injestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_injestion")
            self.feature_score_file_path = os.path.join(self.data_injestion_dir,"feature store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_injestion_dir,"feature store",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_injestion_dir,"feature store",TEST_FILE_NAME)
        except Exception as e:
            raise CarpriceException(e, sys)
    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise CarpriceException(e, sys)

class DataValidationConfig:
    pass