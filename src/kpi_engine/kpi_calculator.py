import pandas as pd


def compute_kpis(df: pd.DataFrame) -> dict:
    """
    Compute core operational KPIs for transaction banking operations.
    """
    return {
        "average_processing_time_minutes": round(df["processing_time"].mean(), 2),
        "manual_review_rate_percent": round(df["manual_review"].mean() * 100, 2),
        "error_rate_percent": round(df["error_flag"].mean() * 100, 2),
        "sla_breach_rate_percent": round(df["sla_breach"].mean() * 100, 2),
    }


if __name__ == "__main__":
    before_df = pd.read_csv("data/before_automation.csv")
    after_df = pd.read_csv("data/after_automation.csv")

    before_kpis = compute_kpis(before_df)
    after_kpis = compute_kpis(after_df)

    print("=== KPIs BEFORE AUTOMATION ===")
    for k, v in before_kpis.items():
        print(f"{k}: {v}")

    print("\n=== KPIs AFTER AUTOMATION ===")
    for k, v in after_kpis.items():
        print(f"{k}: {v}")
