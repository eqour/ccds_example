import pandas as pd
import sys


def clean_csv(input_path, output_path):
    df = pd.read_csv(input_path)
    df_cleaned = df.dropna(subset=['price'])
    df_cleaned.to_csv(output_path, index=False)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python clean_cpu_data.py <input_path> <output_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    clean_csv(input_file, output_file)
