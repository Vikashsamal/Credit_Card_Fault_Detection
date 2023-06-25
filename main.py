from CCFD.logger import logging
from CCFD.exception import CreditcardException
import os, sys
from CCFD.utils import get_collection_as_dataframe
from CCFD.entity.config_entity import DataIngestionConfig
from CCFD.entity import config_entity
from CCFD.components.data_ingestion import DataIngestion
from CCFD.entity.config_entity import TrainingPipelineConfig


# def test_logger_and_exception():
#   try:
#      logging.info("Starting the test_logger_and_exception")
#     result = 3/0
#    print(result)
#   logging.info("Ending point of the test_logger_and_exception")
# except Exception as e:
#    logging.debug(str(e))
#   raise InsuranceException(e,sys)

if __name__ == "__main__":
    try:
        # start_training_pipeline()
        # test_logger_and_exception()
        # get_collection_as_dataframe(database_name = "AMEX_CREDITCARD", collection_name = "CCFD_PROJECT")
        training_pipeline_config = config_entity.TrainingPipelineConfig()

        # data ingestion
        data_ingestion_config = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        

        data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

    except Exception as e:
        raise CreditcardException(e, sys)
    
