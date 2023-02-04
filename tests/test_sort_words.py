from pathlib import Path

from tier4_cspell_dicts import format_words


def test(datadir: Path) -> None:
    input_file = datadir / "words.input.txt"
    answer_file = datadir / "words.answer.txt"

    # Format
    return_code = format_words.main([str(input_file)])
    assert return_code == 1
    assert input_file.read_text() == answer_file.read_text()

    # Re-format
    return_code = format_words.main([str(input_file)])
    assert return_code == 0
    assert input_file.read_text() == answer_file.read_text()
