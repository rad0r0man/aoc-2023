def puzzle_reader(file_name: str) -> list:
    return [line.rstrip() for line in open(file_name)]
