"""Create a dictionary"""

__author__: str = "730705182"

from dictionary import invert


def test_invert_empty_dict():
    """Test invert with an empty dictionary (Edge Case)"""
    assert invert({}) == {}


def test_invert_single_pair():
    """Test invert with a single key-value pair (Use Case 1)"""
    assert invert({"b": "a"}) == {"a": "b"}


def test_invert_multiple_pairs():
    """Test invert with multiple key-value pairs (Use Case 2)"""
    assert invert({"a": "x", "b": "z", "c": "w"})


from dictionary import count


def test_count_empty_list():
    """Test count with an empty list"""
    assert count([]) == {}


def test_count_unique_items():
    assert count(["apple", "banana", "cherry"]) == {
        "apple": 1,
        "banana": 1,
        "cherry": 1,
    }


def test_count_duplicates():
    assert count(["red", "blue", "red", "blue", "blue"]) == {"red": 2, "blue": 3}


from dictionary import favorite_color


def test_favoritecolor_empty():
    """Test favorite_color with an empty dictionary"""
    assert favorite_color({}) is None


def test_favorite_color_one_color():
    """Test favorite_color with a single color in the dictionary"""
    assert favorite_color({"Alice": "blue"}) == "blue"


def test_favorite_color_multiple_colors():
    """Test favorite_color with multiple colors in the dictionary"""
    assert (
        favorite_color({"Alice": "blue", "Bob": "blue", "Charlotte": "green"}) == "blue"
    )
