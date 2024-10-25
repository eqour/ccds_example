from pathlib import Path

import typer
from loguru import logger
from tqdm import tqdm

from ccds_example.config import PROCESSED_DATA_DIR

app = typer.Typer()


def calculate_age_stats(df):
    """Вычисляет статистические данные для возраста."""
    mean_age = df['age'].mean()
    std_age = df['age'].std()
    median_age = df['age'].median()
    return mean_age, std_age, median_age


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = PROCESSED_DATA_DIR / "dataset.csv",
    output_path: Path = PROCESSED_DATA_DIR / "features.csv",
    # -----------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Generating features from dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Features generation complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
