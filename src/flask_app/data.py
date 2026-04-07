from __future__ import annotations

import os
from pathlib import Path

import pandas as pd


DEFAULT_COLUMNS = [
    "ID",
    "Date",
    "Primary Type",
    "Description",
    "Arrest",
    "Domestic",
    "District",
    "Ward",
    "Community Area",
    "Latitude",
    "Longitude",
]


def load_crime_data() -> pd.DataFrame:
    """
    Load the Chicago crime dataset for the web app.

    The actual dataset file is expected to be provided outside git (large file).
    Configure its location with CHAGGG_DATA_PATH.
    """
    env_path = os.environ.get("CHAGGG_DATA_PATH")
    candidate_paths: list[Path] = []
    if env_path:
        candidate_paths.append(Path(env_path))

    candidate_paths.extend(
        [
            Path("data") / "manipulated" / "crimes.parquet",
            Path("data") / "manipulated" / "crimes.csv",
            Path("data") / "processed" / "crimes.parquet",
            Path("data") / "processed" / "crimes.csv",
            Path("data") / "raw" / "crimes.csv",
            Path("data") / "test" / "crimes.csv",
        ]
    )

    for path in candidate_paths:
        try:
            if not path.exists() or not path.is_file():
                continue
            if path.suffix.lower() == ".parquet":
                return pd.read_parquet(path)
            if path.suffix.lower() == ".csv":
                return pd.read_csv(path)
        except Exception:
            # Keep the app bootable even if data loading fails.
            break

    return pd.DataFrame(columns=DEFAULT_COLUMNS)

