from datetime import datetime

class DataValidator:
    """Ensures input validation and data integrity across all transaction workflows."""

    @staticmethod
    def validate_amount(amount_str):
        try:
            val = float(amount_str)
            if val <= 0:
                raise ValueError("Amount must be greater than zero.")
            return round(val, 2)
        except ValueError as e:
            raise ValueError(f"Invalid Amount: {e}")

    @staticmethod
    def validate_date(date_str):
        """Validates date format (YYYY-MM-DD). Default to today if empty."""
        if not date_str:
            return datetime.now().strftime("%Y-%m-%d")
        try:
            valid_date = datetime.strptime(date_str, "%Y-%m-%d")
            return valid_date.strftime("%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid Date format! Please use YYYY-MM-DD.")
