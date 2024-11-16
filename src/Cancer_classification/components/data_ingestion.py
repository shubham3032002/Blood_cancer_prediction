import os
import zipfile
import gdown
from src.Cancer_classification import logger
from src.Cancer_classification.utils.common import get_size

from Cancer_classification.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self) -> str:
        '''Fetch data from the URL'''
        try:
            dataset_url = self.config.source_URL  # Correct attribute name
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into {zip_download_dir}")

            gdown.download(dataset_url, zip_download_dir, quiet=False,fuzzy=True)  # Download file using gdown
            logger.info(f"Download complete: {zip_download_dir}")
        except Exception as e:
            logger.error(f"Error downloading file: {e}")
            raise e

    def extract_zip_file(self):
        '''Extract the zip file to the unzip directory'''
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)
            logger.info(f"Extraction complete to {unzip_path}")
        except Exception as e:
            logger.error(f"Error extracting file: {e}")
            raise e