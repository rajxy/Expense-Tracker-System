import pandas as pd

class BudgetReporter:
    def __init__(self, data_path="data/expenses.csv"):
        self.data_path = data_path

    def generate_monthly_summary(self, month_year):
        """
        Calculates monthly budget analysis and spending insights (e.g., month_year = '2026-03').
        """
        df = pd.read_csv(self.data_path)
        if df.empty:
            return "No transaction history available."

        df["month"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m")
        monthly_data = df[df["month"] == month_year]

        if monthly_data.empty:
            return f"No expenses logged for {month_year}."

        total_spent = monthly_data["amount"].sum()
        category_breakdown = monthly_data.groupby("category")["amount"].sum().to_dict()
        top_category = monthly_data.groupby("category")["amount"].sum().idxmax()

        report = {
            "Month": month_year,
            "Total Spending": f"${total_spent:.2f}",
            "Top Spending Category": top_category,
            "Category Breakdown": category_breakdown
        }

        return report
