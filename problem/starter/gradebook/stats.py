"""gradebook.stats — aggregate statistics over grade records."""


def average_per_student(records: list[dict]) -> dict[str, float]:
    """Map each student name to their average score, rounded to 2 decimals."""
    def average_per_student(records):
    averages = {}

    for record in records:
        name = record["name"]
        score = record["score"]

        if name not in averages:
            averages[name] = []

        averages[name].append(score)

    for name in averages:
        averages[name] = round(sum(averages[name]) / len(averages[name]), 2)

    return averages
    # TODO: implement
    pass


def subjects_offered(records: list[dict]) -> set[str]:
    """Return the set of unique subjects across all records."""
    def subjects_offered(records):
    subjects = set()

    for record in records:
        subjects.add(record["subject"])

    return subjects
    # TODO: implement
    pass


def top_scorer(records: list[dict]) -> tuple[str, float]:
    """Return (name, average) for the student with the highest average."""
    def top_scorer(records):
    averages = average_per_student(records)

    top_name = ""
    top_avg = 0

    for name, avg in averages.items():
        if avg > top_avg:
            top_name = name
            top_avg = avg

    return (top_name, top_avg)
    # TODO: implement
    pass


def passing_students(records: list[dict], threshold: float = 60.0) -> list[str]:
    """Return names whose average >= threshold, sorted alphabetically."""
    def passing_students(records, threshold=60.0):
    averages = average_per_student(records)

    passed = []

    for name, avg in averages.items():
        if avg >= threshold:
            passed.append(name)

    passed.sort()

    return passed
    # TODO: implement
    pass
