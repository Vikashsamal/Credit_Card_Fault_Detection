import pandas as pd
import numpy as np
import os, sys
from CCFD.exception import CreditcardException
from CCFD.entity import artifact_entity
from CCFD.entity import config_entity
from CCFD import utils
from CCFD.logger import logging
from sklearn.model_selection import train_test_split


class DataIngestion:  # data will be divided to Train, Test and Validate.
    def __init__(self, data_ingestion_config: config_entity.DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CreditcardException(e, sys)

    def initiate_data_ingestion(self) -> artifact_entity.DataIngestionArtifact:
        try:
            logging.info("Export collection data as pandas dataframe")
            # Exporting collection data as pandas dataframe
            df: pd.DataFrame = utils.get_collection_as_dataframe(
                database_name=self.data_ingestion_config.database_name,
                collection_name=self.data_ingestion_config.collection_name)

            logging.info("Save data in future store")

            # Replace NA value with NAN.
            df.replace(to_replace="na", value=np.NAN, inplace=True)

            # Save data in future store
            logging.info("Create feature store folder if not available.")
            feature_store_dir = os.path.dirname(self.data_ingestion_config.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)

            logging.info("Save df to feature store folder")
            # Save df to feature store folder   
            df.to_csv(path_or_buf=self.data_ingestion_config.feature_store_file_path, index=False, header=True)

            logging.info("Splitting our data into train and test set.")
            train_df, test_df = train_test_split(df, test_size=self.data_ingestion_config.test_size, random_state=1)

            logging.info("Create dataset directory folder if not exists")
            dataset_dir = os.path.dirname(self.data_ingestion_config.train_file_path)
            os.makedirs(dataset_dir, exist_ok=True)

            logging.info("Save dataset to feature store folder.")
            train_df.to_csv(path_or_buf=self.data_ingestion_config.train_file_path, index=False, header=True)
            test_df.to_csv(path_or_buf=self.data_ingestion_config.test_file_path, index=False, header=True)

            # Prepare artifact folder
            data_ingestion_artifact = artifact_entity.DataIngestionArtifact(
                feature_store_file_path=self.data_ingestion_config.feature_store_file_path,
                train_file_path=self.data_ingestion_config.train_file_path,
                test_file_path=self.data_ingestion_config.test_file_path
            )
            logging.info(f"Data ingestion artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise CreditcardException(e, sys)
