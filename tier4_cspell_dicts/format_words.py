import argparse
from pathlib import Path


def format_words(file_path: Path) -> bool:
    content = file_path.read_text()
    lines = content.splitlines()
    words = [word for word in lines if word and not word.startswith("#")]

    formatted_lines = ["# cspell-tools: keep-case no-split", ""] + sorted(
        words, key=lambda s: (str.casefold(s), s)
    )
    formatted = "\n".join(formatted_lines) + "\n"
    if formatted != content:
        file_path.write_text(formatted)
        return False

    return True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_paths", nargs="*", type=Path)
    args = parser.parse_args(argv)

    return_code = 0
    file_path: Path
    for file_path in args.file_paths:
        if not format_words(file_path):
            print(f"Fixing {file_path}")
            return_code = 1

    return return_code


if __name__ == "__main__":
    exit(main())
