import pandas as pd
from langchain.tools import BaseTool

class CSVReaderTool(BaseTool):
    name = "csv_reader"
    description = "Reads a CSV file. Input must be a valid csv_path."

    def _run(self, file_path: str, n: int = 5):
        df = pd.read_csv(csv_path)
        return {
            "columns": list(df.columns),
            "head": df.head(n).to_dict()
        }
    
