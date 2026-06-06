"""Entry point — run with `python3 main.py` from the starter/ directory."""

from gradebook import RECORDS, format_report


if __name__ == "__main__":
    print(format_report(RECORDS))
def average_per_student(records: list[dict]) -> dict[str, float]:
    scores = {}

    for record in records:
        name = record["name"]
        score = record["score"]

        scores.setdefault(name, []).append(score)

    averages = {}

    for name, marks in scores.items():
        averages[name] = round(sum(marks) / len(marks), 2)

    return averages


def subjects_offered(records: list[dict]) -> set[str]:
    return {record["subject"] for record in records}


def top_scorer(records: list[dict]) -> tuple[str, float]:
    averages = average_per_student(records)
    return max(averages.items(), key=lambda x: x[1])


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    averages = average_per_student(records)

    passed = []

    for name, avg in averages.items():
        if avg >= threshold:
            passed.append(name)

    return sorted(passed)
