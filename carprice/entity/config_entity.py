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
        

class DataIngestionConfig:
    def __init__(self,training_pipeline_config: TrainigPipelineConfig):
        try:
            self.database_name = "Cars"
            self.collection_name = "Cars Database"
            self.data_injestion_dir = os.path.join(training_pipeline_config.artifact_dir,"data_injestion")
            self.feature_store_file_path = os.path.join(self.data_injestion_dir,"feature store",FILE_NAME)
            self.train_file_path = os.path.join(self.data_injestion_dir,"dataset",TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_injestion_dir,"dataset",TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise CarpriceException(e, sys)
    def to_dict(self)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise CarpriceException(e, sys)

class DataValidationConfig:
    def __init__(self, training_pipeline_config:TrainigPipelineConfig):
        self.data_validation_dir = os.path.join(training_pipeline_config.artifact_dir,"data_validation")
        self.report_file_path = os.path.join(self.data_validation_dir,"report.yaml")
        self.missing_threshold:float = 0.2
        self.base_file_path = os.path.join("Car_details.csv")