from typing import List, Optional


def calculate_average(numbers: List[float]) -> Optional[float]:
    if not numbers:
        return None
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


def main():
    data = [1.0, 2.0, 3.0, 4.0]
    result = calculate_average(data)
    if result is not None:
        print(f"The average is: {result}")
    else:
        print("The list is empty.")


if __name__ == "__main__":
    main()
