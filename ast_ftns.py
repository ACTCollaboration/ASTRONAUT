from pathlib import Path

MODULE_DIR = Path(__file__).resolve().parent
FILE_PATH = MODULE_DIR / "asteroid_list.txt"


def ast_names() -> None:
    """
    Print available asteroid names in the API
    """

    # Create a set to store unique parts of the strings
    unique_parts = set()

    with open(FILE_PATH, "r") as file:
        for line in file:
            # Strip any leading/trailing whitespace (including newlines)
            cleaned_line = line.strip()

            underscore_index = cleaned_line.find("_")

            # Extract the part of the string before the first underscore
            if underscore_index != -1:
                part = cleaned_line[:underscore_index]
                unique_parts.add(part)

    sorted_unique_parts = sorted(unique_parts)

    for part in sorted_unique_parts:
        print(part)


def find_ast(ast: str) -> None:
    """
    Input: asteroid name
    Output: print current asteroids in API
    """

    with open(FILE_PATH, "r") as file:
        for line in file:
            if ast in line:
                print(line, end="")
            else:
                continue


def find_arr(arr: str) -> None:
    """
    Input: ACT array: pa4, pa5, pa6
    Output: print current asteroids in API corresponding to arr
    """

    with open(FILE_PATH, "r") as file:
        for line in file:
            if arr in line:
                print(line, end="")
            else:
                continue


def find_freq(freq: str) -> None:
    """
    Input: frequency (GHz): 090, 150, 220
    Output: print current asteroids in API corresponding to freq
    """

    with open(FILE_PATH, "r") as file:
        for line in file:
            if freq in line:
                print(line, end="")
            else:
                continue
