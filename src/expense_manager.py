import os
import pandas as pd
from src.validator import DataValidator

class ExpenseManager:
    def __init__(self, data_path="data/expenses.csv"):
        self.data_path = data_path
        self.columns = ["id", "date", "title", "amount", "category", "tags"]
        self._init_storage()

    def _init_storage(self):
        os.makedirs(os.path.dirname(self.data_path), exist_ok=True)
        if not os.path.exists(self.data_path):
            df = pd.DataFrame(columns=self.columns)
            df.to_csv(self.data_path, index=False)

    def add_expense(self, title, amount, category, tags=None, date=None):
        """Adds expense entry with input validation and custom tagging."""
        valid_amount = DataValidator.validate_amount(amount)
        valid_date = DataValidator.validate_date(date)
        
        df = pd.read_csv(self.data_path)
        new_id = 101 if df.empty else df["id"].max() + 1
        tag_str = ",".join([t.strip().lower() for t in tags]) if tags else "general"

        new_entry = {
            "id": new_id,
            "date": valid_date,
            "title": title.strip(),
            "amount": valid_amount,
            "category": category.strip().capitalize(),
            "tags": tag_str
        }

        df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
        df.to_csv(self.data_path, index=False)
        return new_entry

    def filter_expenses(self, category=None, min_amount=None, max_amount=None, tag=None, start_date=None, end_date=None):
        """Multi-parameter filtering engine."""
        df = pd.read_csv(self.data_path)
        if df.empty:
            return df

        if category:
            df = df[df["category"].str.lower() == category.lower()]
        if min_amount is not None:
            df = df[df["amount"] >= min_amount]
        if max_amount is not None:
            df = df[df["amount"] <= max_amount]
        if tag:
            df = df[df["tags"].str.contains(tag.lower(), na=False)]
        if start_date and end_date:
            df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

        return df
