import pandas as pd
import os


class CardiovascularDataExtractor:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def load_data(self) -> pd.DataFrame:
        """ Load  data from Excel    """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"The file at {self.file_path} was not found.")
        try:
            data = pd.read_excel(self.file_path, sheet_name='Sheet1')
            return data
        except Exception as e:
            raise Exception(f"Error loading data from Excel: {e}")
