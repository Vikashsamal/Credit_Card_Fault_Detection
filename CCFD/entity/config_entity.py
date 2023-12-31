import os, sys
from CCFD.exception import CreditcardException
from CCFD.logger import logging
from datetime import datetime

FILE_NAME = "credit_card.csv"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"


class TrainingPipelineConfig:
    def __init__(self):
        try:
            self.artifact_dir = os.path.join(os.getcwd(),"artifact",f"{datetime.now().strftime('%m%d%Y__%H%M%S')}")
        except Exception as e:
            raise CreditcardException(e, sys)

class DataIngestionConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig): # Define Constructor
        try:
            self.database_name = "AMEX_CREDITCARD"
            self.collection_name = "CCFD"
            self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir, "data_ingestion")
            self.feature_store_file_path = os.path.join(self.data_ingestion_dir, "feature_store", FILE_NAME)
            self.train_file_path = os.path.join(self.data_ingestion_dir, "dataset", TRAIN_FILE_NAME)
            self.test_file_path = os.path.join(self.data_ingestion_dir, "dataset", TEST_FILE_NAME)
            self.test_size = 0.2
        except Exception as e:
            raise CreditcardException(e, sys)
    
    # Convert data into dicionary
    def to_dict(self,)->dict:
        try:
            return self.__dict__
        except Exception as e:
            raise CreditcardException(e, sys)


        
