"""Calculate the cost of throwing a party for x amount of people"""

__author__: str = "730705182"


def main_planner(guests: int) -> None:
    """Function that brings all of the functions together"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(int(treats(people=guests))))
    print(
        "Cost: "
        + "$"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """A function to compute the number of tea bags needed based on number of guests"""
    return people * 2


tea_bags(people=1)


def treats(people: int) -> int:
    """A function to compute the number of treats needed based on the number of tea guests are expecting to drink"""
    return tea_bags(people=people) * 1.5


def cost(tea_count: int, treat_count: int) -> float:
    """A function to compute the cost of the tea bags and the treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
