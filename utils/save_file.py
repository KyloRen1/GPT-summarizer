def save_txt(save_path: str, text: str) -> None:
    with open(str(save_path) + ".txt", "w") as f:
        f.write(text)
    print(f"----- file save to {save_path} -----")
