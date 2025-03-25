"""Create a dictionary"""

__author__: str = "730705182"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of a dictionary."""
    inverted_dict = {}

    for key, value in input_dict.items():
        if value in inverted_dict:
            raise KeyError("Duplicate values found, cannot invert")
        inverted_dict[value] = key

    return inverted_dict


def count(input_list: list[str]) -> dict[str, int]:
    """Counts the occurences of each string in the list and returns a dictionary"""
    count_dict: dict[str, int] = {}

    for item in input_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict


def favorite_color(input_dict: dict[str, str]) -> str:
    """Determines the most frequent color in the dictionary. In case of a tie, return the first occurring color"""
    color_count: dict[str, int] = {}

    for name, color in input_dict.items():
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    most_frequent = None
    max_count = 0

    for color, count in color_count.items():
        if count > max_count:
            most_frequent = color
            max_count = count

    return most_frequent
