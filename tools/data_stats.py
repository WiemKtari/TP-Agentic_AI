import pandas as pd
from langchain.tools import BaseTool

class DataStatsTool(BaseTool):
    name = "data_statistics"
    description = "Computes statistics and data quality metrics for a CSV file"

    def _run(self, csv_path: str):
        df = pd.read_csv(csv_path)
        return {
            "shape": df.shape,
            "missing_values": df.isna().sum().to_dict(),
            "mean": df.select_dtypes("number").mean().to_dict(),
            "cardinality": df.nunique().to_dict()
        }

    async def _arun(self, *args, **kwargs):
        raise NotImplementedError("Async not supported")
