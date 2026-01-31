def calculate_roi(
    avg_time_before_min: float,
    avg_time_after_min: float,
    cases_per_day: int,
    cost_per_hour: float,
    automation_cost_per_month: float
) -> dict:
    """
    Calculate ROI of automation based on time savings.
    Assumptions are explicitly defined for transparency.
    """

    time_saved_per_case_min = max(avg_time_before_min - avg_time_after_min, 0)

    monthly_time_saved_hours = (
        time_saved_per_case_min * cases_per_day * 22
    ) / 60  # 22 working days

    monthly_cost_savings = monthly_time_saved_hours * cost_per_hour

    roi = (monthly_cost_savings - automation_cost_per_month) / automation_cost_per_month

    return {
        "monthly_time_saved_hours": round(monthly_time_saved_hours, 2),
        "monthly_cost_savings": round(monthly_cost_savings, 2),
        "automation_cost_per_month": automation_cost_per_month,
        "roi": round(roi, 2),
    }


if __name__ == "__main__":
    result = calculate_roi(
        avg_time_before_min=17.4,
        avg_time_after_min=6.6,
        cases_per_day=120,
        cost_per_hour=25,
        automation_cost_per_month=1500,
    )

    print("=== ROI ESTIMATION ===")
    for k, v in result.items():
        print(f"{k}: {v}")
