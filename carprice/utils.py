import pandas as pd
import numpy as np
import os, sys
from carprice.exception import CarpriceException
from carprice.config import mongo_client
from carprice.logger import logging

def get_collection_as_dataframe(database_name:str,collection_name:str):
    try:
        logging.info(f"Reading data from database : {database_name} and collection: {collection_name}")
        df = pd.DataFrame(mongo_client[database_name][collection_name].find())
        logging.info(f"find columns : {df.columns}")
        if "_df" in df.columns:
            logging.info("Dropping columns: _id")
            df = df.drop("_id",axis=1)
        logging.info(f"Rows and Columns in df : {df.shape}")
        return df    
        
    except Exception as e:
        raise CarpriceException(e, sys) 