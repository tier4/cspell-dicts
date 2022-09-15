import argparse
from pathlib import Path


def fix_yaml_extension(file_path: Path) -> int:
    return file_path.suffix == ".yaml"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_paths", nargs="*", type=Path)
    args = parser.parse_args(argv)

    return_code = 0
    file_path: Path
    for file_path in args.file_paths:
        if not fix_yaml_extension(file_path):
            print(f"Fixing {file_path}")
            file_path.rename(file_path.with_suffix(".yaml"))
            return_code = 1

    return return_code


if __name__ == "__main__":
    exit(main())
