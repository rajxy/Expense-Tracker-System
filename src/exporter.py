import pandas as pd

class TransactionExporter:
    """Engine for exporting financial transaction summaries to CSV, Excel, or JSON."""

    @staticmethod
    def export_data(dataframe, format_type="excel", filename="export_summary"):
        format_type = format_type.lower()
        
        if format_type == "csv":
            out_file = f"{filename}.csv"
            dataframe.to_csv(out_file, index=False)
        elif format_type == "excel":
            out_file = f"{filename}.xlsx"
            dataframe.to_excel(out_file, index=False, engine="openpyxl")
        elif format_type == "json":
            out_file = f"{filename}.json"
            dataframe.to_json(out_file, orient="records", indent=4)
        else:
            raise ValueError("Unsupported format! Supported formats: csv, excel, json")

        return out_file
