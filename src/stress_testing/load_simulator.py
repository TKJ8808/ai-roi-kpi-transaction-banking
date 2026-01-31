import random
import pandas as pd


def simulate_operational_load(volume: int) -> pd.DataFrame:
    """
    Simulate transaction banking operational load under stress conditions.
    """
    data = []

    for case_id in range(1, volume + 1):
        processing_time = random.gauss(mu=6, sigma=2)

        manual_review = 1 if random.random() < min(0.2 + volume / 1000, 0.6) else 0
        error_flag = 1 if random.random() < min(0.05 + volume / 2000, 0.3) else 0
        sla_breach = 1 if processing_time > 10 or error_flag == 1 else 0

        data.append([
            case_id,
            round(max(processing_time, 1), 2),
            manual_review,
            error_flag,
            sla_breach
        ])

    return pd.DataFrame(
        data,
        columns=[
            "case_id",
            "processing_time",
            "manual_review",
            "error_flag",
            "sla_breach"
        ]
    )


if __name__ == "__main__":
    print("=== STRESS TESTING RESULTS ===")

    for volume in [50, 100, 250, 500]:
        df = simulate_operational_load(volume)

        sla_breach_rate = round(df["sla_breach"].mean() * 100, 2)
        avg_time = round(df["processing_time"].mean(), 2)

        print(
            f"Volume={volume} | "
            f"Avg Time={avg_time} min | "
            f"SLA Breach Rate={sla_breach_rate}%"
        )
