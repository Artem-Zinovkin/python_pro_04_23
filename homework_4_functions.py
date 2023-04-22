from __future__ import annotations

from typing import Any


def players_repr(players: list[dict]) -> None:
    for i in players:
        print(
            f"player №{i['number']}\
 :name - {i['name'].capitalize()}, age - {i['age']} years"
        )


def players_add(players: list[dict], player: dict) -> list[dict]:
    players.append(player)
    return players


def players_del(players: list[dict], name: str) -> list[dict]:
    [
        players.remove(i)
        for i in players
        if i["name"].lower().strip() == name.lower().strip()
    ]
    return players


def players_find(players: list[dict], field: str, value: Any) -> list[dict]:
    new_players_find = []
    [
        new_players_find.append(i)
        for i in players
        if str(i[field]).lower().strip() == value.lower().strip()
    ]
    return new_players_find


def players_get_by_name(players: list[dict], name: str) -> dict | None:
    for i in players:
        if i["name"].lower().strip() == name.lower().strip():
            return i


def main():
    team = [
        {"name": "John", "age": 20, "number": 1},
        {"name": "Marry", "age": 33, "number": 3},
        {"name": "Cavin", "age": 33, "number": 12},
    ]

    options = ["repr", "add", "del", "find", "get"]

    while True:
        if not (user_input := input(f"Enter your choice {options}:")):
            break

        if user_input == "add":
            new_player = input(
                "Enter new player in the format: name, age, number\n"
            ).split(",")
            new_player = {
                "name": new_player[0],
                "age": new_player[1],
                "number": new_player[2],
            }
            players_add(players=team, player=new_player)

        elif user_input == "del":
            del_ = input("Enter name player ")
            players_del(team, del_)

        elif user_input == "get":
            get = input("Enter name player ")
            player = players_get_by_name(team, get)
            if player is None:
                print("not found")
            else:
                print(
                    f"player №{player['number']}\
    : name - {player['name'].capitalize()},\
    age - {player['age']} years"
                )

        elif user_input == "find":
            field, value = input(
                "Enter in the format:\
field, value "
            ).split(",")
            player = players_find(team, field=field, value=value)
            if len(player) != 0:
                players_repr(player)
            else:
                print("not found")

        elif user_input == "repr":
            players_repr(team)


if __name__ == "__main__":
    main()
