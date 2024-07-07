import os
import urllib.request as request
from zipfile import ZipFile
from deepClassifier.entity import DataIngestionConfig
from deepClassifier import logger
from deepClassifier.utils import get_size
from tqdm import tqdm
from pathlib import Path
import opendatasets as od
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi
import shutil

# Initialize Kaggle API


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        logger.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logger.info("Download started...")
            download_path = os.path.dirname(self.config.local_data_file)
            api = KaggleApi()
            api.authenticate()
            api.dataset_download_files("prasunroy/natural-images", path= download_path, unzip= False)

            logger.info(f"Data Set downloaded successfully")

        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")
 

    def _get_updated_list_of_files(self, list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg") and \
                ("airplane" in f or "car" in f or "cat" in f or \
                 "dog" in f or "flower" in f or "fruit" in f or \
                    "motorbike" in f or "person" in f)]

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:
            logger.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)
        
        junk_folder = os.path.join(working_dir,"data")
        if os.path.exists(junk_folder):
            shutil.rmtree(junk_folder)

    def unzip_and_clean(self):
        logger.info(f"unzipping file and removing unawanted files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)