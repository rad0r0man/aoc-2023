def puzzle_reader(file_name: str) -> list:
    with open(file_name, "r") as f:
        return [line.rstrip() for line in f]
