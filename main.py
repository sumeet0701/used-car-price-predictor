from carprice.logger import logging
from carprice.exception import CarpriceException
import os, sys
from carprice.utils import get_collection_as_dataframe
from carprice.entity.config_entity import DataIngestionConfig
from carprice.entity import config_entity
from carprice.components.data_injestion import Dataingestion
from carprice.components.data_validation import DataValidation


# def test_logger_and_exception():
#     try:
#         logging.info("Starting point the test_logger_and_exception")
#         result = 3/0
#         print(result)
#         logging.info("Ending point the test_logger_and_exception")
#     except Exception as e:
#         logging.debug(str(e))
#         raise CarpriceException(e, sys)

if __name__ == "__main__":
    try:
        # test_logger_and_exception()
        # get_collection_as_dataframe(database_name='Cars',collection_name='Cars Database')
        training_pipeline_config = config_entity.TrainigPipelineConfig()
        data_injestion_config = config_entity.DataIngestionConfig(training_pipeline_config= training_pipeline_config)
        print(data_injestion_config.to_dict())

        data_injestion = Dataingestion(data_injestion_config=data_injestion_config)
        data_injestion_artifact = data_injestion.initiate_data_injestion()

        data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
        data_validation = DataValidation(data_validation_config=data_validation_config,
                                         data_ingestion_config=data_injestion_config,
                                         data_ingestion_artifact=data_injestion_artifact)
        data_validation_artifact = data_validation.initiate_data_validation()


    except Exception as e:
        print(e)
