def parse_filename(file_path: str) -> str:
    path = file_path.split("/")
    return path[-1].split(".")[0]
