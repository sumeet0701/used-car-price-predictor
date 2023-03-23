from carprice.entity import config_entity
import pandas as pd
import numpy as np
import os, sys
from carprice.entity import artifact_entity
from carprice.exception import CarpriceException
from carprice import utils
from carprice.logger import logging
from sklearn.model_selection import train_test_split

class Datainjestion:
    def __init__(self, data_injestion_config = config_entity.DataInjestionConfig):
        try:
            self.data_injestion_config = data_injestion_config
        except Exception as e:
            raise CarpriceException(e, sys)
        
    def initiate_data_injestion(self)->artifact_entity.DataInjestinArtifact:
        try:
            logging.info(f"Export collection data as dataframe")
            df:pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_injestion_config.database_name,
                collection_name=self.data_injestion_config.collection_name
            )
            logging.info(f"store data for further store")
            df.replace(to_replace='na', value=np.NaN,inplace=True)
            logging.info(f"create feature store folder if not available")

            feature_store_dir = os.path.dirname(self.data_injestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir,exist_ok=True)
            logging.info("save folder to feature store folder ")

            df.to_csv(path_or_buf=self.data_injestion_config.feature_store_file_path,index=False,header=True)

            logging.info(f"spliting data into train and test")
            train_df, test_df = train_test_split(df, test_size=self.data_injestion_config.test_size, random_state=1)
            
            logging.info("Create dataset dir folder if not excist")
            dataset_dir = os.path.dirname(self.data_injestion_config.train_file_path)
            os.makedirs(dataset_dir,exist_ok=True) 

            logging.info("save dataset to feature store")
            train_df.to_csv(path_or_buf=self.data_injestion_config.train_file_path,index=False, header=True)
            test_df.to_csv(path_or_buf=self.data_injestion_config.test_file_path,index=False, header=True)

            #prepare artifact folder
            data_injestion_artifact = artifact_entity.DataInjestinArtifact(
                feature_store_file_path = self.data_injestion_config.feature_store_file_path,
                train_file_path = self.data_injestion_config.train_file_path,
                test_file_path = self.data_injestion_config.test_file_path
            )

        except Exception as e:
            raise CarpriceException(e, sys)
        

        
# from Insurance import utils
# from Insurance.entity import config_entity
# from Insurance.entity import artifact_entity
# from Insurance.exception import InsuranceException
# from Insurance.logger import logging
# import os,sys
# import pandas as pd 
# import numpy as np
# from sklearn.model_selection import train_test_split

# class DataIngestion:
#     def __init__(self,data_ingestion_config:config_entity.DataInjestionConfig ):
#         try:
#             self.data_ingestion_config = data_ingestion_config
#         except Exception as e:
#             raise CarpriceException(e, sys)

#     def initiate_data_ingestion(self)->artifact_entity.DataInjestinArtifact:
#         try:
#             logging.info(f"Exporting collection data as pandas dataframe")
#             #Exporting collection data as pandas dataframe
#             df:pd.DataFrame  = utils.get_collection_as_dataframe(
#                 database_name=self.data_ingestion_config.database_name, 
#                 collection_name=self.data_ingestion_config.collection_name)

#             logging.info("Save data in feature store")

#             #replace na with Nan
#             df.replace(to_replace="na",value=np.NAN,inplace=True)

#             #Save data in feature store
#             logging.info("Create feature store folder if not available")
#             #Create feature store folder if not available
#             feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
#             os.makedirs(feature_store_dir,exist_ok=True)
#             logging.info("Save df to feature store folder")
#             #Save df to feature store folder
#             df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path,index=False,header=True)


#             logging.info("split dataset into train and test set")
#             #split dataset into train and test set
#             train_df,test_df = train_test_split(df,test_size=self.data_ingestion_config.test_size, random_state = 1)
            
#             logging.info("create dataset directory folder if not available")
#             #create dataset directory folder if not available
#             dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
#             os.makedirs(dataset_dir,exist_ok=True)

#             logging.info("Save df to feature store folder")
#             #Save df to feature store folder
#             train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path,index=False,header=True)
#             test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path,index=False,header=True)
            
#             #Prepare artifact

#             data_ingestion_artifact = artifact_entity.DataInjestinArtifact(
#                 feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
#                 train_file_path=self.data_ingestion_config.train_file_path, 
#                 test_file_path=self.data_ingestion_config.test_file_path)

#             logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
#             return data_ingestion_artifact

#         except Exception as e:
#             raise CarpriceException(error_message=e, error_detail=sys)



        