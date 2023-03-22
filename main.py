from carprice.logger import logging
from carprice.exception import CarpriceException
import os, sys
from carprice.utils import get_collection_as_dataframe

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
        get_collection_as_dataframe(database_name='Cars',collection_name='Cars Database')
    except Exception as e:
        print(e)
