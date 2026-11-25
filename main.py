import os

LINE = "The meeting could have been an email, the email could have been a sentence, and the sentence was 'no'."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
